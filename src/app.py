import json
from flask import Flask, request, jsonify
from proxy import proxy_blueprint

app_name = "TOV Solver - Service"
app = Flask(__name__)

app.register_blueprint(proxy_blueprint)

if __name__ == "__main__":
    app.run(debug=True)