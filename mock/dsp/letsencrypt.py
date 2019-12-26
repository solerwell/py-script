# encoding:utf-8
import flask
from flask import request

app = flask.Flask(__name__)


@app.route('/.well-known/acme-challenge/6SO82AzhtpmQRakqb1vk0gdinR-ayTbtD2qYd2T2_2k', methods=['GET'])
def mock():
    print("========== Activate let's encrypt ssl =============")
    print("========== the req param is", request.args, " =============")
    result = "6SO82AzhtpmQRakqb1vk0gdinR-ayTbtD2qYd2T2_2k.gGJ_JESggg1UIJqupOQocl8oGLmlEC52eprY90JmyQ0"
    return result
