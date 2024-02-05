import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Src-World!"

jobs = [
    {
     "jobName": "job 1",
    },
    {
     "jobName": "job 2", 
    }
]

@app.route("/jobs", methods = ['GET'])
def get_jobs():
    return jsonify(jobs)

@app.route("/jobs", methods = ['POST'])
def add_job():
    request_data = request.get_json()

    job_name = request_data['jobName']

    jobs.append({
     "jobName": job_name, 
    })
    return '', 201


if __name__ == "__main__":
    app.run()