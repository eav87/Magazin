#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
chmod 0666 db.sqlite3
service mydjango restart
