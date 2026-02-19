from redis_connection import RedisConn 
import json
from priority_logic import get_priority_level
from border_alerts import data ###############



def get_border_alerts_from_file(path='border_alerts.json'):
    with open(path, "r") as f: 
        data = json.loads(f.read())
    return data


def add_priority_field(alerts: list): 
    for alert in alerts: 
        priority = get_priority_level(alert)
        alert["priority"] = priority
    return alerts 


def push_to_queue(alert, queue_type):
    r = RedisConn.get_redis_connection()
    value = json.dumps(alert)
    r.lpush(queue_type, value)


def get_type_by_priority(priority):
    if priority == 'URGENT': 
        return 'urgent_queue'
    else: 
        return 'normal_queue'


def main():
    try:
        # data = get_border_alerts_from_file()
        alerts = add_priority_field(data) 
        for alert in alerts: 
            queue_type = get_type_by_priority(alert["priority"])
            push_to_queue(alert, queue_type)
    except Exception as e: 
        print(str(e))

if __name__ == '__main__':
    main()
