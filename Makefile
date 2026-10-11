.PHONY: install test run-api clean docker-build

install:
	pip install -r requirements.txt

test:
	pytest tests/

run-api:
	uvicorn src.api:app --reload --host 0.0.0.0 --port 8000

docker-build:
	docker build -t facevoiceid:latest .

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
