import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='team_12',
         user='root',
         password='riinaaal12345',
         autocommit=True)


# BACKEND functions start here ----------------
def get_airport_info(ICAO):
    sql = f"SELECT ident, name, latitude_deg, longitude_deg FROM airport WHERE ident = '{ICAO}' "
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

def co2_spent(round):
    sql = f"SELECT distance_km FROM distance WHERE record_id in (select max(record_id) from distance)"
    cursor = connection.cursor()
    cursor.execute(sql)
    initialDistance = cursor.fetchall()

    sql2 = f"SELECT co2_change, distance_change FROM event INNER JOIN choice on choice.event_occurred = event.id WHERE choice.id = round"
    cursor = connection.cursor()
    cursor.execute(sql2)
    eventEffect = cursor.fetchall()
    co2_change = 0
    distance_change = 0
    for row in eventEffect:
        co2_change = row[0]
        distance_change = row[1]

    finalDistance = (initialDistance * distance_change)

    sql3 = f"SELECT co2_emission_per_km from airplane INNER JOIN choice on choice.planetype = airplane.type WHERE choice.id = round "
    cursor = connection.cursor()
    cursor.execute(sql3)
    emissionRates = cursor.fetchall()
    emissionRate = 0
    for row in emissionRates:
        emissionRate = row[0]

    finalCO2 = (finalDistance * emissionRate) * co2_change

    sql4 = f"INSERT INTO choice(co2_spent) VALUES (%s)"
    val = [finalCO2]
    cursor = connection.cursor()
    cursor.execute(sql4,val)
    cursor.fetchall()
    return
