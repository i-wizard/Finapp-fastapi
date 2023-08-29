ifeq ($(RUNTIME_ENV), production)
	COMPOSE = sudo docker-compose -f docker-compose.yml
else:
	COMPOSE = sudo docker-compose -f docker-compose.dev.yml
endif

SERVICE = app

up:
	$(COMPOSE) up

up-d:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

makemigrations:
	$(COMPOSE) run $(SERVICE) alembic revision --autogenerate -m $(NAME)

migrate:
	$(COMPOSE) run $(SERVICE) alembic upgrade head