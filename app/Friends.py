import sqlite3
from app.views import *


class Friends(object):
    def __init__(self, request):
        """description of class"""
        self.Test = "Test"
        self.request = request
        #!/usr/bin/python

        import sqlite3

        conn = sqlite3.connect('db.sqlite3')
   

        print("Opened database successfully");

        conn.execute("""create table if not exists `FRIENDS` (
	    `ID`	INTEGER NOT NULL,
	    `ID_FRIEND`	INTEGER);""")

       
        current_user = request.user
        self.current_user = current_user
        

        print(current_user.id)

        Friend_list = []

        cursor = conn.execute("SELECT ID_FRIEND from FRIENDS where ID ="+ str(current_user.id)+ ";")
        for row in cursor:
           print("ID_FRIEND = ", row[0], "\n")
           Friend_list.append(row[0])
        print(Friend_list)


        Counter = len(Friend_list) -1 
        Friend_list_name = []
        while Counter >= 0:
            cursor2 = conn.execute("SELECT username from auth_user where id ="+ str(Friend_list[Counter]) + ";")
            for row in cursor2:
               print("ID_Name = ", row[0], "\n")
               Friend_list_name.append(row[0])
            Counter = Counter -1
        print(Friend_list_name)
        self.Friend_list_name = Friend_list_name





        

        

    