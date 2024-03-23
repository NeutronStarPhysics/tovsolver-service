from flask import Blueprint

proxy_blueprint = Blueprint('proxy', __name__,)

@proxy_blueprint.route('/')
def hello():
    return "Hello Src-World from proxy.py!"
