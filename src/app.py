from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    { "label": "My third task", "done": False },
    { "label": "My fourth task", "done": False },
    { "label": "My fifth task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)  # Agrega la nueva tarea a la lista todos
    return jsonify(todos)  # Devuelve la lista actualizada al front end
    
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
     if 0 <= position < len(todos):
        todos.pop(position)  # Elimina la tarea de la lista según la posición
     return jsonify(todos)  # Devuelve la lista actualizada al front end



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)