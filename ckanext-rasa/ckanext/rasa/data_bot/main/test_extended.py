 #!/usr/lib/ckan/default/bin python -W ignore::DeprecationWarning
from unittest import TestCase, main, skipIf
from mock import Mock, patch
from ckanext.rasa.data_bot.main.extended import ExtendedRedisTrackerStore, ExtendedAgent, StatisticalMessageProcessor, Statistics, ExtendedListSlot
class TestExtendedClasses(TestCase):

    def test_ExtendedRedisTrackerStoreHasTimeout(self):
        # Check ExtendedRedisTrackerStore has timeout attribute
        redis_tracker_store = ExtendedRedisTrackerStore(None, mock=True, timeout=10)
        self.assertEqual(redis_tracker_store.timeout, 10)

    @patch("rasa_core.agent.Agent._create_domain")
    def test_ExtendedAgent__create_processort(self, mock_domain):
        # _create_processor should return StatisticalMessageProcessor
        my_agent = ExtendedAgent("domain.yml")
        self.assertIn("_create_processor", dir(my_agent))

    def test_StatisticalMessageProcessor_handle_message(self):
        # Check StatisticalMsesageProcessor implements handle message
        self.assertIn("handle_message", dir(StatisticalMessageProcessor))
    
    def test_StatisticalMessageProcessor_implements_set_and_execute_next_action(self):      
        self.assertIn("_set_and_execute_next_action", dir(StatisticalMessageProcessor))
    
    @patch("rasa_core.channels.channel.UserMessage") 
    @patch("ckanext.rasa.data_bot.main.extended.StatisticalMessageProcessor._run_action")
    @patch("ckanext.rasa.data_bot.main.extended.StatisticalMessageProcessor._log_slots")
    @patch("rasa_core.domain.Domain")
    @patch("ckanext.rasa.data_bot.main.extended.StatisticalMessageProcessor.__init__")
    def test_StatisticalMessageProcessor_set_and_execute_next_action(self, mock_init, mock_domain, mock_logslot, mock_runaction, mock_UserMessage):
        mock_init.return_value = None
        my_smp = StatisticalMessageProcessor()
        my_smp.domain = mock_domain
        my_smp._set_and_execute_next_action("action_test", mock_UserMessage, "tracker_test")
        my_smp._log_slots.assert_called_with("tracker_test")
        self.assertEqual(len(my_smp._run_action.mock_calls), 2)

    def test_Statistics_log_state(self):
        self.assertIn("log_state", dir(Statistics))

    @patch("ckanext.rasa.data_bot.main.extended.ExtendedListSlot.__init__")
    def test_ExtendedListSlot_as_feature(self, mock_init):
        mock_init.return_value = None
        els = ExtendedListSlot()
        els.value = 1
        value = els.as_feature()
        self.assertEqual(value, [1.0])
    
    @patch("ckanext.rasa.data_bot.main.extended.ExtendedListSlot.__init__")
    def test_ExtendedListSlot_setValue(self, mock_init):
        mock_init.return_value = None
        els = ExtendedListSlot()
        els.value = 1
        els.value = 2
        self.assertEqual(els.value, [1,2])


    @patch("ckanext.rasa.data_bot.main.extended.ExtendedListSlot.__init__")
    def test_ExtendedListSlot_reset(self, mock_init):
        mock_init.return_value = None
        els = ExtendedListSlot()
        els.value = 1
        els.value = 2
        els.reset()
        self.assertEqual(els.value, [])
if __name__ == "__main__":
    main()
    