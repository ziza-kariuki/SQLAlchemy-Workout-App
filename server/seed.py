#!/usr/bin/env python3

import datetime
from app import app
from models import db, Exercise, Workout, WorkoutExercise

# reset data and add new example data, committing to db 
with app.app_context():
    print("Clearing db...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()
    db.session.commit()

    print("Seeding exercises...")
    squat = Exercise(name="Squat", category="Strength", equipment_needed=True)
    pushup = Exercise(name="Push-up", category="Strength", equipment_needed=False)
    running = Exercise(name="Running", category="Cardio", equipment_needed=False)
    yoga = Exercise(name="Yoga Stretch", category="Flexibility", equipment_needed=False)
    balance = Exercise(name="Single-Leg Balance", category="Balance", equipment_needed=False)
    db.session.add_all([squat, pushup, running, yoga, balance])
    db.session.commit()

    print("Seeding workouts...")
    w1 = Workout(date=datetime.date(2026, 9, 1), duration_minutes=45, notes="Full body strength session")
    w2 = Workout(date=datetime.date(2026, 9, 3), duration_minutes=30, notes="Morning cardio run")
    w3 = Workout(date=datetime.date(2026, 9, 5), duration_minutes=20, notes="Recovery stretch and balance work")
    db.session.add_all([w1, w2, w3])
    db.session.commit()

    print("Linking exercises to workouts...")
    links = [
        WorkoutExercise(workout=w1, exercise=squat, reps=10, sets=4),
        WorkoutExercise(workout=w1, exercise=pushup, reps=15, sets=3),
        WorkoutExercise(workout=w2, exercise=running, duration_seconds=1800),
        WorkoutExercise(workout=w3, exercise=yoga, duration_seconds=600),
        WorkoutExercise(workout=w3, exercise=balance, sets=3, duration_seconds=30),
    ]
    db.session.add_all(links)
    db.session.commit()

    print("Done seeding!")

	