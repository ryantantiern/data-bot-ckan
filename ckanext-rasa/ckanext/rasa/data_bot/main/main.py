from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import argparse
import warnings
import os

from rasa_core                  import utils
# from rasa_core.agent            import Agent
# from rasa_core.interpreter      import RasaNLUInterpreter

MODEL_PATH = os.path.abspath("models/dialogue")
INTEPRETER_PATH = os.path.abspath("models/nlu/default/13_3_2018")
AGENT_PKL_PATH = os.path.abspath("agent.pkl")


logger = logging.getLogger(__name__)

# def load_agent():
#     interpreter = RasaNLUInterpreter(INTEPRETER_PATH)
#     agent = Agent.load(MODEL_PATH, interpreter=interpreter)
#     return agent

def handle_message(text=None,sender_id=None):
    return agent.handle_message(text)