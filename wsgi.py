from flask import Flask, render_template, redirect, url_for, request, json, session, escape, flash
from passlib.hash import sha256_crypt
import MySQLdb
import requests
import re

application=Flask(__name__)
application.secret_key = 'Valar Morghulis'

application.config['MYSQL_USER'] = 'root'
application.config['MYSQL_PASSWORD'] = '2312onnf'
application.config['MYSQL_DB'] = 'Users'
application.config['MYSQL_HOST'] = 'localhost'
db=MySQLdb.connect(user="root",passwd="2312onnf",db="Users")

c=db.cursor()
citylist2 = []
c.execute('''SELECT cityname FROM City''')
citylist = re.findall(r"\'([A-Za-z]+)\'",str(c.fetchall()))

def weatherdata(citylist):
	weatherlist = []
	for city in citylist:
		r = requests.get("http://api.wunderground.com/api/39f7c55a8cddcff3/conditions/q/India/"+str(city)+".json")
		data = r.json()
		weather = {}
		c=db.cursor()
		c.execute('''SELECT cid FROM City WHERE cityname = %s''',(city,))
		cid= re.findall(r"([0-9]+)",str(c.fetchone()))
		weather['cid'] = cid[0]
		weather['Location'] = data['current_observation']['display_location']['city']
		weather['Weather'] = data['current_observation']['weather']
		weather['Current_Temp'] = data['current_observation']['temperature_string']
		weather['Feels_Like_Temp'] = data['current_observation']['feelslike_string']
		weather['icon'] = data['current_observation']['icon_url']
		weatherlist.append(weather.copy())
	return weatherlist
	
def weatherupdate():
	c=db.cursor()
	c.execute('''SELECT DISTINCT cid FROM Usercity''')
	cities = re.findall(r"([0-9]+)",str(c.fetchall()))
	citylist3 = []
	for city in cities:
		c.execute('''SELECT cityname FROM City
		WHERE cid = %s''',(city,))
		citylist2 = re.findall(r"\'([A-Za-z]+)\'",str(c.fetchall()))
		citylist3.append(citylist2)
	citylist4 = re.findall(r"\'([A-Za-z]+)\'",str(citylist3))
	weatherlist = weatherdata(citylist4)
	for weather in weatherlist:
		c.execute('''INSERT INTO Cityweather ( cid, location, weather, currenttemp, feelstemp, icon ) VALUES ( %s, %s, %s, %s, %s, %s )''',
		(int(weather['cid']),weather['Location'],weather['Weather'],weather['Current_Temp'],weather['Feels_Like_Temp'],weather['icon'],))
		db.commit()

weatherupdate()

def weatherdb(cidlist):
	db_weatherlist =[]
	c=db.cursor()
	for cid in cidlist:
		c.execute('''SELECT * FROM Cityweather WHERE cid = %s''',(cid,))
		weather = {}
		wearr = c.fetchone()
		weather['cid'] = wearr[0]
		weather['Location'] = wearr[1]
		weather['Weather'] = wearr[2]
		weather['Current_Temp'] = wearr[3]
		weather['Feels_Like_Temp'] = wearr[4]
		weather['icon'] = wearr[5]
		db_weatherlist.append(weather.copy())
	return db_weatherlist

@application.route('/')
@application.route('/homepage')
def homepage():
	return render_template('homepage.html')

@application.route('/removeCity', methods=['POST', 'GET'])
def removeCity():
	if 'username' in session:
		username_session = escape(session['username'])
		if request.method == 'GET':
			city = request.args.get('UserCity')
		elif request.method == 'POST':
			city = request.form['UserCity']
		else:
			city = request.form['UserCity']
		c=db.cursor()
		c.execute('''SELECT uid FROM User
		WHERE username = %s
		''',(username_session,))
		uid_session = c.fetchone()
		c.execute('''SELECT cid FROM City
		WHERE cityname = %s
		''',(city,))
		cid = c.fetchone()
		c.execute('''SELECT * FROM Usercity
		WHERE uid = %s AND cid = %s
		''',(uid_session,cid))
		exist = c.fetchall()
		if exist:
			c.execute('''DELETE FROM Usercity
			WHERE uid = %s AND cid = %s
			''',(uid_session,cid))
			db.commit()
			flash('City deleted successfully')
			return render_template('userhome.html',session_user_name = username_session, citylist = citylist)
		else:
			flash('City not present in your favourites')
			return render_template('userhome.html',session_user_name = username_session, citylist = citylist)

