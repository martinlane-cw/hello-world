from flask import Flask,jsonify,render_template
from flask import request
from flask import abort

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/')
def index():
    print("debug")
    a = 5
    name = "test"
    a = a + 5
    name = "deneme"
    print(name)

    print("deneme")
    return 'Hello World'

@app.route('/test')
def test():
    return 'Hello World'

@app.route('/html')
def html():
    return render_template('home.html')

@app.route('/users/<user_id>')
def parameter(user_id):
    return user_id

@app.route('/users/<user_id>', methods = ['GET','POST','PUT','DELETE'])
def user(user_id):
    if request.method == 'GET':
        """return the information for <user_id>"""
        return "success"

    if request.method == 'POST':
        data = request.form # a multidict containing POST data
        return data
    if request.method == 'PUT':
        data = request.form  # a multidict containing POST data
        return data
    if request.method == 'DELETE':
        """delete user with ID <user_id>"""
        return "success"
    else:
        # POST Error 405 Method Not Allowed
        return "error"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})



app.run(host='0.0.0.0', port=81)

