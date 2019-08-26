import pyodbc
import pandas

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# server = 'tcp:myserver.database.windows.net' for a server over the internet
server = 'localhost\SQLEXPRESS'
database = 'master'
username = ''
password = ''
# Provide the file name. The complete path is required. Leave the r behind the ' as it is need to successfully upload.
filename = r'/Users/matthenley/Desktop/Sample_excel.xlsx'
