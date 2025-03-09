from flask import Flask, request
from flask_cors import CORS
from config.database import connect_to_mongo
from services.student_service import StudentService
from controllers.student_controller import StudentController
from models.student import Student
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MongoDB configuration
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
db = connect_to_mongo(MONGO_URI, DB_NAME)

# Initialize services and controllers
student_service = StudentService(db)
student_controller = StudentController(student_service)

@app.route('/students/create', methods=['POST'])
def create_student():
    data = request.json
    student = Student(**data)
    return student_controller.create_student(student.to_dict())

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    return student_controller.get_student(student_id)

@app.route('/students/update/<student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    return student_controller.update_student(student_id, data)

@app.route('/students/delete/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    return student_controller.delete_student(student_id)

@app.route('/students', methods=['GET'])
def get_all_students():
    return student_controller.get_all_students()

@app.route('/<branch>/<semester>/id', methods=['POST'])
def receive_student_id(branch, semester):
    data = request.json
    student_id = data.get('student_id')
    if not student_id:
        return {"error": "Student ID is required"}, 400

    student = student_controller.get_student(student_id)
    if student[1] == 200:  # Check if student exists
        usn = student[0].get('usn')
        if usn:
            # Create or update the Excel sheet
            filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".xlsx"
            if os.path.exists(filename):
                df = pd.read_excel(filename)
                df = df.append({"USN": usn}, ignore_index=True)
            else:
                df = pd.DataFrame([{"USN": usn}])
            df.to_excel(filename, index=False)
            return {"message": "Student ID received and USN recorded successfully"}, 200
        else:
            return {"error": "USN not found for the student"}, 404
    else:
        return {"error": "Student not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)