import falcon
import MySQLdb
import json
import db_conf

class Get_User:
    def on_get(self, req, resp):
        try:
            db = MySQLdb.connect(**db_conf.dbConfig)
            #use dictionary cursor
            cursor = db.cursor(MySQLdb.cursors.DictCursor)

            q = ("select * from USER")
            cursor.execute(q)
            rows = cursor.fetchall()

            #init the output object
            output = {'User': []}
            for row in rows:
                data = {
                        "user_id": row['user_id'],
                        "UserName": row['UserName'],
                        "Password": row['Password'],
                        "Email": row['Email']
                }

                output['User'].append(data)

            resp.status = falcon.HTTP_200
            resp.body = json.dumps(output, encoding='utf-8')
            cursor.close()
            db.close()

        except Exception as e:
            resp.body = json.dumps({'error': str(e)})
            resp.status = falcon.HTTP_500
            return resp

class Add_User:
    def on_post(self, req, resp):
        try:
            db = MySQLdb.connect(**db_conf.dbConfig)
            cursor = db.cursor()

            raw_json = req.stream.read()
            data = json.loads(raw_json, encoding='utf-8')
            q = """INSERT INTO USER (user_id, UserName, Password, Email) VALUES(%s,%s,%s,%s)"""

            cursor.execute(q, (data['user_id'], data['UserName'], data['Password'], data['Email']))
            db.commit()
            cursor.close()

            output = {
                'status': "Data successfully saved"
            }
            resp.status = falcon.HTTP_200
            data_resp = json.dumps(output, encoding='utf-8')
            resp.body = data_resp
            db.close()

        except Exception as e:
            db.rollback()
            resp.body = json.dumps({'error': str(e)})
            resp.status = falcon.HTTP_500
            return resp

class Update_User:
    def on_put(self, req, resp):
        try:
            db = MySQLdb.connect(**db_conf.dbConfig)
            cursor = db.cursor()

            raw_json = req.stream.read()
            data = json.loads(raw_json, encoding='utf-8')

            q = """UPDATE `USER` SET `user_id`=%s, `UserName`=%s, `Password`=%s, `Email`=%s WHERE id=%s"""
            cursor.execute(q, (data['user_id'], data['UserName'], data['Password'], data['Email']))
            db.commit()
            cursor.close()
            output = {
                'status': "Data successfully changed"
            }
            resp.status = falcon.HTTP_200
            data_resp = json.dumps(output, encoding='utf-8')
            resp.body = data_resp
            db.close()

        except Exception as e:
            db.rollback()
            resp.body = json.dumps({'error': str(e)})
            resp.status = falcon.HTTP_500
            return resp


class Delete_User:
    def on_delete(self, req, resp):
        try:
            user_id = req.get_param('user_id')
            if user_id is None or user_id == "":
                resp.body = json.dumps({'error': 'Parameter user_id is Wrong'})
                resp.status = falcon.HTTP_500
                return resp

            db = MySQLdb.connect(**db_conf.dbConfig)
            cursor = db.cursor()

            q = """DELETE FROM `USER` WHERE user_id=%s"""

            cursor.execute(q, (user_id,))
            db.commit()
            cursor.close()
            output = {
                'status': "Data successfully deleted"
            }
            resp.status = falcon.HTTP_200
            data_resp = json.dumps(output, encoding='utf-8')
            resp.body = data_resp

        except Exception as e:
            db.rollback()
            resp.body = json.dumps({'error': str(e)})
            resp.status = falcon.HTTP_500
            return resp

