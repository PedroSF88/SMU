from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///C:\\Users\\floPe\\OneDrive\\Desktop\\SMU\\SMU-DAL-DATA-PT-08-2019-U-C\\02-Homework\\10-Advanced-Data-Storage-and-Retrieval\\Instructions\\Resources\\hawaii.sqlite")
# new model
Base = automap_base()
Base.prepare(engine, reflect=True)

#Save reference to table
Measurement = Base.classes.measurement
Station = Base.classes.station

session= Session(engine)



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route('/')
def home():
   return(
    "<h1>Home page</h1><br>"
    "<br>"
    "<br>"

    "/api/v1.0/precipitation <br>"
    "Dictionary of date as the key and prcp the value <br>"
    "<br>"
    "<br>"
    


    "/api/v1.0/stations <br>"
    "List of station <br>"
    "<br>"
    "<br>"

    "/api/v1.0/tobs <br>"
    "query for the dates and temperature observations from a year from the last data point. <br>"
    '<br>'
    "<br>"
    "/api/v1.0/precipitation/[start_date]/ <br>"
    "query for the dates and temperature observations from the date <br>"
    "or <br>"
    "/api/v1.0/precipitation/[start_date]/[end_date]<br>"
    "query for the dates and temperature observations between the dates")

@app.route('/api/v1.0/stations')
def get_stations():
    conn = engine.connect()
    stationAll = """
                    SELECT
                        *
                    FROM
                        station
                """
    df = pd.read_sql(stationAll, conn)
    return jsonify(df.to_json())
        


@app.route('/api/v1.0/tobs')
def get_tobs():
    conn = engine.connect()
    dateQuery = """
            SELECT
                MAX(date)
            FROM
                measurement
            """
    endDate = engine.execute(dateQuery).fetchall()[0][0]
    endDate = dt.datetime.fromisoformat(endDate).date()
    startDate = endDate  - dt.timedelta(days=365)
    precipENDYR = f"""
                SELECT
                    date,
                    prcp
                FROM
                    measurement
                WHERE
                    date > '{startDate}'
                    AND date <= '{endDate}'
                """
    df = pd.read_sql(precipENDYR, conn)
    return jsonify(df.to_json())



@app.route("/api/v1.0/precipitation")
def get_precipitation():
    conn = engine.connect()

    precipQuery = f"""
                SELECT
                    date,
                    prcp
                FROM
                    measurement
                """

    df = pd.read_sql(precipQuery, conn)
    return jsonify(df.to_json())

@app.route("/api/v1.0/precipitation/<start_date>/<end_date>")
def get_precipitationDates(start_date,end_date):
    conn = engine.connect()

    precipQuery = f"""
                SELECT
                    date,
                    prcp
                FROM
                    measurement
                WHERE 
                    date > '{start_date}'
                    AND date<= '{end_date}'
                """

    df = pd.read_sql(precipQuery, conn)
    return jsonify(df.to_json())
if __name__ == "__main__":
    app.run(debug=True)
