# Import the dependencies.
from flask import Flask, jsonify
import numpy as np

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def Homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/><br/>"
        f"Precipitation from 2016/8/24 to 2017/8/24:<br/> /api/v1.0/precipitation1617<br/><br/>"
        f"Stations:<br/> /api/v1.0/stations<br/><br/>"
        f"Temperature  year of station 'USC00519281' :<br/> /api/v1.0/tobs<br/><br/>"
        f"Temperature stat from a specific date:<br/> /api/v1.0/yyyy-mm-dd<br/><br/>"
        f"Temperature stat from a specific period:<br/> /api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/><br/>"
        f"Temperature and Precipitation stat from a specific period for a specific station: <br/>example: /api/v1.0/USC00513117/2010-03-22/2014-03-22<br/>"
        f"/api/v1.0/station_ID/yyyy-mm-dd/yyyy-mm-dd"
    )

@app.route("/api/v1.0/precipitation1617")

def Precipitation():
    precipitation_info = session.query(Measurement.date,Measurement.prcp).\
    filter(Measurement.date >= '2016-08-24').\
    order_by(Measurement.date).all()

    session.close()

    precipitation = []
    precipitation = {date: prcp for date, prcp in precipitation_info}

    return jsonify(precipitation)



@app.route("/api/v1.0/stations")
def All_Stations():
    station_join = session.query(Station,Measurement).\
    join(Station,Measurement.station == Station.station).\
    group_by(Measurement.station).all()

    Station_list = []
    for record in station_join:
        (station, measurement) = record
        Station_dict = {}
        Station_dict['Station_id'] = station.station
        Station_dict["name"] = station.name
        Station_dict["lat"] = station.latitude
        Station_dict["long"] = station.longitude
        Station_dict["elevation"] = station.elevation
        Station_list.append(Station_dict)
    

    return jsonify(Station_list)

@app.route("/api/v1.0/tobs")
def Temperature_info():
    most_active_station = 'USC00519281'
    sel = [Measurement.date,Measurement.prcp]
    year_T_info = session.query(*sel).\
    filter(Measurement.station== most_active_station).\
    filter(Measurement.date >= '2016-08-23').\
    order_by(Measurement.date).all()

    Temperature = []
    for date, prcp in year_T_info:
            Temperature_dict = {}
            Temperature_dict["name"] = most_active_station
            Temperature_dict["Date"] = date
            Temperature_dict["Precipitation"] = prcp
            Temperature.append(Temperature_dict)

    return jsonify(Temperature)

@app.route("/api/v1.0/<start_date>")
def period_start(start_date):
    sel = [func.min(Measurement.tobs),
       func.max(Measurement.tobs),
       func.avg(Measurement.tobs)]
    year_start_info = session.query(*sel).\
    filter(Measurement.date >= start_date).all()

    Temperature_start = []
    for min, max, avg in year_start_info:
            Temperature_dict = {}
            Temperature_dict["Min_temp"] = min
            Temperature_dict["Max_temp"] = max
            Temperature_dict["Avg_temp"] = avg
            Temperature_start.append(Temperature_dict)

    return jsonify(Temperature_start)

@app.route("/api/v1.0/<start_date>/<end_date>")
def period_info(start_date, end_date):
    sel = [func.min(Measurement.tobs),
       func.max(Measurement.tobs),
       func.avg(Measurement.tobs)]
    year_T_info = session.query(*sel).\
    filter(Measurement.date >= start_date).\
    filter(Measurement.date <= end_date).all()

    Period_info = []
    for min, max, avg in year_T_info:
            Temperature_dict = {}
            Temperature_dict["Min_temp"] = min
            Temperature_dict["Max_temp"] = max
            Temperature_dict["Avg_temp"] = avg
            Period_info.append(Temperature_dict)

    return jsonify(Period_info)

@app.route("/api/v1.0/<station>/<start_date>/<end_date>")
def period_station_info(start_date, end_date,station):
    sel = [func.min(Measurement.tobs),
       func.max(Measurement.tobs),
       func.avg(Measurement.tobs),
       func.min(Measurement.prcp),
       func.max(Measurement.prcp),
       func.avg(Measurement.prcp)]
    year_T_info = session.query(*sel).\
    filter(Measurement.date >= start_date).\
    filter(Measurement.date <= end_date).\
    filter(Measurement.station == station).all()

    Period_station_info = []
    for min_t, max_t, avg_t,min_p, max_p, avg_p  in year_T_info:
            Temperature_dict = {}
            Temperature_dict["Station name"] = station
            Temperature_dict["Min_temp"] = min_t
            Temperature_dict["Max_temp"] = max_t
            Temperature_dict["Avg_temp"] = avg_t
            Temperature_dict["Min_precipitation"] = min_p
            Temperature_dict["Max_precipitation"] = max_p
            Temperature_dict["Avg_precipitation"] = avg_p
            Period_station_info.append(Temperature_dict)

    return jsonify(Period_station_info)

if __name__ == "__main__":
    app.run(debug=True)