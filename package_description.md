Package: *xuebadb*  
Sub-packages: *dbgeneric* and *dfanalysis*  

**Sub-package: dbgeneric**  
* Module: *odbc_interface* - This module is responsible for connecting to and querying from a Microsoft SQL Server DB using the ODBC driver and pyodbc module. This module has a class ODBCInterface which contains the following methods:-
  * *\_\_init\_\_*: This takes the server name, username, password and database name and stores it in class instance attributes
  * *\_\_connect*: This is a private method that creates the connection using the class attributes which we stored in the constructor. It makes use of pyodbc module.
  * *select*: This method takes the query that the user wants to run as a string and returns a [Pandas dataframe](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.html) as the output.
