Package: *xuebadb*  
Sub-packages: *dbgeneric* and *dfanalysis*  

**Sub-package: `dbgeneric`**  
* Module: *odbc_interface* This module is responsible for connecting to and querying from a Microsoft SQL Server DB using the ODBC driver and pyodbc module. This module has a class ODBCInterface which contains the following methods:-
  * `__init__` takes the server name, username, password and database name and stores it in class instance attributes
  * `__connect` is a private method that creates the connection using the class attributes which we stored in the constructor. It makes use of pyodbc module.
  * `select` takes the query that the user wants to run as a string and returns a [Pandas dataframe](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.html) as the output.

* Module: `mysql_interface` This module is responsible for connecting to and querying from a MySQL DB. The module has a class MySQLInterface that contains the following methods:
  * `__init__` takes the server name, username, password and database name and stores it in class instance attributes.
  * `__connect` makes use of the mysql.connector module to create a connection object using the class attributes.
  * `select` takes the query and return the query result as a [Pandas dataframe](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.html).
  
**Sub-package: `dfanalysis`**  
* Module: `cleanup` This module contains the following method to display the missing values:
  * `show_nulls` displays the data sparsity matrix to see missing values. It replaces with None values in the pandas dataframe with numpy NaN values, and display the sparsity matrix using the missingno and matplotlib.pyplot modules. 
