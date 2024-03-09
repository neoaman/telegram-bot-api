build:
	virtualenv .venv --prompt . -p python3.11
	.venv/bin/python -m pip install -r requirements.txt

install:
	.venv/bin/python -m pip install -r requirements.txt

run:
	.venv/bin/python -m uvicorn main:app --reload --host 0.0.0.0 --port 18000 --env-file .env