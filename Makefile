# SHELL := /bin/bash

# help:
#	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

install:
	pipenv install

activate:
	pipenv shell

run:
	python3 manage.py runserver

user:
	python3 manage.py createsuperuser

migration:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

flush:
	python3 manage.py flush

push:
	git push
	
static:
	python3 manage.py collecstatic

superuser:
	python3 manage.py createsuperuser

heroku:
	git push heroku master

deploy:
	docker-compose build
	docker-compose up -d

down:
	docker-compose down
