import xuebadb.dbgeneric.mysql_interface as mysql
import xuebadb.dbgeneric.odbc_interface as odbc

mysql_con = mysql.MySQLInterface('cosc304.ok.ubc.ca', 'vbalaji', '10796456', 'WorksOn')
mysql_res = mysql_con.select("select * from dept")

odbc_con = odbc.ODBCInterface("sql04.ok.ubc.ca", "rlawrenc", "test", "workson")
odbc_res = odbc_con.select("select * from dept")
