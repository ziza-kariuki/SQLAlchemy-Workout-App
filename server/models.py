from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
db = SQLAlchemy()

# Define Models here
# Exercise model
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean)

    #An Exercise has many WorkoutExercises
    workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise')
    
    #An Exercise has many Workouts through WorkoutExercises
    workouts = association_proxy('workout_exercises', 'workout')

    #Validating that the name isn't left empty
    @validates('name')
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Exercise name cannot be empty.")
        return value

    def __repr__(self):
        return f'<Exercise {self.id}: {self.name}>'

#Workout model
class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)

    #A Workout has many WorkoutExercises
    workout_exercises = db.relationship('WorkoutExercise', back_populates='workout')

    #A Workout has many Exercises through WorkoutExercises
    exercises = association_proxy('workout_exercises', 'exercise')

    #Validating that time given isn't negative
    @validates('duration_minutes')
    def validate_duration_minutes(self, key, value):
            if value is not None and value <= 0:
                raise ValueError("Workout duration must be a positive number.")
            return value
    
    def __repr__(self):
        return f'<Workout {self.id}: {self.date}>'


#Workout_exercise model
class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    #Table constraints
    __table_args__ = (
        db.CheckConstraint('reps >= 0', name='reps_non_negative'),
        db.CheckConstraint('sets >= 0', name='sets_non_negative'),
        db.CheckConstraint('duration_seconds >= 0', name='duration_seconds_non_negative'),
    )

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_minutes = db.Column(db.Integer)

    #A WorkoutExercise belongs to a Workout
    workout = db.relationship('Workout', back_populates='workout_exercises')

    #A WorkoutExercise belongs to an Exercise
    exercise = db.relationship('Exercise', back_populates='workout_exercises')

    def __repr__(self):
        return f'<WorkoutExercise {self.id}>'