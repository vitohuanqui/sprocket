# Sprocket
RESTfull api that services requests for sprocket factory data and sprockets.
FastAPI based website

# Install

## What do you need before start?

- Install Docker https://docs.docker.com/engine/install/
- Install docker-compose https://docs.docker.com/compose/install/

### Download and install on MAC

https://docs.docker.com/docker-for-mac/install/

## Docker


```bash
cd project;
# Config local domain
# Copy .env or ask the nearest team member and the .env file
cp .env.example .env
# Build docker image
make build;
# define some env variables need to run make ssh-dev and
# run docker compose under /setup/docker/
make start;
# log into the container
make ssh-dev;
```


## Database
With the Makefile and Docker configuration, the database setup is automatic; you just need to run 
```bashx
make build
```
Its a PostgreSQL database.
If you wish to create records in the database with the seed, run.

```bashx
make seed
```
## Run FastAPI Server

The application runs on port 8000
go to http://localhost:8000/docs to see the available endpoints.
```bash
make start;
###---------------------------------###
# you can log into the container with
make ssh-dev
```
the endpoint http://localhost:8000/sprocket-data-factory you can pass query params
http://localhost:8000/sprocket-data-factory?end_date=YYYY-MM-DD&start_date=YYYY-MM-DD&factory={factory_id}&sprocket_type={sprocket_type_id}&group_by={year|month|day|hour}

# Run tests

You can run the tests using the following commands:

```bash
make start
make tests
```

# Reformat your code

We use `black`. There is a `invoke` task to help you with that.

```bash
# Reformat your unstaged changes.
make black
```