@application.route('/addCity', methods=['POST', 'GET'])
def addCity():
	if 'username' in session:
		username_session = escape(session['username'])
		if request.method == 'GET':
			city = request.args.get('UserCity')
		elif request.method == 'POST':
			city = request.form['UserCity']
		else:
			city = request.form['UserCity']
#		if request.method == 'POST':
#			city = request.form['City']
		c=db.cursor()
		c.execute('''SELECT uid FROM User
		WHERE username = %s
		''',(username_session,))
		uid_session = c.fetchone()
		c.execute('''SELECT cid FROM City
		WHERE cityname = %s
		''',(city,))
		cid = c.fetchone()
		c.execute('''INSERT INTO Usercity
		(uid , cid)
		VALUES (%s , %s)
		''',(uid_session,cid))
		db.commit()
		return render_template('userhome.html',session_user_name=username_session,citylist = citylist)

@application.route('/login')
def login():
	return render_template('loginpage.html')

@application.route('/logout')
def logout():
	session['logged_in'] = False
	session.pop('username', None)
	session.pop('uid', None)
	return render_template('homepage.html')

@application.route('/register')
def register():
	return render_template('registerpage.html')

@application.route('/userHome')
def userhome():
	if 'username' in session:
		username_session = escape(session['username'])
		return render_template('userhome.html',session_user_name=username_session,citylist = citylist)
	return render_template('login.html')

@application.route('/checkWeather', methods=['POST', 'GET'])
def checkWeather():
	if 'username' in session:
		username_session = escape(session['username'])
		c=db.cursor()
		c.execute('''SELECT uid FROM User
		WHERE username = %s
		''',(username_session,))
		uid_session = c.fetchone()		
		clist2 = []
		c.execute('''SELECT cid FROM Usercity WHERE uid = %s''',(uid_session,))
		user_cidlist = re.findall(r"([0-9]+)",str(c.fetchall()))
		c.execute('''SELECT cid FROM Cityweather''')
		db_cidlist = re.findall(r"([0-9]+)",str(c.fetchall()))
		cidlist = list(set(user_cidlist).intersection(set(db_cidlist)))
		cidrem = list(set(user_cidlist)-set(cidlist))
		
		db_weatherlist = weatherdb(cidlist)
		
		for cid in cidrem:
			c.execute('''SELECT cityname FROM City WHERE cid = %s''',(cid,))
			clist2.append(str(c.fetchone()))
		clist3 = re.findall(r"\'([A-Za-z]+)\'",str(clist2))
		
		api_weatherlist = weatherdata(clist3)
		
		return render_template('userweatherdata.html',session_user_name = username_session,api_weatherlist = api_weatherlist, db_weatherlist = db_weatherlist)

@application.route('/signUp', methods=['POST', 'GET'])
def signUp():
	if request.method == 'POST':
		username = request.form['UserName']
		password = sha256_crypt.encrypt(str(request.form['Password']))
	else:
		username = request.args.get('UserName')
		password = sha256_crypt.encrypt(str(request.args.get('Password')))
		
	if username and password:
		c=db.cursor()
		c.execute("SELECT COUNT(1) FROM User WHERE username = %s;",(username,))
		if c.fetchone()[0]:
			flash("User Exists Already")
			return redirect('/register')
		else:
				c.execute('''
				INSERT INTO User (username, password)
				VALUES (%s, %s)
				''',(str(username), str(password)))
				db.commit()
				flash("User Created!")
				c.execute('''SELECT uid FROM User WHERE username = %s
				''',(username,))
				uid = c.fetchone()
				session['logged_in'] = True
				session['username'] = username
				session['uid'] = uid
				return redirect('/userHome')
	else:
		return json.dumps({'html':'<span>Enter the required fields</span>'})

@application.route("/Authenticate", methods=['POST'])
def Authenticate():
	username = request.form['UserName']
	password = request.form['Password']
	c=db.cursor()
	c.execute("SELECT COUNT(1) FROM User WHERE username = %s;",(username,))		
	if c.fetchone()[0]:
		c.execute("SELECT password FROM User WHERE username = %s;",(username,))
		for row in c.fetchall():
			if sha256_crypt.verify(password,row[0]):
				session['logged_in'] = True
				c.execute('''SELECT uid FROM User WHERE username = %s
				''',(username,))
				uid = c.fetchone()
				session['username'] = username
				session['uid'] = uid
				return redirect('/userHome')
			else:
				return json.dumps({'html':'<span>Wrong user id or Password.</span>'})
	else:
			return json.dumps({'html':'<span>Wrong user id or Password.</span>'})

if __name__=='__main__':
	application.run()
