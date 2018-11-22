# data533_lab2_vaghul_jiachen
Submission repository for DATA-533 Lab 2

Group Members:-
* Vaghul Aditya Balaji
* Jiachen Wei

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
