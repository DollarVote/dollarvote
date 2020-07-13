release: python manage.py migrate
web: gunicorn dollarvote.wsgi --workers=3 --log-file -