from flask_restful import Resource, reqparse
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields
from services.client import ClientService
from .product import ProductResponse

from flask_cors import cross_origin

import requests

class Employee(Schema):

    legajo = fields.Str();
    Nombre = fields.Str();
    Apellido = fields.Str();

class EmployeesSchema(Schema):
    employees = fields.List(fields.Nested(Employee))


class EmployeeResource(Resource, MethodResource):

    @doc(description="Returns all employees", tags=["Employees"])
    @marshal_with(EmployeesSchema)
    def get(self):
        employees = requests.get("https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/recursos-psa/1.0.0/m/api/recursos").json();
        return {
            'employees': employees
        }