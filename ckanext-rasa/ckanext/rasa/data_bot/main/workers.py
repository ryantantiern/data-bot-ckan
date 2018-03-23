import sys
import time
from rq                                     import Connection, Worker
from redis                                  import StrictRedis
from ckanext.rasa.data_bot.main.main        import REDIS_HOST, PORT, DB, QS
from rasa_core.interpreter                  import RasaNLUInterpreter

redis = StrictRedis(host=REDIS_HOST, port=PORT, db=DB)

def main(qs):
    with Connection(connection=redis):
        Worker(qs).work()

if __name__ == '__main__':
    qs = QS
    main(qs)