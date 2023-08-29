COMPOSE =  docker-compose -f docker-compose.dev.yml
ifeq ($(RUNTIME_ENV), production)
	COMPOSE = sudo docker-compose -f docker-compose.yml
endif

SERVICE = app

up:
	$(COMPOSE) up

up-d:
	$(COMPOSE) up -d

build:
	$(COMPOSE) build

down:
	$(COMPOSE) down

migrations:
	$(COMPOSE) run $(SERVICE) alembic revision --autogenerate -m "First Migration"

migrate:
	$(COMPOSE) run $(SERVICE) alembic upgrade head