
import mysql.connector

class database:
    
    def __init__(self,database):
        self.database = database
        self.mydatabase = mysql.connector.connect(host = "localhost",
                                       user="root",
                                       passwd="ZKMoguz1958+",
                                       database= database)
        #mycursor= self.mydatabase.cursor()
    def show_table(self,table_name):  
        mycursor= self.mydatabase.cursor()
        mycursor.execute("DESCRIBE {}".format(table_name))
        
        for table in mycursor:
            print(table)
        
           
    def create_table(self,table_name,fields):
        query = "CREATE TABLE IF NOT EXISTS {} (".format(table_name)
        for i in range(len(fields)-1):
            query = query+ "{} ,".format(fields[i])
        query += "{});".format(fields[-1])
        
        mycursor= self.mydatabase.cursor()
        mycursor.execute(query)
        
    def insert_data(self,table_name,fields,data):
        
        
        query = "INSERT INTO {}(".format(table_name)
        
        if len(fields) ==1:
            
            query += "{})".format(fields)
        else:
            for field in range(len(fields)-1):
                
                query += "{},".format(fields[field])
                
            query += "{})".format(fields[-1]) 
            
        query += " VALUES ("
        if len(data) == 1:
            query += "%s)"
        else:
            for i in range(len(data)-1):
                query += "%s,"
            query += "%s)"
                
        print(query)
        
        if len(data) == len(fields):
            
            param = tuple(i for i in data)    
            mycursor= self.mydatabase.cursor()
            mycursor.execute(query,param)
            self.mydatabase.commit()
       
        else:
            
            mycursor= self.mydatabase.cursor()
            mycursor.executemany(query,data)
            self.mydatabase.commit()

