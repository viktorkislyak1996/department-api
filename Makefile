.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit install

.PHONY: migrations
migrations:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: server
server:
	poetry run python manage.py runserver

.PHONY: test
test:
	poetry run python manage.py test

.PHONY: update
	update: migrate install-pre-commit ;

.PHONY: app
app:
	docker-compose up -d
	make migrate
	make install-pre-commit
