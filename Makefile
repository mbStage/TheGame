install:
	python -m pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=caesar_CLI.py --cov=lib 

format:	
	black *.py 

lint:
	pylint --disable=R,C,W0621 --ignore-patterns=test_.*?py *.py ./lib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy