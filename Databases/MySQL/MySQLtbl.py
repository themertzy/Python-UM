
import mysql.connector
from MySQLdb import *

class defineTBL:

  def __init__(self, db, host, pswrd, tblname):

    self.db = db
    self.host = host
    self.pswrd = pswrd
    self.tblname = tblname

    self.strdb = str(self.db)
    self.strhost = str(self.host)
    self.pswrd = str(self.pswrd)
    self.strtblname = str(self.strtblname)

  def createTBL(self, db, host, user, pswrd, tblname):     #creates a new table with no columns. 
                                                           #this is so that the user has complete
    self.db = db                                           #control over adding and removing columns
    self.host = host
    self.user = user                     
    self.pswrd = pswrd
    self.tblname = tblname

    self.network = connectdb(self.db, self.host, self.user, self.pswrd)
    self.network.execute("CREATE TABLE " + self.strtblname + " (id INT AUTO_INCREMENT PRIMARY KEY)")