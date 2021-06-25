#!/bin/bash
set -e

cd /root/app/basiccrm
git pull
source /root/app/basiccrm/venv/bin/activate
pip install -r requirements.txt
./manage.py collectstatic --noinput
./manage.py migrate
supervisorctl restart basiccrm
