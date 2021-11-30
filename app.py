from flask import Flask, jsonify
from approvals import approvals
from flask import request, Response
from approvals import add_approval_to_DB
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.debug = True
toolbar = DebugToolbarExtension(app)

app.config['FLASK_ENV'] = 'development'


@app.route('/')
def hello_world():
    return jsonify({
        'greeting': 'Hello World!'
    })


@app.route('/approvals')
def all_approvals():
    return jsonify({
        'approvals': approvals,
    })


@app.route('/approvals/<approval_id>')
def find_approval_by_id(approval_id):
    for approval in approvals:
        if approval["id"] == int(approval_id):
            return jsonify({
                "approval": approval,
            })


@app.route('/approvals/add', methods=['POST'])
def add_approval():
    data = request.get_json()
    try:
        title = data['title']
        project_name = data['project_name']
        value = data['value']
        if title and project_name and value:
            data = add_approval_to_DB(title, project_name, int(value))
            return jsonify(data), 201
    except:
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')
