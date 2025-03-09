class StudentService:
    def __init__(self, db):
        self.db = db
        self.collection = db['students']

    def create_student(self, student_data):
        # Check for unique id
        if self.collection.find_one({"_id": student_data["_id"]}):
            return {"error": "Student ID must be unique"}, 400

        # Check for unique usn
        if self.collection.find_one({"usn": student_data["usn"]}):
            return {"error": "USN must be unique"}, 400

        # Check that mobile_number and parents_number are not the same
        if student_data["mobile_number"] == student_data["parents_number"]:
            return {"error": "Mobile number and parents number cannot be the same"}, 400

        result = self.collection.insert_one(student_data)
        return str(result.inserted_id), 201

    def get_student(self, student_id):
        student = self.collection.find_one({"_id": student_id})
        return student

    def update_student(self, student_id, updated_data):
        # Check that mobile_number and parents_number are not the same
        if "mobile_number" in updated_data and "parents_number" in updated_data:
            if updated_data["mobile_number"] == updated_data["parents_number"]:
                return {"error": "Mobile number and parents number cannot be the same"}, 400

        result = self.collection.update_one({"_id": student_id}, {"$set": updated_data})
        return result.modified_count

    def delete_student(self, student_id):
        result = self.collection.delete_one({"_id": student_id})
        return result.deleted_count

    def get_all_students(self):
        students = list(self.collection.find())
        return students