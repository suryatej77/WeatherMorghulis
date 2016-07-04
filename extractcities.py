import re
import MySQLdb

db=MySQLdb.connect(user="root",passwd="2312onnf",db="Users")

c=db.cursor()

text = open("/home/teja/Weather/w.html","r")
titles = re.findall('<td class="tablesaw-cell-persist"><a href="https://www.wunderground.com/global/stations/(.*?).html" title="Weather Forecast for (.*?)">(.*?)</a></td>',text.read())
for t in titles:
	c.execute('''INSERT INTO City (cityname)
	VALUES (%s)
	''',(str(t[2]),))
	db.commit()
