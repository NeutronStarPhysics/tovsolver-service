from flask import Blueprint, request, jsonify
from adapters.proxyrequest import ProxyRequest

from task_manager import TaskManager

proxy_blueprint = Blueprint('proxy', __name__,)

@proxy_blueprint.route('/')
def hello():
    return "Proxy.py!"

def parse_request(request) -> ProxyRequest:
    proxy_request = ProxyRequest()

    try:
        request_data = request.get_json()

        proxy_request.name = request_data["name"]
        proxy_request.type = request_data["type"]
        proxy_request.payload = request_data["payload"]

    except Exception as e:
        print("Exception parsing request: {}".format(str(e)))

    return proxy_request


@proxy_blueprint.route("/invoke", methods = ['POST'])
def invoke():
    print("REQUEST:" + str(request.get_data()))
    proxy_request = parse_request(request)

    print("Calling '{}'".format(proxy_request.type))
    task_manager = TaskManager(proxy_request.type, proxy_request.payload)

    response = task_manager.invoke()

    return response, 201
