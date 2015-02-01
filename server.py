import flask
from flask import request
import simplejson

app = flask.Flask(__name__)

tests = [1,2,3,4,5,6,7,8,9]
active_tasks = []
nodes = {}

@app.route('/')
def index():
    return "aaa"

@app.route('/get_tests')
def get_tests(a=1):
    print a
    tasks = list(set(tests) - set(active_tasks))[:4]
    
    active_tasks.extend(tasks)
    nodes[request.environ.get('REMOTE_ADDR')] = {
        'tests': tasks
    }
    print nodes
    return simplejson.dumps(tasks)

@app.route('/submit_results', methods=["POST"])
def submit_results():
    print request.
    return ""

app.run(host="0.0.0.0")
