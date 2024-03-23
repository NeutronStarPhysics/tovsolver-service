import json
from flask import Flask, request, jsonify
from proxy import proxy_blueprint
from services.jobs import jobs_blueprint

app = Flask(__name__)

app.register_blueprint(proxy_blueprint)
app.register_blueprint(jobs_blueprint)

if __name__ == "__main__":
    app.run(debug=True)