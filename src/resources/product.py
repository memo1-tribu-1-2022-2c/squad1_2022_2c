from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields
from services.product import ProductService


product_service = ProductService()

class ProductResponse(Schema):
    product = fields.Str(default="Some product")
    product_id = fields.Int(default=0)
    versions = fields.List(fields.Str(default="A lot of versions"))

class ProductCreate(Schema):
    product = fields.Str(default="Some product name")


class ProductSearchResource(MethodResource, Resource):
    @doc(description="Returns a product with all its versions", tags=["Products"])
    @marshal_with(ProductResponse)
    def get(self, product_id: str):
        result = product_service.search_product(product_id)
        return result




class ProductResource(MethodResource, Resource):

    @doc(description="Creates a new product", tags=["Products"])
    @use_kwargs(ProductCreate)
    @marshal_with(ProductResponse)
    def post(self, **kwargs):
        new_product = product_service.new_product(**kwargs)
        return new_product
        