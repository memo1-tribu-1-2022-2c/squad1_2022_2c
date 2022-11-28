from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields

from services.version import VersionService

version_service = VersionService()

class VersionResponse(Schema):
    number = fields.Str(default="Version 1.0")
    version_id = fields.Int(default=0)
    state = fields.Str(default="Deprecated")


class VersionListResponse(Schema):
    versions = fields.List(fields.Nested(VersionResponse))

class VersionCreate(Schema):
    number = fields.Str(required=True)
    product_id = fields.Int(required=True)

class VersionModifySchema(Schema):
    version_id = fields.Str(required=True)
    number = fields.Str(required=False)
    state_change = fields.Boolean(required=False)

class VersionErrorSchema(Schema):
    error = fields.Str(default="Could not retrieve versions")

class VersionSearchResource(MethodResource, Resource):

    @doc(description="Returns a version from a product", tags=['Versions'])
    @marshal_with(VersionListResponse)
    @marshal_with(VersionErrorSchema, code='404')
    def get(self, product_id):
        try:
            return {'versions': version_service.get_by_product_id(product_id)}
        except:
            return {
                'error': f'Could not retrieve versions from product: {product_id}'
            }, '404'

class VersionResource(MethodResource, Resource):



    @doc(description="Creates a new version for the product", tags=['Versions'])
    @use_kwargs(VersionCreate)
    @marshal_with(VersionResponse)
    @marshal_with(VersionErrorSchema, code='404')
    def post(self, **kwargs):
        try:
            return version_service.store_new_version(**kwargs)
        except:
            return {
                'error': f'Could not store new version {kwargs["number"]} in product {kwargs["product_id"]}'
            }, '404'

    @doc(description="Allows to change the number and status of a version", tags=['Versions'])
    @use_kwargs(VersionModifySchema)
    @marshal_with(VersionResponse)
    @marshal_with(VersionErrorSchema, code='404')
    def patch(self, **kwargs):
        
        try:

            return version_service.modify_version(**kwargs)

        except Exception as exception:

            return {
                'error': exception.args[0]
            }, '404'