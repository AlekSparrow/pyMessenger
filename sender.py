import requests

name = input('Your name: ')

while True:
    data = {
        'name': name,
        'text': input('>>> ')
    }

    response = requests.post('http://127.0.0.1:5000/send', json=data)
