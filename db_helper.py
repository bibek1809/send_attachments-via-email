import sqlite3
import mysql.connector

DB_FILE = "./archive.dht"

class DBhelper:
    def __init__(self):
        pass
    
    def import_table(self):
        conn = None
        #conn = connection.MySQLConnection(user='admin', password='Password',host='db_url',database='database_name')
        conn = sqlite3.connect(DB_FILE)
        query = f"SELECT * FROM Sample_Table"
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
