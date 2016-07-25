#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 1.50,
        "currency": "$",
        "title": "Energy Consumption",
        "actual_consumption": 1000.00,
        "uom": "Watt",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_energy.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 1.60,
        "currency": "$",
        "title": "Energy Production",
        "actual_consumption": 2000.00,
        "uom": "Watt",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_solar_energy.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 1.70,
        "currency": "$",
        "title": "Water Consumption",
        "actual_consumption": 3000.00,
        "uom": "m3",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_water.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 1.80,
        "currency": "$",
        "title": "Gas Consumption",
        "actual_consumption": 4000.00,
        "uom": "smc",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_gas.png",
    }
]

aggregate = [
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "day": [{"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00}],
        "week": [{"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00}, ],
        "month": [{"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                  {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00}, ],
        "year": [{"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00},
                 {"Timestamp": "2016-02-13T18:15:39.563Z+0200", "value": 1000.00}, ],
        "actual_consumption": 1000.00,
        "min_consumption_range": 20.00,
        "max_consumption_range": 1500.00,
        "uom_consumption": "Watt",
        "actual_co2_production": 2.3,
        "uom_co2_production": "Kg"
    }
]

details = [
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.00,
        "currency": "$",
        "title": "Bravo Ale",
        "actual_consumption": 1000.00,
        "uom": "Watt",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_energy.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.20,
        "currency": "$",
        "title": "Energy Production",
        "actual_consumption": 2000.00,
        "uom": "Watt",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_solar_energy.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.40,
        "currency": "$",
        "title": "Water Consumption",
        "actual_consumption": 3000.00,
        "uom": "m3",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_water.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.60,
        "currency": "$",
        "title": "Gas Consumption",
        "actual_consumption": 4000.00,
        "uom": "smc",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_gas.png",
    }
]

details_ec = [
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.00,
        "currency": "$",
        "title": "CAZZO FUNZIONA EC",
        "actual_consumption": 1000.00,
        "uom": "Watt",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_energy.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.20,
        "currency": "$",
        "title": "Energy Production",
        "actual_consumption": 2000.00,
        "uom": "Watt",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_solar_energy.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.40,
        "currency": "$",
        "title": "Water Consumption",
        "actual_consumption": 3000.00,
        "uom": "m3",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_water.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.60,
        "currency": "$",
        "title": "Gas Consumption",
        "actual_consumption": 4000.00,
        "uom": "smc",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_gas.png",
    }
]

details_ep = [
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.00,
        "currency": "$",
        "title": "CAZZO FUNZIONA EP",
        "actual_consumption": 1000.00,
        "uom": "Watt",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_energy.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.20,
        "currency": "$",
        "title": "Energy Production",
        "actual_consumption": 2000.00,
        "uom": "Watt",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_solar_energy.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.40,
        "currency": "$",
        "title": "Water Consumption",
        "actual_consumption": 3000.00,
        "uom": "m3",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_water.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.60,
        "currency": "$",
        "title": "Gas Consumption",
        "actual_consumption": 4000.00,
        "uom": "smc",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_gas.png",
    }
]

details_wc = [
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.00,
        "currency": "$",
        "title": "CAZZO FUNZIONA WC",
        "actual_consumption": 1000.00,
        "uom": "Watt",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_energy.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.20,
        "currency": "$",
        "title": "Energy Production",
        "actual_consumption": 2000.00,
        "uom": "Watt",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_solar_energy.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.40,
        "currency": "$",
        "title": "Water Consumption",
        "actual_consumption": 3000.00,
        "uom": "m3",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_water.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.60,
        "currency": "$",
        "title": "Gas Consumption",
        "actual_consumption": 4000.00,
        "uom": "smc",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_gas.png",
    }
]

details_gc = [
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.00,
        "currency": "$",
        "title": "CAZZO FUNZIONA GC",
        "actual_consumption": 1000.00,
        "uom": "Watt",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_energy.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.20,
        "currency": "$",
        "title": "Energy Production",
        "actual_consumption": 2000.00,
        "uom": "Watt",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_solar_energy.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.40,
        "currency": "$",
        "title": "Water Consumption",
        "actual_consumption": 3000.00,
        "uom": "m3",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_water.png",
    },
    {
        "user_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "hw_id": "8cbab44a-5ab0-4eef-8c7d-16ca7398f8ac",
        "price": 3.60,
        "currency": "$",
        "title": "Gas Consumption",
        "actual_consumption": 4000.00,
        "uom": "smc",
        "icon": "http://flexmeter.polito.it/wp-content/uploads/2016/07/icon_gas.png",
    }
]

@app.route('/measurements', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/measurements/aggregate', methods=['GET'])
def get_aggregate():
    return jsonify({'aggregate': aggregate})


@app.route('/measurements/details', methods=['GET'])
def get_details():
    return jsonify({'details': details})


@app.route('/measurements/details/ec', methods=['GET'])
def get_details_ec():
    return jsonify({'details_ec': details_ec})


@app.route('/measurements/details/ep', methods=['GET'])
def get_details_ep():
    return jsonify({'details_ep': details_ep})


@app.route('/measurements/details/wc', methods=['GET'])
def get_details_wc():
    return jsonify({'details_wc': details_wc})


@app.route('/measurements/details/gc', methods=['GET'])
def get_details_gc():
    return jsonify({'details_gc': details_gc})

if __name__ == '__main__':
    app.run(host='130.192.163.22', debug=True,
            threaded=True)                                                                                                                                                                                                                            
