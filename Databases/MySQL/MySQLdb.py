
import mysql.connector

class defineDB:

  def __init__(self):   #db, host, user, pswrd


    self.db = "db"
    self.host = "host"
    self.user = "user"
    self.pswrd = "pswrd"

    self.strdb = str(self.db)
    self.strhost = str(self.host)
    self.struser = str(self.user)
    self.strpswrd = str(self.pswrd)

  def createDB(self, db, host, user, pswrd):     #creates a new MySQL database.

    self.db = db
    self.host = host
    self.user = user                
    self.pswrd = pswrd

    self.db = mysql.connector.connect(
      host = self.strhost,
      user = self.struser,
      passwd = self.strpswrd
    )

    self.thiscursor = self.db.cursor()
    self.thiscursor.execute("CREATE DATABASE " + self.strdb)

  def connectDB(self, db, host, user, pswrd):       #connect to an existing MySQL database.

     self.db = db
     self.host = host
     self.user = user                     
     self.pswrd = pswrd

     self.db = mysql.connector.connect(
       host = self.strhost,
       user = self.struser,
       passwd = self.strpswrd,
       database = self.strdb
     )

     self.thiscursor = self.db.cursor() 

     return self.thiscursor         #this function returns the cursor so 
                                    #that execute can be used directly

  