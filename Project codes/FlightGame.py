import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='team12',
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

def create_player():
    while True:
        name = input("Enter name: ")

        sql = f"SELECT player_name FROM player WHERE player_name = '{name}' "
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        if cursor.rowcount == 0:
            co2_budget = 1000000
            co2_consumed = 0
            total_travelled = 0
            sql2 = f"INSERT INTO player(player_name,co2_budget,co2_consumed,total_travelled)VALUES (%s,%s,%s,%s)"
            val = [name, co2_budget, co2_consumed, total_travelled]
            cursor = connection.cursor()
            cursor.execute(sql2, val)
            cursor.fetchall()
            break

        else:
            print("Player already exists!")

    return name


def co2_spent(round, name):
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
    sql5 = f"SELECT co2_consumed, total_travelled FROM player WHERE player.screen_name = '{name}'"
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
    sql6 = f"UPDATE player SET co2_consumed = %s, total_travelled = %s WHERE player.screen_name = '{name}'"
    cursor = connection.cursor()
    cursor.execute(sql6, (update_co2, update_km))
    cursor.fetchall()

    return

# Fixed event function
def event_occurrence(turn,userid):
    import random
    sql = f"SELECT * from event"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    random.choice(result)
    weights = []
    events = []
    for row in result:
        #print(row)
        events.append(row[1])
        weights.append(row[3]*100)

    #print(weights)
    pick = random.choices(events, weights = weights, k=1)

    posneg = ''
    co2 = 0
    event = 0
    sql2 = f"SELECT * from event WHERE info = '{pick[0]}'"
    cursor = connection.cursor()
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    for row in result2:
        posneg = row[2]
        co2 = row[4]
        event = row[0]

    if pick[0] == 'No event':
        print("")
        sql3 = f"UPDATE choice SET event_occurred = {event} WHERE turn = {turn} AND player_name = '{userid}'"
        cursor = connection.cursor()
        cursor.execute(sql3)
    else:
        print("\n\nyou've got a message from control tower!")
        print(pick[0])
        print("\nThe event will affect your flight :")
        if posneg == 'neg':
            #if row[5] == 'NULL': ignoring the distance pe
            print(f"Co2 consumption is {co2 * 100}% increased!")
            sql4 = f"UPDATE choice SET event_occurred = {event}, co2_spent = co2_spent + co2_spent* {co2} WHERE turn = {turn} AND player_name = '{userid}'"
            cursor = connection.cursor()
            cursor.execute(sql4)
        elif posneg == 'pos':
            print(f"Co2 consumption is {co2 * 100}% decreased!")
            sql5 = f"UPDATE choice SET event_occurred = {event}, co2_spent = co2_spent - co2_spent* {co2} WHERE turn = {turn} AND player_name = '{userid}'"
            cursor = connection.cursor()
            cursor.execute(sql5)
