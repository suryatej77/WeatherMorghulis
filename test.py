import re
import MySQLdb

db=MySQLdb.connect(user="root",passwd="2312onnf",db="Users")

c=db.cursor()
city = []
c.execute('''SELECT cityname FROM City''')
city = str(c.fetchall())
city2 = re.findall(r"\'([A-Za-z]+)\'",city)

for t in city2:
	print (t)
