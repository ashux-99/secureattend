.PHONY: install test lint run docker-build docker-run clean

install:
	pip install -r requirements.txt

test:
	pytest tests/ -v

lint:
	flake8 .

run:
	python main.py

docker-build:
	docker build -t secureattend .

docker-run:
	docker run -it secureattend

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
