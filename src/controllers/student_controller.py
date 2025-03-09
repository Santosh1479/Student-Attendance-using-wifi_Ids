from flask import jsonify

class StudentController:
    def __init__(self, student_service):
        self.student_service = student_service

    def create_student(self, student_data):
        required_fields = ["id", "name", "usn", "mobile_number", "semester", "parents_number", "branch"]
        for field in required_fields:
            if field not in student_data:
                return jsonify({"error": f"{field} is required"}), 400

        result, status_code = self.student_service.create_student(student_data)
        return jsonify(result), status_code

    def get_student(self, student_id):
        student = self.student_service.get_student(student_id)
        if student:
            return jsonify(student), 200
        else:
            return jsonify({"error": "Student not found"}), 404

    def update_student(self, student_id, student_data):
        result = self.student_service.update_student(student_id, student_data)
        if isinstance(result, dict) and "error" in result:
            return jsonify(result), 400
        elif result > 0:
            return jsonify({"message": "Student updated successfully"}), 200
        else:
            return jsonify({"error": "Student not found"}), 404

    def delete_student(self, student_id):
        deleted_count = self.student_service.delete_student(student_id)
        if deleted_count > 0:
            return jsonify({"message": "Student deleted successfully"}), 200
        else:
            return jsonify({"error": "Student not found"}), 404

    def get_all_students(self):
        students = self.student_service.get_all_students()
        return jsonify(students), 200