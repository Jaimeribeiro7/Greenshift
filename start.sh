#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn painel_comissoes_igreen_completo.wsgi