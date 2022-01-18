from flask import Flask, request
import os
import mysql.connector
from utils.utils import app_prediction
import MySQLdb

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config["DEBUG"] = True


# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>API para desafío de tripulaciones.</p>"


# @app.route('/api/v1/append_register', methods = ['GET'])
# def append_register():

#     '''
#     Permite guardar nuevos registros.
#     '''
#     connection = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'password',
#     database = 'webs_db'
#     )
#     cursor = connection.cursor()
#     # url = request.form['URL']
#     url = 'https://www.porno.com'
#     # status = request.form['status']
#     # status = status.lower()
#     status = 'legitimate'

#     values_list = [url, status]

#     if url is None or status is None:
#         connection.commit()
#         connection.close()
#         return "Missing values, the data were not stored"

#     else:
#         cursor.execute('INSERT INTO webs (url, status) VALUES (%s,%s);', values_list)

#     connection.commit()
#     connection.close()
#     return 'Data stored'



@app.route('/', methods=['GET'])
def get_info():

    '''
    Devuelve si la web es ligítima o phishing en caso de que esté en la base de datos.
    '''
    # connection = mysql.connector.connect(
    # username = 'Desafio2109sep',
    # host = 'desafio-tripulaciones.c7f2y5gspcuf.eu-west-3.rds.amazonaws.com',
    # port = 10100,
    # password = 'Desafio21Tripulaciones09',
    # database = 'desafio_tripulaciones_db'
    # )

    server = "desafio-tripulaciones.c7f2y5gspcuf.eu-west-3.rds.amazonaws.com"
    pwd = "Desafio21Tripulaciones09"
    dbname = "desafio_tripulaciones_db"
    user = "Desafio2109sep"
    port = 10100

    connection = MySQLdb.connect(server, user, pwd, dbname, port, charset='utf8', use_unicode=True)

    cursor = connection.cursor()
    # url = request.form['URL']
    url = 'https://www.porno.com'

    if url is None:
        return "Missing values, the data connot be provided"

    else:
        try:
            query_get = "SELECT * FROM web_table WHERE url LIKE %s;"
            cursor.execute(query_get, (url,))
            url, result = cursor.fetchone()
            in_db = True

        except:
            print('Not in the DB')
            result = app_prediction(url, './models/One_Hot_Encoder', './models/web_predictor.model')
            url_predicted = [url, result]
            query_save = 'INSERT INTO web_table (url, status) VALUES (%s,%s);'
            cursor.execute(query_save, url_predicted)
            in_db = False
            connection.commit()
            connection.close()
            return {'url':url,'result': result, 'in_database':in_db}
    connection.commit()
    connection.close()

    return {'url':url,'result': result, 'in_database':in_db}

app.run()