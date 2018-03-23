import unittest
from unittest import TestCase
from ckanext.rasa.data_bot.main.main import INTEPRETER_PATH, MODEL_PATH
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.events import UserUttered,Restarted

class TestStoriesChatFlow(TestCase):

	def setUp(self):
		interpreter = RasaNLUInterpreter(INTEPRETER_PATH, lazy_init=True)
		self.agent = Agent.load(MODEL_PATH, interpreter)
		self.templates_offer_help =  [
			"What can I do for you?",
			"How can I be of assistance?",
			"What would you like me to do?",
			"What shall we do today?"
		]
		self.templates_greet = [
			"Hi, I'm DataBot!",
			"Hello there, I'm DataBot!",
			"I'm DataBot. Nice to make your acquaintance."
		]
		self.templates_help = [
			"Currently I can source data."
		]
		self.templates_source_data_prompt_tags = [
			"Great! What data would you like?",
			"Excellent! What data are you searching for?",
			"Wonderful! What kind of data are you looking for?",
			"Sure, what are the search terms?",
		]
		self.templates_sourceData = [
			"Is there anything else I can do for you?",
			"How else can I help you?"
		]
		
	def test_greet(self):

		response = self.agent.handle_message("/greet", sender_id="default")
		self.assertEqual(len(response), 2)
		self.assertIn(response[0], self.templates_greet)
		self.assertIn(response[1], self.templates_offer_help)
		self.agent.tracker_store.get_or_create_tracker("default").update(Restarted())

	def test_requestHelp(self):
		m = "/requestHelp"
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
		self.assertIn(response[0], self.templates_sourceData)
		self.agent.tracker_store.get_or_create_tracker("default").update(Restarted())

	def test_sourceDataMultipleTags(self):
		context = [
				"/greet"
		]
		m = '/sourceData{"tags":["london", "transport"], "limit":"8"}'
		for c in context:
			x = self.agent.handle_message(c, sender_id="default")
		response = self.agent.handle_message(m, sender_id="default")
		self.assertIn(response[0], self.templates_sourceData)
		self.agent.tracker_store.get_or_create_tracker("default").update(Restarted())
	
	def test_greetSpam(self):
		"""
		Should always respond to greets the same way, even if its spam
		"""
		m = "/greet"	
		for i in range(10):
			response = self.agent.handle_message(m, sender_id="default")
			self.assertEqual(len(response), 2)
			self.assertIn(response[0], self.templates_greet)
			self.assertIn(response[1], self.templates_offer_help)
		self.agent.tracker_store.get_or_create_tracker("default").update(Restarted())		

if __name__ == "__main__":
	unittest.main()