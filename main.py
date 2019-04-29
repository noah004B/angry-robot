from datetime import datetime
from flask import Flask, make_response
from robot import Robot

app = Flask(__name__)
robot = Robot()

@app.route('/angry/')
def root():
    if robot.angry():
        return make_response(f'処理を受け付けました\n'), 202
    else:
        return make_response(f'実行中です\n'), 200

@app.route('/calm/')
def stop():
    if robot.calm():
        return make_response(f'中止処理を受け付けました\n'), 202
    else:
        return make_response(f'実行していません\n'), 200

@app.route('/status/')
def status():
    if robot.is_alive():
        return make_response(f'実行中です\n'), 200
    else:
        return make_response(f'実行していません\n'), 200

