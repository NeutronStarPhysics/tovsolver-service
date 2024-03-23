from flask import Blueprint, request, jsonify
from adapters.proxyrequest import ProxyRequest

proxy_blueprint = Blueprint('proxy', __name__,)

@proxy_blueprint.route('/')
def hello():
    return "Hello Src-World from proxy.py!"

def parse_request(request) -> ProxyRequest:
    request_data = request.get_json()
    print("request_data:" + str(request_data))

    proxy_request = ProxyRequest()
    proxy_request.name = request_data["name"]
    proxy_request.type = request_data["type"]
    proxy_request.payload = request_data

    return proxy_request


def __eos_merge(payload):
    print("Entering '__eos_merge'")

    return  0

choice_table = {
    "eos_merge": __eos_merge,
}


@proxy_blueprint.route("/invoke", methods = ['POST'])
def invoke():
    proxy_request = parse_request(request)

    print("Calling '{}'".format(proxy_request.type))
    error = choice_table[proxy_request.type](proxy_request.payload)


    return '', 201
