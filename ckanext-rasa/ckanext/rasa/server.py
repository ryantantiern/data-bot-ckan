import argparse
import logging
import os
from data_bot.main.extended import ExtendedRasaCoreServer, ExtendedRedisTrackerStore
from data_bot.main.main import MODEL_PATH, INTEPRETER_PATH, dir_path
from rasa_core.domain import TemplateDomain
import rasa_core.utils as utils

logger = logging.getLogger(__name__)

def create_argument_parser():
    """Parse all the command line arguments for the server script."""

    parser = argparse.ArgumentParser(
            description='starts server to serve an agent')
    parser.add_argument(
            '-d', '--core',
            type=str,
            help="core model to run with the server")
    parser.add_argument(
            '-u', '--nlu',
            type=str,
            help="nlu model to run with the server")
    parser.add_argument(
            '-p', '--port',
            type=int,
            default=5005,
            help="port to run the server at")
    parser.add_argument(
            '--cors',
            nargs='*',
            type=str,
            help="enable CORS for the passed origin. "
                 "Use * to whitelist all origins")
    parser.add_argument(
            '--auth_token',
            type=str,
            help="Enable token based authentication. Requests need to provide "
                 "the token to be accepted.")
    parser.add_argument(
            '-o', '--log_file',
            type=str,
            default="rasa_core.log",
            help="store log file in specified file")

    utils.add_logging_option_arguments(parser)
    return parser


if __name__ == "__main__":
    # Running as standalone python application
    
    arg_parser = create_argument_parser()
    cmdline_args = arg_parser.parse_args()

    logging.basicConfig(level=cmdline_args.loglevel)

    # Set HTTP log path
    http_logs = os.path.join(dir_path, "bot/logs/http.logs")

    # Load Domain
    domain = TemplateDomain.load(os.path.join(MODEL_PATH, "domain.yml"))

    # Create tracker store
    tracker_store = ExtendedRedisTrackerStore(domain, db=2, timeout=900, mock=False)

    # Initialize Rasa Core Server
    model_directory = MODEL_PATH
    interpreter = INTEPRETER_PATH
    rasa = ExtendedRasaCoreServer(model_directory,
                                  interpreter,
                                  cmdline_args.loglevel,
                                  http_logs,
                                  cmdline_args.cors,
                                  auth_token = cmdline_args.auth_token,
                                  tracker_store=tracker_store)

    logger.info("Started http server on port %s" % cmdline_args.port)

    # Run Rasa Core Server
    rasa.app.run("0.0.0.0", cmdline_args.port)
