#!/bin/bash

# sleep 5
clear 

# # get hello world
# echo "get hello world"
# curl http://localhost:5000/

# # get services
# echo "get services"
# curl http://localhost:5000/jobs

# # add new job
# echo "add new job"
# uuid=$(dbus-uuidgen)
# curl -X POST -H "Content-Type: application/json" -d '{ "jobName": "'"$uuid"'" }' http://localhost:5000/jobs

# # check if job was added
# echo "check if job was added"
# curl http://localhost:5000/jobs


# proxy request
echo "proxy request - eos_merge"
uuid=$(dbus-uuidgen)
payload='{ "name": "'"$uuid"'", "type": "eos_merge" }'
curl -X POST -H "Content-Type: application/json" -d "$payload" http://localhost:5000/invoke

echo "proxy request - eos_generator"
uuid=$(dbus-uuidgen)
payload='{ "name": "'"$uuid"'", "type": "eos_generator", "payload": { "type": "mit_bag_model", "rho_0": 100, "bag_constant": 5 } }'
curl -X POST -H "Content-Type: application/json" -d "$payload" http://localhost:5000/invoke

