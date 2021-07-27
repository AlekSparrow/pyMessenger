.PHONY: setup \
		server \
		receiver \
		sender \

venv/bin/activate: ## alias for virtual environment
	python3 -m venv venv

setup: venv/bin/activate ## project setup
	. venv/bin/activate; pip install pip wheel setuptools
	. venv/bin/activate; pip install -r requirements.txt

server: venv/bin/activate ## server
	. venv/bin/activate; python3 server.py

receiver: venv/bin/activate ## receiver
	. venv/bin/activate; python3 receiver.py

sender: venv/bin/activate ## sender
	. venv/bin/activate; python3 sender.py
