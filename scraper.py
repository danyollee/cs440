import pymysql
pymysql.install_as_MySQLdb()
import csv
import MySQLdb


# open the connection to the MySQL server.
# using MySQLdb
mydb = MySQLdb.connect(host='classmysql.engr.oregonstate.edu', user='cs440_group04', passwd='5LCZ9XAEhfmE', db='cs440_group04')
print("db connected")
cursor = mydb.cursor()
csv_data = csv.reader(open('/Users/danlee/Documents/cs440/project/cs440/artists.csv','r', encoding = 'utf-8'))
assert(csv_data is not 0)
i=0
# for row in csv_data:
#     if i == 0:
#         i += 1
#         continue
#     print(row[0])
# execute and insert the csv into the database.
for row in csv_data:
    if i == 0:
        i += 1
        continue
    if i % 1000 == 0:
        print("Executing query: ", i)
    cursor.execute("INSERT INTO `artist`(`name`) VALUES (%s) ON DUPLICATE KEY UPDATE `name` = %s", (row[0], row[0]))
    i += 1
mydb.commit()
# close the connection to the database.
cursor.close()
print ("CSV has been imported into the database")
