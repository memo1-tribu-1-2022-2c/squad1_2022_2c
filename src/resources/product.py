from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields
from services.product import ProductService
from .version import VersionResponse
from flask_cors import cross_origin


product_service = ProductService()


class ProductVersion(Schema):
    number = fields.Str(default="0.0")

class ProductResponse(Schema):
    product = fields.Str(default="Some product")
    product_id = fields.Int(default=0)
    versions = fields.List(fields.Nested(VersionResponse))

class ProductModifySchema(Schema):
    product_id = fields.Str(required=True)
    name = fields.Str(required=False)

class ProductCreate(Schema):
    product = fields.Str(default="Some product name")
    versions = fields.List(fields.Nested(ProductVersion))

class ProductSchema(Schema):
    product = fields.Str()
    product_id = fields.Str()

class ProductList(Schema):
    products = fields.List(fields.Nested(ProductSchema))

class ProductErrorSchema(Schema):
    error = fields.Str(default="Product not found")


class ProductSearchResource(MethodResource, Resource):
    @doc(description="Returns a product with all its versions", tags=["Products"])
    @marshal_with(ProductResponse)
    @marshal_with(ProductErrorSchema, code='404')
    def get(self, product_id: str):
        try:
            result = product_service.search_product(product_id)
            return result
        except Exception as exception:

            return {
                'error': exception.args[0]
            }, '404'

class ProductResource(MethodResource, Resource):

    @doc(description="Creates a new product", tags=["Products"])
    @use_kwargs(ProductCreate)
    @marshal_with(ProductResponse)
    @marshal_with(ProductErrorSchema, code='404')
    @cross_origin()
    def post(self, **kwargs):
        try:
            new_product = product_service.new_product(**kwargs)
            return new_product
        except:

            return {
                'error': 'Could not create Product'
            }, '404'

    @doc(description="Changes the name of a product", tags=["Products"])
    @use_kwargs(ProductModifySchema)
    @marshal_with(ProductResponse)
    @marshal_with(ProductErrorSchema, code='404')
    @cross_origin()
    def patch(self, **kwargs):
        try:
            return product_service.update_product(**kwargs)
        except Exception as exception:
            return {
                'error': exception.args[0]
            }, '404'

    @doc(description="Returns a list with the products", tags=["Products"])
    @marshal_with(ProductList)
    def get(self):
        return product_service.get_products()