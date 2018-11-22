import mysql.connector
import pandas as pd

class MySQLInterface:    
    def __init__(self, server, username, password, dbname):
        self.server = server
        self.username = username
        self.password = password
        self.dbname = dbname
        
    def __connect(self):        
        try:
            self.cnx = mysql.connector.connect(user=self.username, password=self.password, host=self.server, database=self.dbname)
        except mysql.connector.Error as err:
            print(err)
            self.cnx.close()
            
    def select(self, query):
        try:
            self.__connect()
            output = []
            cursor = self.cnx.cursor()
            cursor.execute(query)
            for row in cursor:
                output.append(row)
            cursor.close()
            return pd.DataFrame(output)
        except:
            print("Unable to run the SELECT query")
        finally:
            self.cnx.close()
            