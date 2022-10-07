import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3307,
        user='root',
        password='',
        db='flask login'
    )
    if connection.is_connected():
        print("Conexion Exitosa")
except Exception as ex:
    print(ex)
   