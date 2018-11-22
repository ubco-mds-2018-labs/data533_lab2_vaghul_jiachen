<<<<<<< HEAD
xuebadb is a package to access and query a specified type of database, and perform analysis of the query result. This version allows SQL and MySQL databases.

need to install ...

pyodbc

[ Microsoft ODBC Driver 17 ](https://docs.microsoft.com/en-us/sql/connect/python/python-driver-for-sql-server?view=sql-server-2017)

## `dbgeneric` subpackage

#### `db_interface` module

#### `odbc_interface` module

#### `mysql_interface` module

## `dfanalysis` subpackage

#### `stats` module
#### `visuals` module
=======
# data533_lab2_vaghul_jiachen
Submission repository for DATA-533 Lab 2

Group Members:-
* Vaghul Aditya Balaji
* Jiachen Wei

Package: *xuebadb*  
Sub-packages: *dbgeneric* and *dfanalysis*  

**Sub-package: dbgeneric**  
* Modules: *odbc_interface* - This module is responsible for connecting to and querying from a Microsoft SQL Server DB using the ODBC driver and pyodbc module. This module has a class ODBCInterface which contains the following methods:-
  * *\_\_init\_\_*: This takes the server name, username, password and database name and stores it in class instance attributes
  * *\_\_connect*: This is a private method that creates the connection using the class attributes which we stored in the constructor. It makes use of pyodbc module.
  * *select*: This method takes the query that the user wants to run as a string and returns a [Pandas dataframe](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.html) as the output.
>>>>>>> bcee66718a12fffaadc2db8dcb7f8e232ac1f65b
