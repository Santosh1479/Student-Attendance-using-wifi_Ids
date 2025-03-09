# Student CRUD Application

This project is a simple Flask application that implements a CRUD (Create, Read, Update, Delete) functionality for managing student records using MongoDB.

## Project Structure

```
student-crud-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── models
│   │   └── student.py         # Defines the Student model
│   ├── controllers
│   │   └── student_controller.py # Handles HTTP requests for student operations
│   ├── services
│   │   └── student_service.py  # Interacts with the database for CRUD operations
│   └── config
│       └── database.py        # Sets up MongoDB connection
├── requirements.txt           # Lists project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd student-crud-app
   ```

2. **Install dependencies:**
   Make sure you have Python and pip installed. Then run:
   ```
   pip install -r requirements.txt
   ```

3. **Set up MongoDB:**
   Ensure you have a MongoDB instance running. You can use a local instance or a cloud service like MongoDB Atlas.

4. **Run the application:**
   Execute the following command to start the Flask application:
   ```
   python src/main.py
   ```

## Usage Examples

- **Create a new student:**
  Send a POST request to `/students` with the student details in JSON format.

- **Get a student by ID:**
  Send a GET request to `/students/<id>`.

- **Update a student:**
  Send a PUT request to `/students/<id>` with the updated details in JSON format.

- **Delete a student:**
  Send a DELETE request to `/students/<id>`.

## License

This project is licensed under the MIT License.