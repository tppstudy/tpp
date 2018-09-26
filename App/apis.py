
from flask_restful import Api, Resource, fields, marshal_with, reqparse



api = Api()


def init_api(app):
    api.init_app(app=app)

