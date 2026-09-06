# server/schemas.py
from marshmallow import Schema, fields


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str()
    equipment_needed = fields.Bool()
    workout_exercises = fields.List(
        fields.Nested('WorkoutExerciseSchema', exclude=('exercise',)), dump_only=True
    )


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int()
    notes = fields.Str()
    workout_exercises = fields.List(
        fields.Nested('WorkoutExerciseSchema', exclude=('workout',)), dump_only=True
    )


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()
    workout_id = fields.Int(load_only=True)
    exercise_id = fields.Int(load_only=True)
    exercise = fields.Nested('ExerciseSchema', exclude=('workout_exercises',), dump_only=True)
    workout = fields.Nested('WorkoutSchema', exclude=('workout_exercises',), dump_only=True)