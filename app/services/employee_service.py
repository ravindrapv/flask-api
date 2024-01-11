
from flask_pymongo import PyMongo
from bson import ObjectId

class EmployeeService:
    def __init__(self, mongo):
        self.employees_collection = mongo.db.employees

    def get_employees_pagination(self, page, per_page):
        skip = (page - 1) * per_page
        employees = self.employees_collection.find().skip(skip).limit(per_page)
        return employees

    def get_total_employees_count(self):
        return self.employees_collection.count_documents({})

    def get_employee_by_id(self, employee_id):
        return self.employees_collection.find_one({'_id': ObjectId(employee_id)})

    def create_employee(self, new_employee):
        result = self.employees_collection.insert_one(new_employee)
        new_employee['_id'] = str(result.inserted_id)
        return new_employee

    def update_employee(self, employee_id, updated_employee_data):
        filter_criteria = {'_id': ObjectId(employee_id)}
        self.employees_collection.update_one(filter_criteria, {'$set': updated_employee_data})
        return self.employees_collection.find_one(filter_criteria)

    def delete_employee(self, employee_id):
        result = self.employees_collection.delete_one({'_id': ObjectId(employee_id)})
        return result.deleted_count