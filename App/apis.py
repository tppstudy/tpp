from flask_restful import Api, Resource, fields, marshal_with, reqparse, marshal
from App.models import Letter, City

api = Api()


def init_api(app):
    api.init_app(app=app)

city_fields={
    "id" : fields.Integer,
    "regionName": fields.String,
    "cityCode": fields.Integer,
    "pinYin": fields.String,
}

letter_city_fields ={
    "A":fields.List(fields.Nested(city_fields)),
    "B": fields.List(fields.Nested(city_fields))
}

result_fields = {
    "returnCode":fields.String,
    "returnValue":fields.Nested(letter_city_fields)
}

class AreaResource(Resource):
    @marshal_with(result_fields)
    def get(self):

        # returnValues = {}
        # letters = Letter.query.all()
        # for letter in letters:
        #     letter_cities = City.query.filter_by(c_letter = letter.id)
        #     returnValues[letter.letter] = letter_cities
        # return {"returnCode": "0","returnValue":returnValues}
        returnValues = {}
        letters = Letter.query.all()#返回所有的城市
        letter_city_fields_dynamic = {}#定义一个动态的字典存储城市数据

        for letter in letters:
            letter_city_fields_dynamic[letter.letter] = fields.List(fields.Nested(city_fields))
            letter_cities = City.query.filter_by(c_letter=letter.id)
            returnValues[letter.letter] = letter_cities
        result_fields_dynamic = {
            "returnCode": fields.String,
            "returnValue": fields.Nested(letter_city_fields_dynamic)
        }
        data = {"returnCode": "0", "returnValue": returnValues}
        result = marshal(data=data, fields=result_fields_dynamic)
        return result


    def post(self):

        returnValues = {}
        letters = Letter.query.all()
        letter_city_fields_dynamic = {}

        for letter in letters:
            letter_city_fields_dynamic[letter.letter] = fields.List(fields.Nested(city_fields))
            letter_cities = City.query.filter_by(c_letter=letter.id)
            returnValues[letter.letter] = letter_cities
        result_fields_dynamic = {
            "returnCode":fields.String,
            "returnValue":fields.Nested(letter_city_fields_dynamic)
        }
        data = {"returnCode":"0","returnValue":returnValues}
        result = marshal(data=data,fields = result_fields_dynamic)
        return result
        #return {"returnCode": "0", "returnValue": returnValues}
api.add_resource(AreaResource, "/areas/")
