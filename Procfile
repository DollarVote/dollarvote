release: python manage.py migrate
web: gunicorn dollarvote.asgi:application -w 3 -k uvicorn.workers.UvicornWorker --log-file -