from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

locations = {
    'Moorpark College' : {
        'address': '7075 Campus Rd, Moorpark, CA 93021',
        'days': 'M-F',
        'hours': '10am-7pm', 
        'appointment' : False,
        'wait' : 24,
        'update': '13:30',
        'phone': None
    },
    'Filmore Family Medical Group' : {
        'address': '828 W Ventura St, Fillmore, CA 93015', 
        'days': 'Tuesday',
        'hours': '9am-4pm', 
        'appointment' : False,
        'wait' : 24,
        'update': '13:30',
        'phone': None
    },
    'Santa Paula' :  {
        'address': None, 
        'days': 'F-T',
        'hours': '10am-7pm', 
        'appointment' : False,
        'wait' : 24,
        'update': '13:30',
        'phone': None
    },
    'Academic Family Medicine Center' : {
        'address': '300 Hillmont Ave, Ventura, CA 93003', 
        'days': None,
        'hours': None,  
        'appointment' : True,
        'wait' : 24,
        'update': '13:30',
        'phone': '805-652-7660'
    },
    'Ventura County Fairgrounds' : {
        'address': 'W Harbor Blvd, Ventura CA 93001',
        'days': 'M-F',
        'hours': '9am-6pm',  
        'appointment' : False,
        'wait' : 24,
        'update': '13:30',
        'phone': None
    },
    'Magnolia Family Medical Center' : {
        'address': '2240 E Gonzales Rd, Oxnard, CA 9036', 
        'days': None,
        'hours': None, 
        'appointment': True,
        'wait' : 24,
        'update': '13:30',
        'phone': '805-652-7660'
        }

class Locations(Resource):
    def get(self, location_id):
        return {location_id: loactions[location_id]}

    def put(self, location_id):
        locations[location_id] = request.form['data']
        return {location_id: locations[location_id]}

api.add_resource(Locations, '/<string:location_id>') 

if __name__ == '__main__':
    app.run(debug=True)


