import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='team_12',
         user='root',
         password='riinaaal12345',
         autocommit=True)

def get_airport(ICAO):
    sql = f"SELECT name FROM airport WHERE ident = '{ICAO}' "
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def create_player(name):
    sql = f"SELECT player_name FROM player WHERE player_name = '{name}' "
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount == 0:
        co2_budget = 20000
        co2_consumed = 0
        total_travelled = 0
        sql2 = f"INSERT INTO player(player_name,co2_budget,co2_consumed,total_travelled)VALUES (%s,%s,%s,%s)"
        val = [name, co2_budget, co2_consumed, total_travelled]
        cursor = connection.cursor()
        cursor.execute(sql2, val)
        cursor.fetchall()

    else:
        name2 = input("Player already exists, enter new name: ")
        co2_budget = 20000
        co2_consumed = 0
        total_travelled = 0
        sql2 = f"INSERT INTO player(player_name,co2_budget,co2_consumed,total_travelled)VALUES (%s,%s,%s,%s)"
        val = [name2, co2_budget, co2_consumed, total_travelled]
        cursor = connection.cursor()
        cursor.execute(sql2, val)
        cursor.fetchall()

    return
