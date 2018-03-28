from unittest import TestCase, main
import os.path as path
from ckanext.rasa.data_bot.main.main import INTEPRETER_PATH, MODEL_PATH
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.events import UserUttered,Restarted
from rasa_core.domain import TemplateDomain

DOMAIN_PATH = path.join(MODEL_PATH, "domain.yml")

class TestStoriesChatFlow(TestCase):

	def setUp(self):
		interpreter = RasaNLUInterpreter(INTEPRETER_PATH, lazy_init=True)
		self.agent = Agent.load(MODEL_PATH, interpreter)
		self.domain = TemplateDomain.load(DOMAIN_PATH)
		self.templates_offer_help =  [data["text"] for data in self.domain.templates["action_offer_help"]]
		self.templates_greet = [data["text"] for data in self.domain.templates["action_greet"]]
		self.templates_help = [
			"Currently I can source data."
		]
		self.templates_source_data_prompt_tags = [data["text"] for data in self.domain.templates["action_source_data_prompt_tags"]]
		self.templates_reoffer_help = [data["text"] for data in self.domain.templates["action_reoffer_help"]]

	def test_greet(self):

		response = self.agent.handle_message("/greet", sender_id="default")
		self.assertEqual(len(response), 2)
		self.assertIn(response[0], self.templates_greet)
		self.assertIn(response[1], self.templates_offer_help)
		self.agent.tracker_store.get_or_create_tracker("default").update(Restarted())

	def test_requestHelp(self):
		m = "/requestHelp"
		self.agent.handle_message("/greet", sender_id="default")
		response = self.agent.handle_message(m, sender_id="default")
		self.assertIn(response[0], self.templates_help)
		self.assertIn(response[1], self.templates_offer_help)
		self.agent.tracker_store.get_or_create_tracker("default").update(Restarted())
	
	def test_sourceDataPromptParameters(self):
		context = [
			"/greet",
		]
		m ="/sourceData"
		for c in context:
			self.agent.handle_message(c, sender_id="default")
		response = self.agent.handle_message(m, sender_id="default")
		self.assertIn(response[0], self.templates_source_data_prompt_tags)
		self.agent.tracker_store.get_or_create_tracker("default").update(Restarted())
	
	def test_sourceDataOneTag(self):
		context = [
			"/greet"
		]
		m = '/sourceData{"tags":"london", "limit":"8"}'
		# DEV = True in actions.py

		for c in context:
			x = self.agent.handle_message(c, sender_id="default")
		response = self.agent.handle_message(m, sender_id="default")
		self.assertEqual(response[0], "Searching for datasets that have tag london limited to top 8 results:\n1. This is currently in development!")
		self.assertIn(response[1], self.templates_reoffer_help)
		self.agent.tracker_store.get_or_create_tracker("default").update(Restarted())

	def test_sourceDataMultipleTags(self):
		context = [
				"/greet"
		]
		m = '/sourceData{"tags":["london", "transport"], "limit":"8"}'
		for c in context:
			x = self.agent.handle_message(c, sender_id="default")
		response = self.agent.handle_message(m, sender_id="default")
		self.assertEqual(response[0], "Searching for datasets that have tags london transport limited to top 8 results:\n1. This is currently in development!")
		self.agent.tracker_store.get_or_create_tracker("default").update(Restarted())


if __name__ == "__main__":
	main()