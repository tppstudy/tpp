from App.ext import db


"""
            {
                "id": 454,
                "parentId": 0,
                "regionName": "安阳",
                "cityCode": 410500,
                "pinYin": "ANYANG"
            }
"""
class Letter(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement = True)
    letter = db.Column(db.String(1))
class City(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    regionName = db.Column(db.String(16))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(128))
    c_letter = db.Column(db.Integer,db.ForeignKey(Letter.id))