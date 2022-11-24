from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from marshmallow import Schema, fields



class VersionResponse(Schema):
    version = fields.Str(default="Version 1.0")
    product = fields.Str(default="Some product")


class VersionCreate(Schema):
    version = fields.Str(default="Some version number")
    product = fields.Str(default="Product for which the version belongs")


class VersionSearchResource(MethodResource, Resource):

    @doc(description="Returns a version from a product", tags=['Versions'])
    @marshal_with(VersionResponse)
    def get(self, version_id):
        return {
            'version': 'version:' + version_id,
            'product': 'El que mas te guste'
        }


class VersionResource(MethodResource, Resource):



    @doc(description="Creates a new version for the product", tags=['Versions'])
    @use_kwargs(VersionCreate)
    @marshal_with(VersionResponse)
    def post(self, **kwargs):
        return {
            'version': kwargs['version'],
            'product': kwargs['product']
        }