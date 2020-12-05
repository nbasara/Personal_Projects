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
        },
    'Oxnard performing Arts and Convention Center' : {
        'address': '800 Hobson Way, Oxnard, CA 93030',
        'days': 'M-F',
        'hours': '8am-9pm',
        'appointment': True,
        'wait': 23,
        'update': 23,
        'phone': '1-888-634-1123'
        },
    'Las Islas Family Medical Group' : {
        'address': '325 W Channel Islands Blvd, Oxnard, CA 93033',
        'days': None,
        'hours': None,
        'appointment': True,
        'wait': None,
        'update': None,
        'phone': None
        },
    'Oxnard College' : {
        'address': '4000 S Rose Ave, Oxnard, CA 93033',
        'days': 'F-T',
        'hours': '10am-7pm',
        'appointment': False,
        'wait': None,
        'update': None,
        'phone': None
        },
    'Thousand Oaksf Library - Newbury Park Branch' : {
        'address': '2331 Borchard Rd, Thousand Oaks, CA, 91320',
        'days': 'M-F',
        'hours': '8am-8pm',
        'appointment': False,
        'wait': None,
        'update': None,
        'phone': None,
        },
    'Conejo Valley Family Medical Group' : {
        'address': '125 W Thousands Oaks Blvd, Thousand Oaks, CA 91360',
        'days': None,
        'hours': None,
        'appointment': True,
        'wait': None,
        'update': None,
        'Phone': '805-652-7660'
        },
    'Sierra Vista Family Medical Clinic' : {
        'address': '1227 E Los Angeles Ave, Simi Valley, CA 93065',
        'days': None,
        'hours': None,
        'appointment': True,
        'wait': None,
        'update': None,
        'Phone': '805-652-7660'
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


