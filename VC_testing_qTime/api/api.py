import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


locations = [
	{'id': 0,
	 'location' : 'Moorpark College',
	 'address' : '7075 Campus Rd, Moorpark, CA 93021',
	 'appointment' : False,
	 'Days' : 'M-F',
 	 'Hours' : '10AM-7PM',
	 'wait_time' : 120,
	 'last_updated' : '12:20:21'}
]

@app.route('/', methods=['GET'])
def home():
	return "<h1>Ventura County Covid Drive Thru Testing</h1><p>Current wait time for Moorpark Colleg is 1 hour.</p>"
app.run()
