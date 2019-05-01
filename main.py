from datetime import datetime
from flask import Flask, make_response
from job import JobManager
from pi_controller import PiController
import atexit

app = Flask(__name__)
pi = PiController()
job = JobManager(pi)

@app.route('/angry/')
def root():
    result = job.run()
    if result:
        return make_response(f'処理を受け付けました\n'), 202
    else:
        return make_response(f'実行中です\n'), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

def exit_handler():
    # @TODO The cleaning up is not working...
    print('See you...')
    global pi
    pi.cleanup()

atexit.register(exit_handler)

