#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
export DJANGO_SUPERUSER_USERNAME=root
export DJANGO_SUPERUSER_EMAIL=root@root.pl
export DJANGO_SUPERUSER_PASSWORD=root
python manage.py createsuperuser --noinput
echo "from projects.models import Client; Client(name='testowy klient').save()" | python manage.py shell
echo  "initialize done"

exec "$@"
