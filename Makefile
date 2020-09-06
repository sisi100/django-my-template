build:
	docker-compose build

docker-up:
	docker-compose up -d

restart:
    docker-compose restart web

log:
	docker-compose logs -f web

createsuperuser:
	docker-compose run --rm web python manage.py createsuperuser

makemigrations:
	docker-compose run --rm web python manage.py makemigrations

migrate:
	docker-compose run --rm web python manage.py migrate

black:
	docker-compose run --rm web black .

isort:
	docker-compose run --rm web isort .
