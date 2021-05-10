from flask import Flask, request, abort
from datetime import datetime
import time

app = Flask(__name__)
db = [
    {
        'name': 'Name',
        'text': 'Test message',
        'time': 0.1
    },
    {
        'name': 'Name',
        'text': 'Test message',
        'time': 0.2
    },
]


@app.route("/")
@app.route("/status")
def status():
    data = {
        'status': True,
        'name': 'Messenger',
        'time': datetime.now().strftime('%y/%m/%d %H:%M'),
        'count_messages': len(db),
        'count_users': len(set(msg['name'] for msg in db))
    }
    return data


@app.route("/send", methods=['POST'])
def send():
    data = request.json
    if not isinstance(data, dict):
        return abort(400)
    if 'name' not in data or 'text' not in data:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if not 0 < len(name) <= 64:
        return abort(400)
    if not 0 < len(text) <= 10000:
        return abort(400)

    db.append({
        'name': name,
        'text': text,
        'time': time.time()
    })
    if text == '/stat':
        db.append({
            'name': 'Bot',
            'text': f'Unique users: {status()["count_users"]}\nMessages: {status()["count_messages"]}',
            'time': time.time()
        })
    return {}


@app.route("/messages")
def messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    filtered_messages = []
    for message in db:
        if message['time'] > after:
            filtered_messages.append(message)
    return {'messages': filtered_messages[:50]}


app.run()
