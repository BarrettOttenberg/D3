from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import pandas as pd
import numpy as np


engine = create_engine('sqlite:///../../resources/database/hawaii.sqlite')

Base = automap_base()
Base.prepare(engine=engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(bind=engine)


app = Flask(__name__)


@app.route("/")
def index():
    return (
        "Welcome to the official Hawaii Vacation Analysis and Planning Site!<br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/&lt;start&gt;<br/>"
        "/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )


@app.route("/api/v1.0/precipitation")
def preciptation():
    """
    - Query for the dates and precipitation from the last year.
    - Convert the query results to a Dictionary using date as the key and prcp as the value.
    - Return the json representation of your dictionary.
    """
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-01', Measurement.date <= '2017-08-31').all()
    dic = pd.DataFrame(results).set_index('date').rename(columns={'prcp': 'precipitation'}).to_dict()

    return jsonify(dic)


@app.route("/api/v1.0/stations")
def stations():
    """
    - Return a json list of stations from the dataset.
    """
    results = list(np.ravel(session.query(Station.station).all()))

    return jsonify(results)


@app.route("/api/v1.0/tobs")
def tobs():
    """
    - Return a json list of Temperature Observations (tobs) for the previous year.
    """
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2016-08-01', Measurement.date <= '2017-08-31').all()
    dic = pd.DataFrame(results).set_index('date').rename(columns={'tobs': 'temperature_observations'})
    dic.temperature_observations = dic.temperature_observations.astype(float)
    dic = dic.to_dict()

    return jsonify(dic)


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temps(start, end='2017-08-23'):
    """
    - Return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    - When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    - When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    """
    def calc_temps(start_date, end_date):
        results = session.query(Measurement.tobs).filter(Measurement.date >= start_date, Measurement.date <= end_date).all()
        results_ra = np.ravel(results)

        minimum = np.min(results_ra)
        average = np.average(results_ra)
        maximum = np.max(results_ra)
        return minimum, average, maximum

    minimum, average, maximum = calc_temps(start, end)
    dic = {"temp_minimum": minimum.astype(float), "temp_average": average.astype(float), "temp_maximum": maximum.astype(float)}
    return jsonify(dic)


if __name__ == '__main__':
    app.run(debug=False)