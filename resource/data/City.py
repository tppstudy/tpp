import json

import pymysql


def get_city_data():

    db = pymysql.Connect(host = "localhost",user = "root",password = "gwlh1234",database = "flaskday56",charset = "utf8")
    Cursor = db.cursor()

    with open("City.json",'rb') as city_info:
        citis = json.load(city_info)
        returnValues = citis.get("returnValue")
        #print(returnValues)
        letters = returnValues.keys()
        for letter in letters:
            # db.begin()
            # Cursor.execute("INSERT INTO letter(letter) values  ('{}');".format(letter))
            # db.commit()

            db.begin()
            sqlstr = "select * from  letter where letter= '{}';".format(letter)
            Cursor.execute(sqlstr)
            result = Cursor.fetchone()
            db.commit()
            letter_citis = returnValues.get(letter)
            for letter_city in letter_citis:
                regionName = letter_city.get("regionName")
                id = letter_city.get("id")
                pinYin = letter_city.get("pinYin")
                cityCode = letter_city.get("cityCode")
                db.begin()
                sqlstr = "INSERT INTO city(id,regionName,cityCode,pinYin,c_letter) values  ({},'{}',{},'{}',{});".format(id,regionName,cityCode,pinYin,result[0])
                Cursor.execute(sqlstr)
                db.commit()
if __name__ == '__main__':
    get_city_data()