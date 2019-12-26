# encoding:utf-8
import flask
from flask import request

app = flask.Flask(__name__)


@app.route('/.well-known/acme-challenge/6hWWNiqvB4WkjQpQfB_5cfvO0WCXaPvswhDc-8gQJZk', methods=['GET'])
def mock():
    print("========== Activate let's encrypt ssl =============")
    print("========== the req param is", request.args, " =============")
    result = "6hWWNiqvB4WkjQpQfB_5cfvO0WCXaPvswhDc-8gQJZk.gGJ_JESggg1UIJqupOQocl8oGLmlEC52eprY90JmyQ0"
    return result
