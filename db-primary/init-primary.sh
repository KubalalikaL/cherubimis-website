#!/bin/sh

set -e

echo "Initializing primary Database..."

mysql -u root -p"${MYSQL_ROOT_PASSWORD}" <<-EOSQL
  -- Create microservice databases:
  CREATE DATABASE IF NOT EXISTS ${MYSQL_DATABASE};

  -- Create microservice users & grant privileges:
  CREATE USER IF NOT EXISTS '${MYSQL_USER}'@'%' IDENTIFIED BY '${MYSQL_PASSWORD}';
  GRANT ALL PRIVILEGES ON ${MYSQL_DATABASE}.* TO '${MYSQL_USER}'@'%';

  FLUSH PRIVILEGES;
EOSQL

echo "Primary MySQL initialization complete."
