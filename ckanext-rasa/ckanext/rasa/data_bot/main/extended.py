"""
Extends rasa_core clases to record data suitable for creating training data(NLU and Stories),
and gather statistics
"""
from rasa_core.processor import MessageProcessor
from rasa_core.channels.direct import CollectingOutputChannel
from rasa_core.agent import Agent
from rasa_core.dispatcher import Dispatcher
from rasa_core.actions.action import ActionListen
from rasa_core.slots import DataSlot
from rasa_core.events import UserUttered
from rasa_core.tracker_store import RedisTrackerStore    
from rasa_core.domain import TemplateDomain
import os.path as path
import json
import csv
import logging

DIR = path.dirname(path.realpath(__file__))
CONVO_STATES_PATH = path.join(DIR, "bot/states/")

logger = logging.getLogger(__name__)

class ExtendedRedisTrackerStore(RedisTrackerStore):
    def __init__(self, domain, mock=False, host='localhost',
                 port=6379, db=2, password=None, timeout=None):
        self.timeout = timeout
        super(ExtendedRedisTrackerStore, self).__init__(domain, mock, host, port, db, password)

    def save(self, tracker, timeout=None):
        timeout = self.timeout
        serialised_tracker = RedisTrackerStore.serialise_tracker(tracker)
        self.red.set(tracker.sender_id, serialised_tracker, ex=timeout)

    def retrieve(self, sender_id):
        stored = self.red.get(sender_id)
        if stored is not None:
            self.red.expire(sender_id, self.timeout)
            return self.deserialise_tracker(sender_id, stored)
        else:
            return None

class ExtendedAgent(Agent):

    def _create_processor(self, preprocessor=None):
        # type: (Callable[[Text], Text]) -> MessageProcessor
        """Instantiates a processor based on the set state of the agent."""

        self._ensure_agent_is_prepared()
        return StatisticalMessageProcessor(
            self.interpreter, self.policy_ensemble, self.domain,
            self.tracker_store, message_preprocessor=preprocessor)


class StatisticalMessageProcessor(MessageProcessor):

    def __init__(self, *args, **kwargs):
        self.high_threshold = 0.5
        self.low_threshold = 0.3
        super(StatisticalMessageProcessor, self).__init__(*args, **kwargs)

    def handle_message(self, message):
        # type: (UserMessage) -> Optional[List[Text]]
        """Handle a single message with this processor."""

        # preprocess message if necessary
        if self.message_preprocessor is not None:
            message.text = self.message_preprocessor(message.text)
        tracker = self._get_tracker(message.sender_id)
        self._handle_message_with_tracker(message, tracker)

        # Ask user to repeat if confidence level too low
        if tracker.latest_message.parse_data["intent"]["confidence"] < self.high_threshold:
            # Ask the user to repeat message
            tracker._paused = True
            self._set_and_execute_next_action("action_give_up", message, tracker)
            tracker._paused = False

        else:
            # Predict next message like normal
            self._predict_and_execute_next_action(message, tracker)
            self._save_tracker(tracker)

        # Log tracker into file
        # try:
        #     Statistics.log_state(CONVO_STATES_PATH, tracker)
        # except IOError as e:
        #     logger.exception("Don't have permissions to write to file")

        # finally:
        if isinstance(message.output_channel, CollectingOutputChannel):
            return [outgoing_message
                    for _, outgoing_message in message.output_channel.messages]
        else:
            return None


    def _set_and_execute_next_action(self, action_name, message, tracker):
        """
        Sets the next action to action_name then execute
        :param action_name: String
        :param tracker: DialogueStateTracker
        :return: void
        """
        # this will actually send the response to the user

        dispatcher = Dispatcher(message.sender_id,
                                message.output_channel,
                                self.domain)

        action = self.domain.action_map[action_name][1]
        self._log_slots(tracker)
        self._run_action(action, tracker, dispatcher)
        self._run_action(ActionListen(), tracker, dispatcher)

class Statistics(object):
    
    @staticmethod
    def log_state(dir_path, tracker):
        filepath = path.join(dir_path, tracker.sender_id + ".log")
        with open(filepath, 'a') as f:
            string = json.dumps(tracker.current_state()) + "\n"
            f.write(string)

    def _convert_json_into_csv(self, input_filepath, output_filepath):
        data = []
        with open(input_filepath, 'r') as f:
            # convert each line into a csv string
            for line in f:
                line_data = json.loads(line)
                intent_ranking = line_data["latest_message"]["intent_ranking"]
                for intent in intent_ranking:
                    d = dict()
                    d[intent["name"]] = intent["confidence"]
                data.append(d)
        if len(data) > 0:
            keys = data[0].keys()
            with open(output_filepath, 'w') as f:
                dict_writer = csv.DictWriter(output_filepath, keys)
                dict_writer.writeheader()
                dict_writer.writerows(data)

class ExtendedListSlot(DataSlot):
    type_name = "extended_list"

    def __init__(self, name, initial_value=None, value_reset_delay=1):

        super(ExtendedListSlot, self).__init__(name, initial_value, value_reset_delay)

    def __setattr__(self, name, val):
        if name == "value":
            if self.__dict__.get(name) is None:
                self.__dict__[name] = []
            if val is not None:
                self.__dict__[name].append(val)
        else:
            self.__dict__[name] = val

    def as_feature(self):
        try:
            if self.value is not None and len(self.value) > 0:
                return [1.0]
            else:
                return [0.0]
        except (TypeError, ValueError):
            # we couldn't convert the value to a list - using default value
            return [0.0]


