import os

from rasa_core.tracker_store    import RedisTrackerStore    
from rasa_core.domain import TemplateDomain

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
