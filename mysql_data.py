import MySQLdb
from sqlalchemy import *

db = create_engine('mysql+mysqldb://root:myRootpwd32@192.168.99.100:3306/WhiskeyClub', pool_recycle=3600)
connection = db.connect()

# Open database connection
# db = MySQLdb.connect("192.168.99.100",
#                      "root",
#                      "myRootpwd32",
#                      "WhiskeyClub" )/apis/get/users

# prepare a cursor object using cursor() method
cursor = connection

# execute SQL query using execute() method.
sql = "select * from USER"

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        user_id = row[0]
        Username = row[1]
        Password = row[2]
        Email = row[3]
        # Now print fetched result
        print "user_id=%s,Username=%s,Password=%s,Email=%s" % \
            (user_id, Username, Password, Email )
except:
        print "Error: unable to fecth data"

# disconnect from server
connection.close()