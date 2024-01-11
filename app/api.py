from dotenv import load_dotenv
load_dotenv()
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_pymongo import PyMongo
from app.models.employee import EmployeeSchema
from app.services.employee_service import EmployeeService
import os
app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(app) 

employee_schema = EmployeeSchema()
employee_service = EmployeeService(mongo)

class EmployeeResource(Resource):
    def get(self, employee_id=None):  
        if employee_id:
            employee = employee_service.get_employee_by_id(employee_id)
            if employee:
                return {'employee': employee_schema.dump(employee)}
            else:
                return {'message': 'Employee not found'}, 404
        else:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 10))
            employees = employee_service.get_employees_pagination(page, per_page)
            total_employees = employee_service.get_total_employees_count()
            return {
                'employees': employee_schema.dump(employees, many=True),
                'total_employees': total_employees,
                'current_page': page,
                'per_page': per_page
            }

    def post(self):
        try:
            new_employee = employee_schema.load(request.json)
        except ValidationError as e:
            return {'message': 'Validation error', 'errors': e.messages}, 400

        created_employee = employee_service.create_employee(new_employee)
        return {'message': 'Employee created successfully', 'employee': employee_schema.dump(created_employee)}, 201

    def put(self, employee_id):
        updated_employee_data = request.json
        updated_employee = employee_service.update_employee(employee_id, updated_employee_data)

        return {'message': 'Employee updated successfully', 'employee': employee_schema.dump(updated_employee)}

    def delete(self, employee_id):
        deleted_count = employee_service.delete_employee(employee_id)

        if deleted_count > 0:
            return {'message': 'Employee deleted successfully'}
        else:
            return {'message': 'Employee not found'}, 404

api.add_resource(EmployeeResource, '/api/employees', '/api/employees/<string:employee_id>')

if __name__ == '__main__':
    app.run(debug=True)