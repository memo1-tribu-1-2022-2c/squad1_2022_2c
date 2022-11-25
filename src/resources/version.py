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



class VersionSearchResource(MethodResource, Resource):

    @doc(description="Returns a version from a product", tags=['Versions'])
    @marshal_with(VersionListResponse)
    def get(self, product_id):
        return {'versions': version_service.get_by_product_id(product_id)}

class VersionResource(MethodResource, Resource):



    @doc(description="Creates a new version for the product", tags=['Versions'])
    @use_kwargs(VersionCreate)
    @marshal_with(VersionResponse)
    def post(self, **kwargs):
        return version_service.store_new_version(**kwargs)