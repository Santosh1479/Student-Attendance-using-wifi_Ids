class Student:
    def __init__(self, id, name, usn, mobile_number, semester, parents_number, branch):
        self.id = id
        self.name = name
        self.usn = usn
        self.mobile_number = mobile_number
        self.semester = semester
        self.parents_number = parents_number
        self.branch = branch

    def to_dict(self):
        return {
            "_id": self.id,
            "name": self.name,
            "usn": self.usn,
            "mobile_number": self.mobile_number,
            "semester": self.semester,
            "parents_number": self.parents_number,
            "branch": self.branch
        }