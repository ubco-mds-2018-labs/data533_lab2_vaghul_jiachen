from mysql_interface import MySQLInterface
from odbc_interface import ODBCInterface
class DBInterface(ODBCInterface, MySQLInterface):   #inherit
    def __init__(self,dbtype,server,username,password,dbname):
        dbtypelist=['sql_server','mysql']
        if dbtype not in dbtypelist:
            raise Exception("The argument \'dbtype\' must be in the list {}".format(dbtypelist) )
        if dbtype=='sql_server':
            ODBCInterface.__init__(self,server,username,password,dbname)
            self.dbtype = dbtype
        elif dbtype=='mysql':
            MySQLInterface.__init__(self, server, username, password, dbname)
            self.dbtype = dbtype
    def querySelect(self,query):
        if self.dbtype=='sql_server':
            ODBCInterface.select(self,query)
        if self.dbtype=='mysql':
            MySQLInterface.select(self,query)