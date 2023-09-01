#!/usr/bin/env sh
cd /app/
pip install -r requirements.txt
python manage.py migrate
gunicorn --conf /app/gunicorn.py --bind 0.0.0.0:8000 --reload --reload-engine=poll  Magazin.wsgi
#python manage.py runserver 0.0.0.0:8000