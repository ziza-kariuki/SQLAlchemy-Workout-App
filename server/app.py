from flask import Flask, request, jsonify
from flask_migrate import Migrate
from config import app, db
from marshmallow import ValidationError

from models import Workout, Exercise, WorkoutExercise
from schemas import WorkoutSchema, ExerciseSchema, WorkoutExerciseSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

#Schema Objects
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()

# Define Routes here
#Workout Routes
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts)), 200
 
 
@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return jsonify({'error': 'Workout not found'}), 404
    return jsonify(workout_schema.dump(workout)), 200
 
@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json() or {}
    try:
        validated_data = workout_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_workout = Workout(**validated_data)
    db.session.add(new_workout)
    db.session.commit()
    return jsonify(workout_schema.dump(new_workout)), 201
 
 
@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return jsonify({'error': 'Workout not found'}), 404
    db.session.delete(workout)
    db.session.commit()
    return '', 204

#Exercise Routes
 
@app.route('/exercises', methods=['GET'])
def get_exercises():
    return {'message': 'not yet implemented'}, 501
 
 
@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    return {'message': 'not yet implemented'}, 501
 
 
@app.route('/exercises', methods=['POST'])
def create_exercise():
    return {'message': 'not yet implemented'}, 501
 
 
@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    return {'message': 'not yet implemented'}, 501
 
 
@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    return {'message': 'not yet implemented'}, 501
 

if __name__ == '__main__':
    app.run(port=5555, debug=True)