from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields


class ProductResponse(Schema):
    product = fields.Str(default="Some product")
    versions = fields.List(fields.Str(default="A lot of versions"))

class ProductCreate(Schema):
    product = fields.Str(default="Some product name")


class ProductSearchResource(MethodResource, Resource):
    @doc(description="Returns a product with all its versions", tags=["Products"])
    @marshal_with(ProductResponse)
    def get(self, product_id):
        return {
            'product': 'Tremendo producto',
            'versions': ['1.0', '2.0', '3.0']
        }


class ProductResource(MethodResource, Resource):

    @doc(description="Creates a new product", tags=["Products"])
    @use_kwargs(ProductCreate)
    @marshal_with(ProductResponse)
    def post(self, **kwargs):
        return {
            'product': kwargs['product'],
            'versions': []
        }
