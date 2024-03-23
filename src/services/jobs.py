from flask import Blueprint, request, jsonify


jobs_blueprint = Blueprint('jobs', __name__,)

jobs = [
    {
     "jobName": "job 1",
    },
    {
     "jobName": "job 2", 
    }
]

@jobs_blueprint.route("/jobs", methods = ['GET'])
def get_jobs():
    return jsonify(jobs)

@jobs_blueprint.route("/jobs", methods = ['POST'])
def add_job():
    request_data = request.get_json()

    job_name = request_data['jobName']

    jobs.append({
     "jobName": job_name, 
    })
    return '', 201
