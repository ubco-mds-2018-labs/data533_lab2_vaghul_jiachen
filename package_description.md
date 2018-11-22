<<<<<<< HEAD
# data533_lab2_vaghul_jiachen
Submission repository for DATA-533 Lab 2

Group Members:-
* Vaghul Aditya Balaji
* Jiachen Wei

Package: *xuebadb*  
Sub-packages: *dbgeneric* and *dfanalysis*  

**dbgeneric:-**  
Modules:-  
* *odbc_interface* - This module is responsible for connecting to and querying from a Microsoft SQL Server DB using the ODBC driver and pyodbc module. This module has a class ODBCInterface which contains the following methods:-
  * *\_\_init\_\_*: This takes the server name, username, password and database name and stores it in class instance attributes
  * *\_\_connect*: This is a private method that creates the connection using the class attributes which we stored in the constructor. It makes use of pyodbc module.
  * *select*: This method takes the query that the user wants to run as a string and returns a [Pandas dataframe](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.html) as the output.
=======
***xuebadb*** is a python package that allows users to conveniently connect to and query from various database systems using a unified API. Currently, it supports connecting to *MySQL* and *SQL Server* database systems. The queries return Pandas dataframes which can then be cleaned up and analysed using one of the modules in the package.

---

**Requirements:-**  
In order to be able to use the package, you would have to install the following:-

Python packages:-
* pyodbc
* mysql.connector
* pandas
* numpy
* missingno

[ Microsoft ODBC Driver 17 ](https://docs.microsoft.com/en-us/sql/connect/python/python-driver-for-sql-server?view=sql-server-2017)

---

**Package structure:-**

xuebadb --> package  
 -- dbgeneric --> sub-package  
    -- db_interface --> module   
    -- mysql_interface -->module  
    -- odbc_interface --> module  
 -- dfanalysis --> sub-package
     -- cleanup --> module
     -- stats --> module
     
Please use *DATA533_Lab2_Vaghul_Jiachen.py* to test out the package and the functionalities.
>>>>>>> bcee66718a12fffaadc2db8dcb7f8e232ac1f65b
