#!/bin/bash

# sleep 5

# get hello world
curl http://localhost:5000/

# get services
curl http://localhost:5000/jobs

# add new job
uuid=$(dbus-uuidgen)
curl -X POST -H "Content-Type: application/json" -d '{
  "jobName": "${uuid}"
}' http://localhost:5000/jobs

# check if job was added
curl http://localhost:5000/jobs
