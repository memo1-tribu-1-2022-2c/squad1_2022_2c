from flask import Flask
from flask_restful import Api
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})
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



db = psycopg2.connect(database="soporte",
                        host="oregon-postgres.render.com",
                        user="soporte_user",
                        password="6WqrfY2A46IdtKIsn903Ek3jCxKu6hS0",
                        port="5432")

def connect_and_return():
    global db
    if db.closed:
        db = psycopg2.connect(database="soporte",
                        host="oregon-postgres.render.com",
                        user="soporte_user",
                        password="6WqrfY2A46IdtKIsn903Ek3jCxKu6hS0",
                        port="5432")
    return db


def try_commit():
    global db
    try:
        db.commit()
    except:
        db.rollback()

def rollback():
    global db
    db.rollback()