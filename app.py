# -*- coding: utf-8 -*-
import re, time, subprocess, sys
from flask import Flask, render_template, jsonify, abort, make_response, request
from conf import IR_CMD, ir_code


def send_ir_code(code):
    subprocess.call([IR_CMD, "-t", code])


api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False # jsonifyでの日本語文字化け対策


# 簡単なクライアントを起動する
@api.route('/')
def index():
    return render_template("index.html")



# API
@api.route('/ir-remote/api/v1/<string:obj>/<string:cmd>', methods=['POST'])
def ir_remote_api_v1(obj, cmd):
    if request.headers['Content-Type'] != 'application/json':
        return(flask.jsonify(res='error'), 400)
    for object in ir_code:
        if object['name'] == obj.upper():
            for command in object['codes']:
                if command['name'] == cmd.upper():
                    print(command['code'])
                    send_ir_code(command['code'])
                    break
    print(obj.upper())
    print(cmd.upper())
    return jsonify(res='ok')

@api.route('/ir-remote/api/v1/command-list', methods=['GET'])
def ir_remote_api_v1_command_list():
    if request.headers['Content-Type'] != 'application/json':
        return(flask.jsonify(res='error'), 400)
    return jsonify(ir_code=ir_code)



# エントリーポイント
if __name__ == "__main__":
    api.run(host='0.0.0.0',port=3000)


