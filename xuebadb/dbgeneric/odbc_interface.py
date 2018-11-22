import pyodbc
import pandas

class ODBCInterface:
    def __init__(self,server,username,password,dbname):
        self.server = server
        self.username = username
        self.password = password
        self.dbname = dbname
    def __connect():  #private
        try:
            self.cnx = pyodbc.connect("""DRIVER={ODBC Driver 17 for SQL Server};
                        SERVER="""+str(self.server)+""";
                        DATABASE="""+str(dbname)+""";
                        UID="""+str(username)+""";
                        PWD="""+str(password))
        except pyodbc.Error as err:  
            print("Error when connecting to the database.")
            print(err)
            self.cnx.close()
    def select(self, query):
        try:
            self.__connect()
            cursor = cnx.cursor()
            cursor.execute(query) 
            output=[]
            for row in cursor:
                output.append(row)
            cursor.close()
            output=pandas.DataFrame(output)
            return output
        except pyodbc.Error as err:  
            print(err)
            
test=ODBCInterface("sql04.ok.ubc.ca","rlawrenc","test","workson")