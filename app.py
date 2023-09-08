from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
todos = [
    {'id': 1, 'title': 'Do the laundry', 'done': False},
    {'id': 2, 'title': 'Walk the dog', 'done': True}
]

# Route to get all todos
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

# Route to get a specific todo by ID
@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify({'todo': todo})

# Route to create a new todo
@app.route('/api/todos', methods=['POST'])
def create_todo():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'The title field is required'}), 400

    new_todo = {
        'id': len(todos) + 1,
        'title': request.json['title'],
        'done': False
    }
    todos.append(new_todo)
    return jsonify({'todo': new_todo}), 201

# Route to update a todo by ID
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404

    if 'title' in request.json:
        todo['title'] = request.json['title']
    if 'done' in request.json:
        todo['done'] = request.json['done']

    return jsonify({'todo': todo})

# Route to delete a todo by ID
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404

    todos.remove(todo)
    return jsonify({'result': 'Todo deleted'})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)