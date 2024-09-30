# Pull official base image
FROM postgres:16

# Run create.sql on init by adding create.sql to /docker-entrypoint-initdb.d which will run on init
ADD create.sql /docker-entrypoint-initdb.d