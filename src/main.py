from flask import Flask, request
from flask_cors import CORS
from config.database import connect_to_mongo
from services.student_service import StudentService
from controllers.student_controller import StudentController
from models.student import Student
from dotenv import load_dotenv
import os

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

if __name__ == '__main__':
    app.run(debug=True)