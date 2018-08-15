#!/bin/bash

deactivate

source venv/bin/activate

export FLASK_RUN_PORT=1469
export FLASK_APP=app.py

#python app.py
flask run

deactivate
