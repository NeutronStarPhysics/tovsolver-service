import json
from flask import Flask, request, jsonify
from proxy import proxy_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(proxy_blueprint)

    return app

if __name__ == "__main__":
    create_app().run(debug=True)