#!/bin/sh

echo ":: Clearing db"
./manage.py sqlclear meetup | python manage.py dbshell;
echo ":: Syncing db"
./manage.py syncdb
