import MySQLdb

# Open database connection
db = MySQLdb.connect("192.168.99.100",
                     "root",
                     "myRootpwd32",
                     "WhiskeyClub" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

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
db.close()