#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd dollarvote; python manage.py createsuperuser --no-input)
fi
(cd /opt/app/dollarvote/; gunicorn dollarvote.wsgi --user www-data --bind 127.0.0.1:8000 --workers 3) &
nginx -g "daemon off;"