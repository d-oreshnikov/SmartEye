.PHONY: build run clean purge lint lint-fix lint-mypy lint-black lint-isort lint-docformatter

DB_CONTAINER=postgres-container

run:
	docker compose up -d

clean_db:
	-docker stop $(DB_CONTAINER)
	-docker rm $(DB_CONTAINER)

purge:
	-docker stop $$(docker ps -aq)
	-docker rm $$(docker ps -aq)
	-docker volume rm $$(docker volume ls -q)
	-docker rmi $$(docker images -q)

lint-mypy:
	mypy 

lint-black:
	black --check .

lint-isort:
	isort -c .

lint-docformatter:
	docformatter -c -r . || (docformatter -r .; return -1)

lint: lint-mypy lint-black lint-isort lint-docformatter

lint-fix:
	black .
	docformatter -i -r .
	isort .
	find . -name '*.py' | xargs autoflake --in-place --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports --remove-duplicate-keys
