#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER user_department;
	CREATE DATABASE department;
	GRANT ALL PRIVILEGES ON DATABASE department TO user_department;
EOSQL