from flask_restful import Api, Resource, fields, marshal_with, reqparse
from App.models import Letter

api = Api()


def init_api(app):
    api.init_app(app=app)


class AreaResource(Resource):
    def get(self):
        return {"returnCode": "0"}


api.add_resource(AreaResource, "/areas/")
