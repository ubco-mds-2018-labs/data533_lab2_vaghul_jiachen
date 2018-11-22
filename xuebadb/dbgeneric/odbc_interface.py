import pyodbc
import pandas

class ODBCInterface:
    def __init__(self, server, username, password, dbname):
        self.server = server
        self.username = username
        self.password = password
        self.dbname = dbname
        
    def __connect(self): #private
        try:
            self.cnx = pyodbc.connect("""DRIVER={ODBC Driver 17 for SQL Server};
                                      SERVER="""+str(self.server)+""";
                                      DATABASE="""+str(self.dbname)+""";
                                      UID="""+str(self.username)+""";
                                      PWD="""+str(self.password))
        except pyodbc.Error as err:  
            print("Error when connecting to the database.")
            print(err)
            self.cnx.close()
            
    def select(self, query):
        try:
            self.__connect()
            cursor = self.cnx.cursor()
            cursor.execute(query) 
            output = []
            for row in cursor:
                inner_list = []
                for val in row:
                    inner_list.append(str(val).strip())  #remove trailing white space to create dataframe
                output.append(inner_list)
            cursor.close()
            return pandas.DataFrame(output)
        except:  
            print("Unable to run SELECT query")
        finally:
            self.cnx.close()