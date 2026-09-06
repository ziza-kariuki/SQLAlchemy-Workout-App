# SQLAlchemy-Workout-App
A backend API for a workout tracking application used by personal trainers. The API will be responsible for tracking workouts and their associated exercises. Each workout can include multiple exercises, with sets, reps, or duration attached to each. Exercises are reusable, so a trainer can add the same exercise to various workouts.

## Features
### Workout Management
* **Create Workouts:** Add new workout sessions to the system.
* **View Workouts:** Retrieve and inspect existing workout records.
* **Delete Workouts:** Permanently remove workouts from the database.

### Exercise Management
* **Create Exercises:** Add new exercises to the master library.
* **View Exercises:** Browse and view all available exercises.
* **Delete Exercises:** Remove exercises from the system.
* **Reusable Exercises:** Reuse individual exercises across multiple workouts.

## Installation Instructions
1. Clone the repository and navigate into the project directory:
   ```bash
   git clone <git@github.com:ziza-kariuki/SQLAlchemy-Workout-App.git>
   cd SQLAlchemy-Workout-App
   ```
2. Install the project dependencies using Pipenv:
   ```bash
   pipenv install
   ```
3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```
4. Perform database migrations and seed the database:
   ```bash
   flask db upgrade
   python seed.py
   ```

## Run Instructions
To start the backend server, run the following command within the active Pipenv shell:
```bash
flask run
```

## API Endpoint Details

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/workouts` | List all workouts |
| `GET` | `/workouts/<id>` | Show a single workout with its associated exercises |
| `DELETE` | `/workouts/<id>` | Delete a workout |
| `GET` | `/exercises` | Show an exercise and associated workouts |
| `POST` | `/exercises` | Create an exercise |
| `DELETE` | `/exercises/<id>` | Delete an exercise |
| `POST` | `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` | Add an exercise to a workout, including reps/sets/duration |

## Pipfile Dependencies
```toml
[packages]
Flask = "2.2.2"
Flask-Migrate = "3.1.0"
flask-sqlalchemy = "3.0.3"
Werkzeug = "2.2.2"
importlib-metadata = "6.0.0"
importlib-resources = "5.10.0"
ipdb = "0.13.9"
marshmallow = "3.20.1"
```

## Technologies Used
* Language: Python 3.12
