#!/usr/bin/env bash
# exit on error
set -o errexit

pipenv install --deploy --ignore-pipfile

python manage.py collectstatic --no-input
python manage.py migrate
if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi