#!/bin/bash

# Create PostgreSQL container
docker run --name test-postgres -e POSTGRES_PASSWORD='test' -e POSTGRES_USER=test -d postgres:9.4.5


# Create app container
docker run -it --name test-app --link test-postgres:postgres -p 8000:8000 -v $PWD/app:/home/app -w /home/app -d python:2.7

# Install requirements
docker exec test-app pip install -r requirements.txt

# Make tables and load a superuser for Admin site.
docker exec test-app python manage.py migrate
docker exec test-app python manage.py loaddata superuser.json

# Start python server in background.
# Admin site will be available at http://localhost:8000/admin/
# Login as: admin/admin
docker exec -d test-app python manage.py runserver 0.0.0.0:8000

# Run tests
docker exec test-app python manage.py test
