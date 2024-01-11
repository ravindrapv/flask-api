# My Flask Employee API

This is a simple Flask API for managing employee records.

## Endpoints

1. **Get All Employees**
   - **Endpoint:** `/api/employees`
   - **Method:** `GET`
   - **Description:** Retrieves a list of all employees.

2. **Get Employee by ID**
   - **Endpoint:** `/api/employees/<string:employee_id>`
   - **Method:** `GET`
   - **Description:** Retrieves a specific employee by their ID.

3. **Create Employee**
   - **Endpoint:** `/api/employees`
   - **Method:** `POST`
   - **Description:** Creates a new employee.

4. **Update Employee**
   - **Endpoint:** `/api/employees/<string:employee_id>`
   - **Method:** `PUT`
   - **Description:** Updates an existing employee by their ID.

5. **Delete Employee**
   - **Endpoint:** `/api/employees/<string:employee_id>`
   - **Method:** `DELETE`
   - **Description:** Deletes an employee by their ID.

6. **Get Paginated Employees**
   - **Endpoint:** `/api/employees?page=<int:page>&per_page=<int:per_page>`
   - **Method:** `GET`
   - **Description:** Retrieves a paginated list of employees.

## Getting Started

1. Install dependencies:

   ```bash
   pip install -r requirements.txt


2. Dependencies
### Flask
### Flask-RESTful
### Flask-CORS
### Flask-PyMongo
### Marshmallow
### dotenv
