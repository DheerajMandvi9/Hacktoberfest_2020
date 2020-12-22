import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = "mandvi"
DATABASE = "library"
AUTH_PLUGIN= "mysql_native_password"



def get_database():
    try:
        database = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            auth_plugin=AUTH_PLUGIN
        
        )
        cursor = database.cursor(dictionary=True)
        return database, cursor
    except mysql.connector.Error:
        return None, None
