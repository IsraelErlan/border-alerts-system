from redis_connection import RedisConn 
from mongo_connection import Mongo
from datetime import datetime
import json

def insert_document_to_mongo(document):
    col = Mongo.get_collection()
    col.insert_one(document)

def add_time_field(alert):
    time_insertion = datetime.now()
    alert["time_insertion"] = time_insertion
    return alert


def alert_handler(msg):
    if msg is not None:
        alert = json.loads(msg)
        alert = add_time_field(alert)
        insert_document_to_mongo(alert)


def main():
    r = RedisConn.get_redis_connection()
    while True: 
        msg = r.rpop('urgent_queue')
        # if msg and msg.error(): 
        #     continue
        if msg is not None:
            alert_handler(msg)

        else: 
            msg = r.brpop(['normal_queue'])
            alert_handler(msg)


if __name__ == '__main__': 
    try:
        main()
    except Exception as e:
        print(str(e))


