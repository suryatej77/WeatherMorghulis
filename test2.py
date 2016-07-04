from flask import Flask, render_template, redirect, url_for, request, json, session, escape, flash
from passlib.hash import sha256_crypt
import MySQLdb
import requests
import re

app=Flask(__name__)

app.secret_key = 'Valar Morghulis'

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '2312onnf'
app.config['MYSQL_DB'] = 'Users'
app.config['MYSQL_HOST'] = 'localhost'
db=MySQLdb.connect(user="root",passwd="2312onnf",db="Users")

c=db.cursor()
citylist2 = []
c.execute('''SELECT cityname FROM City''')
citylist2 = str(c.fetchall())
citylist = re.findall(r"\'([A-Za-z]+)\'",citylist2)

clist = ["Mumbai","Bangalore"]
#print (clist)
#if 'username' in session:
#		username_session = escape(session['username'])
#		uid_session  = escape(session['uid'])
#		if request.method == 'GET':
#			city = request.args.get('City','')
#		else:
#			city = request.form['City']
city = "Hyderabad"
clist2 = []
uid_session  = 0
c=db.cursor()
c.execute('''SELECT cid FROM Usercity WHERE uid = %s''',(uid_session,))
clist = c.fetchall()
for cid in clist:
	c.execute('''SELECT cityname FROM City WHERE cid = %s''',(cid,))
	clist2.append(str(c.fetchone()))
#print (clist2)
#citylist2 = str(c.fetchall())
clist3 = re.findall(r"\'([A-Za-z]+)\'",str(clist2))
#weatherlist = weatherdata(clist)
weatherlist = []
for city in clist3:
	r = requests.get("http://api.wunderground.com/api/39f7c55a8cddcff3/conditions/q/India/"+str(city)+".json")
	data = r.json()
	print (data)
	weather = {}
	#weather['Location'] = data['current_observation']['display_location']['full']
	weather['Weather'] = data['current_observation']['weather']
	weather['Current_Temp'] = data['current_observation']['temperature_string']
	weather['Feels_Like_Temp'] = data['current_observation']['feelslike_string']
	weather['icon'] = data['current_observation']['icon_url']
	weatherlist.append(weather.copy())
render_template('userweatherdata.html',session_user_name = username_session,weatherlist = weatherlist)

