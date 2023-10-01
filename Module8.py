import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='riinaaal12345',
         autocommit=True)

# Module 8 assignment 1
def getLocation(location):
    sql = "SELECT name, municipality FROM airport WHERE ident = '" + location + "' "
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

location = input("Enter ICAO code of an airport ")
print(getLocation(location))

# Module 8 assignment 2

def totalAirports(area_code):
    sql = "SELECT type, count(*) FROM airport WHERE iso_country = '" + area_code +"' Group by type desc"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

area_code = input("Enter area code ")
print(totalAirports(area_code))

# Module 8 assignment 3

def locationCodes(code):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '" + code +"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

first = input("Enter ICAO code of first airport ")
second = input("Enter ICAO code of second airport ")


from geopy import distance

cordinatesFirst = locationCodes(first)
cordinatesSecond = locationCodes(second)
print(f" Distance between airports is {distance.distance(cordinatesFirst, cordinatesSecond).km: .2f} kilometers")