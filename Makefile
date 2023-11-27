install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval src/*.ipynb
	python -m pytest -vv --cov=src.lib

format:	
	black src/*.py
	nbqa black src/*.ipynb 

lint:
	nbqa ruff src/*.ipynb
	ruff check src/*.py

deploy:
	#deploy goes here
		
all: install lint deploy test format
