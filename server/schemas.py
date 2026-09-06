# server/schemas.py
from marshmallow import Schema, fields, validate


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True , validate=validate.Length(min=2, error="Name is too short."))
    category = fields.Str()
    equipment_needed = fields.Bool()
    workout_exercises = fields.List(
        fields.Nested('WorkoutExerciseSchema', exclude=('exercise',)), dump_only=True
    )


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(validate=validate.Range(min=1, error="Duration must be at least 1 minute."))
    notes = fields.Str()
    workout_exercises = fields.List(
        fields.Nested('WorkoutExerciseSchema', exclude=('workout',)), dump_only=True
    )


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    reps = fields.Int(validate=validate.Range(min=1, error="Reps must be greater than 0."))
    sets = fields.Int(validate=validate.Range(min=1, error="Sets must be greater than 0."))
    duration_seconds = fields.Int(validate=validate.Range(min=10, error="Duration must be at least 10 seconds."))
    workout_id = fields.Int(load_only=True)
    exercise_id = fields.Int(load_only=True)
    exercise = fields.Nested('ExerciseSchema', exclude=('workout_exercises',), dump_only=True)
    workout = fields.Nested('WorkoutSchema', exclude=('workout_exercises',), dump_only=True)