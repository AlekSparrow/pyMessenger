from datetime import datetime
import time
import requests


def print_message(msg):
    dt = datetime.fromtimestamp(msg['time'])
    print(dt.strftime('%H:%M:%S'), msg['name'])
    print(msg['text'])
    print()


after = 0
while True:
    response = requests.get(
        'http://127.0.0.1:5000/messages',
        params={'after': after}
    )
    messages = response.json()['messages']
    if messages:
        for message in messages:
            print_message(message)
        after = messages[-1]['time']
    time.sleep(1)
