#!/bin/bash

# Zatrzymamy wykonanie skryptu w przypadku jakiegokolwiek błędu
set -e

# Czekamy, aż baza danych użytkowników będzie gotowa
echo "Waiting for the 'users' database to be ready..."
while ! nc -z "$DB2_HOST" "$DB2_PORT"; do
  sleep 0.1
done
echo "'users' database is ready!"

# Czekamy, aż baza danych wtzg będzie gotowa
echo "Waiting for the 'wtzg' database to be ready..."
while ! nc -z "$DB1_HOST" "$DB1_PORT"; do
  sleep 0.1
done
echo "'wtzg' database is ready!"

# Wykonujemy migracje dla bazy danych użytkowników (users)
echo "Running Django migrations for 'users' database..."
python manage.py makemigrations
python manage.py migrate users --database=users

# Wywołanie skryptu init-db.sql dla bazy users
if [ -f /app/init_db/init-db.sql ]; then
  echo "Executing init-db.sql on 'users' database..."
  PGPASSWORD="$DB2_PASSWORD" psql -U "$DB2_USER" -h "$DB2_HOST" -d "$DB2_NAME" -f /app/init_db/init-db.sql
else
  echo "init-db.sql not found, skipping."
fi

# Wykonujemy migracje dla bazy wtzg
echo "Running Django migrations for 'wtzg' database..."
python manage.py migrate

# Wywołanie skryptów SQL dla bazy wtzg
if [ -f /app/init_db/init-app-details.sql ]; then
  echo "Executing init-app-details.sql on 'wtzg' database..."
  PGPASSWORD="$DB1_PASSWORD" psql -U "$DB1_USER" -h "$DB1_HOST" -d "$DB1_NAME" -f /app/init_db/init-app-details.sql
else
  echo "init-app-details.sql not found, skipping."
fi

# Wywołanie skryptów SQL dla bazy wtzg
if [ -f /app/init_db/init-fieldsofstudy.sql ]; then
  echo "Executing init-fieldsofstudy.sql on 'wtzg' database..."
  PGPASSWORD="$DB1_PASSWORD" psql -U "$DB1_USER" -h "$DB1_HOST" -d "$DB1_NAME" -f /app/init_db/init-fieldsofstudy.sql
else
  echo "init-fieldsofstudy.sql not found, skipping."
fi

# Uruchamiamy serwer Django
echo "Starting Django server..."
python manage.py runserver [::]:8000
