from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
        data = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!' # return 'Hello World' in response
    
#task3    
@app.route('/students')
def get_students():
        return jsonify(data)# return student data in response

 #task4
    # route variables
@app.route('/students/<id>')
def get_student(id):
      for student in data: 
        if student['id'] == id: # filter out the students without the specified id
          return jsonify(student)
#task5
@app.route('/students')
def get_students():
 result = []
pref = request.args.get('pref') # get the parameter from url
if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
        return jsonify(result) # return filtered set if parameter is supplied
     return jsonify(data) # return entire dataset if no parameter supplied
   
    
#Exercise 1
# Define all possible keys
possible_meals = ["Chicken", "Fish", "Vegetable"]
possible_programs = [
    "Computer Science (Major)",
    "Computer Science (Special)",
    "Information Technology (Major)",
    "Information Technology (Special)"
]

@app.route('/stats', methods=['GET'])
def get_stats():
    # Initialize counts for all possibilities
    stats = {key: 0 for key in possible_meals + possible_programs}

    # Calculate counts
    for entry in data:
        meal = entry.get('pref', '')
        program = entry.get('programme', '')

        if meal in stats:
            stats[meal] += 1  # Increment meal count
        if program in stats:
            stats[program] += 1  # Increment program count

    return jsonify(stats)  # Return stats as JSON

#Exercise 2

@app.route('/add/<int:a>/<int:b>', methods=['GET'])
def add(a, b):
    result = a + b
    return jsonify({"operation": "addition", "a": a, "b": b, "result": result})

@app.route('/subtract/<int:a>/<int:b>', methods=['GET'])
def subtract(a, b):
    result = a - b
    return jsonify({"operation": "subtraction", "a": a, "b": b, "result": result})

@app.route('/multiply/<int:a>/<int:b>', methods=['GET'])
def multiply(a, b):
    result = a * b
    return jsonify({"operation": "multiplication", "a": a, "b": b, "result": result})

@app.route('/divide/<int:a>/<int:b>', methods=['GET'])
def divide(a, b):
    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    result = a / b
    return jsonify({"operation": "division", "a": a, "b": b, "result": result})



app.run(host='0.0.0.0', port=8080)