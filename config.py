from flask import Flask
from flask_restful import Api
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec

app = Flask(__name__)
api = Api(app)
docs = FlaskApiSpec(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Modulo Soporte',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
