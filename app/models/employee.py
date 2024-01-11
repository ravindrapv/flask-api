import os
from marshmallow import Schema, fields, validate

class EmployeeSchema(Schema):
    _id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    position = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    salary = fields.Float(required=False, validate=validate.Range(min=0))
    experience = fields.Str(required=True, validate=validate.Length(min=1, max=50))