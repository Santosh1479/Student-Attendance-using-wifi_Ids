# Student CRUD App

This is a simple CRUD application for managing student records using Flask and MongoDB.

## Routes

### Create Student
- **URL:** `/students/create`
- **Method:** `POST`
- **Description:** Create a new student record.
- **Request Body:**
  ```json
  {
    "id": "string",
    "name": "string",
    "usn": "string",
    "mobile_number": "string",
    "semester": "string",
    "parents_number": "string",
    "branch": "string"
  }
  ```
- **Response:**
  - `201 Created` on success
  - `400 Bad Request` if required fields are missing or validation fails

### Get Student
- **URL:** `/students/<student_id>`
- **Method:** `GET`
- **Description:** Retrieve a student record by ID.
- **Response:**
  - `200 OK` with student data
  - `404 Not Found` if student does not exist

### Update Student
- **URL:** `/students/update/<student_id>`
- **Method:** `PUT`
- **Description:** Update an existing student record by ID.
- **Request Body:**
  ```json
  {
    "name": "string",
    "usn": "string",
    "mobile_number": "string",
    "semester": "string",
    "parents_number": "string",
    "branch": "string"
  }
  ```
- **Response:**
  - `200 OK` on success
  - `400 Bad Request` if validation fails
  - `404 Not Found` if student does not exist

### Delete Student
- **URL:** `/students/delete/<student_id>`
- **Method:** `DELETE`
- **Description:** Delete a student record by ID.
- **Response:**
  - `200 OK` on success
  - `404 Not Found` if student does not exist

### Get All Students
- **URL:** `/students`
- **Method:** `GET`
- **Description:** Retrieve all student records.
- **Response:**
  - `200 OK` with list of students

### Receive Student ID
- **URL:** `/<branch>/<semester>/id`
- **Method:** `POST`
- **Description:** Receive a student ID and record the USN in an Excel sheet.
- **Request Body:**
  ```json
  {
    "student_id": "string"
  }
  ```
- **Response:**
  - `200 OK` if student ID is received and USN is recorded successfully
  - `400 Bad Request` if student ID is missing
  - `404 Not Found` if student or USN does not exist

## Process

1. **Setup:**
   - Clone the repository.
   - Install the required dependencies using `pip install -r requirements.txt`.
   - Create a `.env` file with the following variables:
     ```
     MONGO_URI=<your_mongo_uri>
     DB_NAME=<your_db_name>
     ```

2. **Run the Application:**
   - Start the Flask application using `python src/main.py`.

3. **Hardware Integration:**
   - The `Hardware.cpp` file contains code for an ESP8266 module to send student IDs to the server.
   - Configure the network credentials and server URL in the `Hardware.cpp` file.
   - Upload the code to the ESP8266 module.

4. **Usage:**
   - Use the provided routes to create, read, update, and delete student records.
   - The hardware module will send student IDs to the server, which will record the USN in an Excel sheet.

