release: python manage.py migrate
web: gunicorn b13.wsgi
release: python manage.py collectstatic --noinput
web: python b13.py

