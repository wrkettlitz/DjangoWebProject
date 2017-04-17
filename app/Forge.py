import sqlite3
from app.views import *


class Forge(object):
    
    def __init__(self, request):
        """description of class"""
        self.Test = "Test"
        self.request = request
        #!/usr/bin/python
        import sqlite3
        conn = sqlite3.connect('db.sqlite3')
        

        
   

        print("Opened database successfully");

        conn.execute("""create table if not exists 'Forge' (
        `User_ID` INTEGER, `Weapon` INTEGER, PRIMARY KEY(`User_ID`));""")
        
       
        current_user = request.user
        self.current_user = current_user

        print("user id = " + str(current_user.id))
        Credits =0
        Credits_table = conn.execute("SELECT Credits from Credits where ID ="+ str(current_user.id)+ ";")
        for row in Credits_table:
           print("Credits = ", str(row[0]), "\n")
           Credits = str(row[0])
        self.Credits = Credits

        current_weapon_level = 0
        current_weapon_level_table = conn.execute("SELECT weapon from Forge where User_ID ="+ str(current_user.id)+ ";")
        for row in current_weapon_level_table:
            print("current_weapon_level =" + str(row[0]))
            current_weapon_level = row[0]
            
        self.current_weapon_level = current_weapon_level



        current_weapon_name = ""
        next_weapon_name = ""
        next_weapon_cost = 0
        if current_weapon_level == 1:
            current_weapon_name = "Bronze Sword"
            next_weapon_name = "Iron Sword"
            next_weapon_cost = 2500
        elif current_weapon_level == 2:
            current_weapon_name = "Iron Sword"
            next_weapon_name = "Steel Sword"
            next_weapon_cost = 5000
        elif current_weapon_level == 3:
            current_weapon_name = "Steel Sword"
            next_weapon_name = "Mithril Sword"
            next_weapon_cost = 10000
        elif current_weapon_level == 4:
            current_weapon_name = "MithrilSword"
            next_weapon_name = "Max Quality Reached"

        self.current_weapon_name = current_weapon_name
        self.next_weapon_name = next_weapon_name
        self.next_weapon_cost = next_weapon_cost


    def BuyWeapon(request, current_credits, next_weapon_cost, current_weapon_level):
        if  current_credits>=next_weapon_cost and  current_weapon_level <4:
            
            import sqlite3
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.cursor()

        
        
            current_user = request.user
        
            cur.execute("UPDATE Forge SET weapon=? WHERE User_ID=?", (int(current_weapon_level) + 1, current_user.id))
            cur.execute("UPDATE Credits SET Credits=? WHERE ID=?", (int(current_credits) - (int(next_weapon_cost)), (current_user.id)))
            print("buyweapon wordt uitgevoerd" + str(current_credits) + str(next_weapon_cost) + str(current_weapon_level)) 
            conn.commit()
            conn.close()

    def TestAccountDefaultValues(self,AccountID, weapon_level, Credits ):
        import sqlite3
        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()
        cur.execute("UPDATE Forge SET weapon=? WHERE User_ID=?", (weapon_level, AccountID))
        cur.execute("UPDATE Credits SET Credits=? WHERE ID=?", (Credits, AccountID))
        conn.commit()
        conn.close()

      
        