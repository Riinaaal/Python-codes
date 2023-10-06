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
    # Get distance from distance table
    sql = f"SELECT distance_km FROM distance WHERE record_id in (select max(record_id) from distance)"
    cursor = connection.cursor()
    cursor.execute(sql)
    total= cursor.fetchall()
    initialDistance = 0
    for row in total:
        initialDistance = row[0]


    # Get how event effects distance and co2
    sql2 = f"SELECT co2_change, distance_change FROM event INNER JOIN choice on choice.event_occurred = event.id WHERE choice.id = {round}"
    cursor = connection.cursor()
    cursor.execute(sql2)
    eventEffect = cursor.fetchall()
    co2_change = 0
    distance_change = 0
    for row in eventEffect:
        co2_change = row[0]
        distance_change = row[1]
        if distance_change == None:
            distance_change = 0

    finalDistance = initialDistance * distance_change + initialDistance


    # Find out plane type to calculate emissions
    sql3 = f"SELECT co2_emission_per_km from airplane INNER JOIN choice on choice.plane_type = airplane.type WHERE choice.id = {round} "
    cursor = connection.cursor()
    cursor.execute(sql3)
    result = cursor.fetchall()
    emissionRate = 0
    for row in result:
        emissionRate = row[0]

    finalCO2 = (finalDistance * emissionRate * co2_change) + (finalDistance * emissionRate)


    #Update final result of co2_spent to choice table
    sql4 = f"UPDATE choice SET co2_spent =  %s WHERE choice.id = {round}"
    val = [finalCO2]
    cursor = connection.cursor()
    cursor.execute(sql4, (val))
    cursor.fetchall()


    # Get current co2_consumed & total_travelled
    sql5 = f"SELECT co2_consumed, total_travelled FROM player WHERE player.id = 1"
    cursor = connection.cursor()
    cursor.execute(sql5)
    info = cursor.fetchall()
    co2_original = 0
    total_km_original = 0
    for row in info:
        co2_original = row[0]
        total_km_original = row[1]

    update_km = total_km_original + finalDistance
    update_co2 = co2_original + finalCO2


    # Update co2_cosnsumed and total_travelled
    sql6 = f"UPDATE player SET co2_consumed = %s, total_travelled = %s WHERE player.id = 1"
    cursor = connection.cursor()
    cursor.execute(sql6, (update_co2, update_km))
    cursor.fetchall()

    return
