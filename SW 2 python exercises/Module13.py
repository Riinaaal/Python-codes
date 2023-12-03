from flask import Flask
import mysql.connector


connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='riinaaal',
         autocommit=True)

app = Flask(__name__)


# Assignment 1
@app.route('/prime_number/<number>')
def calculate(number):
    num = int(number)
    fulfills = 0
    for x in range(num):
        if x != 0 and num % x == 0 and x != num:
            fulfills = fulfills + 1

    if fulfills == 1 and num != 1:
        return f'"Number": {num}, "isPrime": true'
    else:
        return f'"Number": {num}, "isPrime": false'


# Assignment 2
@app.route('/airport/<icao>')
def get_location(icao):
    sql = "SELECT ident, name, municipality FROM airport WHERE ident = '" + icao + "' "
    cursor = connection.cursor()
    cursor.execute(sql)
    answer = cursor.fetchall()
    result = answer[0]
    return f'"ICAO": "{result[0]}", "Name": "{result[1]}", "Location": "{result[2]}" '


app.run(host="127.0.0.1", debug=True, port=5000)