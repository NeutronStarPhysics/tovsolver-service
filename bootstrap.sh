#!/bin/sh

export FLASK_APP=./${APP_FOLDER}/app.py

echo "FLASK_APP: ${FLASK_APP}"

pipenv run flask --debug run -h 0.0.0.0