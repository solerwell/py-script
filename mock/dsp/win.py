# encoding:utf-8
import flask
from flask import jsonify, request

app = flask.Flask(__name__)


@app.route('/win', methods=['GET'])
def dsp1():
    print("========== RECEIVED WIN NOTICE =============")
    print("========== the req param is", request.args, " =============")
    resp = {"result": "win notice receive!"}
    return jsonify(resp)

