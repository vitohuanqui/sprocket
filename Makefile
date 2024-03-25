SUPPORTED_COMMANDS := test lint format run
SUPPORTS_MAKE_ARGS := $(findstring $(firstword $(MAKECMDGOALS)), $(SUPPORTED_COMMANDS))
ifneq "$(SUPPORTS_MAKE_ARGS)" ""
  COMMAND_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(COMMAND_ARGS):;@:)
endif

help:
	@echo "  build                       build docker image"
	@echo "  test                        run the testsuite"
	@echo "  black                       check the source for style errors"
	@echo "  start                         run the server in localhost"
	@echo "  stop                         stop the server in localhost"

.PHONY: build
build:
	@echo "--> Building image"
	docker-compose -f setup/docker/docker-compose.yml build

.PHONY: test
test:
	@echo "--> Running unittest"
	pytest --verbose --cov=src --cov=tests --cov-report=term-missing --cov-report=xml:.artifacts/coverage.xml --junit-xml=.artifacts/tests.xml

.PHONY: code-black
code-black:
	@echo "--> Format the python code"
	docker exec -it fastapi-app-sprocket-container bash -c "autoflake --remove-all-unused-imports --remove-unused-variables  --recursive --in-place src/ tests/"
	docker exec -it fastapi-app-sprocket-container bash -c "black -S -l 79 src tests"
	docker exec -it fastapi-app-sprocket-container bash -c "isort --recursive --apply src tests"


.PHONY: start
start:
	@echo "--> Running dev server"
	docker network create -d bridge sprocketnetwork | true
	docker-compose -f setup/docker/docker-compose.yml up -d

.PHONY: startlogs
startlogs:
	@echo "--> Running dev server"
	docker network create -d bridge sprocketnetwork | true
	docker-compose -f setup/docker/docker-compose.yml up

.PHONY: stop
stop:
	@echo "--> Stopping dev server"
	docker-compose -f setup/docker/docker-compose.yml stop

.PHONY: logs
logs:
	@echo "--> Running dev server"
	docker-compose -f setup/docker/docker-compose.yml logs -f

.PHONY: ssh-dev
ssh-dev:
	@echo "--> SSH dev server"
	docker-compose -f setup/docker/docker-compose.yml exec app /bin/bash

.PHONY: ssh-db-dev
ssh-db-dev:
	@echo "--> SSH dev server"
	docker-compose -f setup/docker/docker-compose.yml exec database-app-container /bin/bash

.PHONY: my_target
ssh:
	docker-compose -f setup/docker/docker-compose.yml exec $(dst) /bin/bash

.PHONY: tests
tests:
	docker-compose -f setup/docker/docker-compose.yml exec app bash -c "pytest"

.PHONY: seed
seed:
	docker-compose -f setup/docker/docker-compose.yml exec app bash -c "python fill_database.py"

.PHONY: migrate
migrate:
	docker exec -it fastapi-app-sprocket-container bash -c "alembic upgrade head"
