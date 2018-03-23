 #!/usr/bin/env python -W ignore::DeprecationWarning
import os.path as path
import argparse
import warnings
import logging

from ckanext.rasa.data_bot.main.main import MODEL_PATH, dir_path, INTEPRETER_PATH
from rasa_core.policies.sklearn_policy import SklearnPolicy
from rasa_core.agent import Agent
from rasa_core.domain import TemplateDomain
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.console import ConsoleInputChannel

DOMAIN_FILE = path.join(dir_path, "domain.yml")
STORIES = path.join(dir_path, "data/stories.md")

logger = logging.getLogger()  # get the root logger


def train_dialogue(domain_file=DOMAIN_FILE, model_path=MODEL_PATH, training_data_file=STORIES):
    agent = Agent(domain=TemplateDomain.load(domain_file), policies=[SklearnPolicy()])
    logger.info("Begin dialogue training")    
    agent.train(filename=training_data_file, max_history=3)
    agent.persist(model_path)

def run():
    logger.info("=======================================================================================================")
    logger.info("Rasa process starting")    
    interpreter = RasaNLUInterpreter(INTEPRETER_PATH)
    agent = Agent.load(MODEL_PATH, INTEPRETER_PATH)
    logger.info("Finished loading agent, starting input channel")
    agent.handle_channel(ConsoleInputChannel())
    logger.info("=======================================================================================================")

if __name__ == "__main__":
    # Log warnings in a separate folder
    warning_fh = logging.FileHandler("logs/warnings.log")
    warning_logger = logging.getLogger("py.warning")
    logging.captureWarnings(True)
    warning_logger.addHandler(warning_fh)

    
    parser = argparse.ArgumentParser(
        description='starts the bot')

    parser.add_argument(
        'task',
        choices = ["nlu", "dialogue", "run"],
        help = "Runs the methods tran_nlu, train_dialogue or run eg. nlu, dialogue, run"
        )
        
    task = parser.parse_args().task
    
    if task == "dialogue":
        train_dialogue()
    if task == "run":
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.DEBUG)
        logging.basicConfig(filename='logs/rasa_core.log',level=logging.DEBUG)
        run()
    else:
        warnings.warn("Need to pass either 'nlu' or 'dialogue'")