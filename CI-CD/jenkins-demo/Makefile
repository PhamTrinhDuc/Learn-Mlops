# Makefile

.PHONY: install test build run lint clean

install:
	pip install --upgrade pip
	pip install -r requirements.txt && pytest

test:
	pytest tests/

lint:
	flake8 app/ tests/

build:
	docker build -t duc8504/jenskins-demo:latest .

run:
	docker run --rm -p 8000:8000 duc8504/jenskins-demo:latest

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
