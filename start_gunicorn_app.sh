#!/bin/bash

gunicorn --worker-class socketio.sgunicorn.GeventSocketIOWorker server:app --bind 0.0.0.0:8000