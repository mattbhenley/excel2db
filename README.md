# Setup the Excel Import Script

1. Install Python along with the pip package manager. Python needs to be in your Environment variable PATH so that it can be accessed in cmd from any directory. 

2. Using pip, install the following libraries in your python installation. 

    a. pyodbc

    b. xlrd
    
    c. pandads 

3. Download and install the obdc driver for sql server.
    https://www.microsoft.com/en-us/download/details.aspx?id=56567


4. Edit the .py file in any text editor adn modify the parameters shown below. Save changes.
Some other example server values are: 
    ```server = 'localhost\sqlexpress' # for a named instance```

    ```server = 'myserver,port' # to specify an alternate port```
    
    ```server = 'tcp:myserver.database.windows.net' for a server over the internet```

    ```server = 'localhost\SQLEXPRESS'```

    ```database = 'master'```
    
    ```password = ''```

    ```Provide the file name. The complete path is required. Leave the r behind the ' as it is need to successfully upload.```

    ```filename = r'/Users/matthenley/Desktop/Houston Northwest UPDATED.xlsx' ```

5. Run the script from the command line, powershell, IDLE or any Python IDE. When running in command line use the following:
        ``` python import_excel.py ```