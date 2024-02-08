# sqlalchemy-challenge

### Climate Analysis and Data Exploration of Hawaii

This project utilizes Python and SQLAlchemy to perform climate analysis and data exploration of the Hawaii climate database. Specifically, SQLAlchemy ORM queries, Pandas, and Matplotlib are employed.

## Part 1: Analyze and Explore the Climate Data

In the first part of the project, the following steps were taken:

    Connect to the SQLite database using SQLAlchemy's create_engine() function.
    Reflect tables into classes using SQLAlchemy's automap_base() function and save references to the classes named Station and Measurement.
    Link Python to the database by creating a SQLAlchemy session.

# Precipitation Analysis

For precipitation analysis:

    The most recent date in the dataset was found.
    This date was used to retrieve the previous 12 months of precipitation data by querying the database.
    The date and precipitation data were loaded into a Pandas DataFrame.
    Summary statistics for the precipitation data were calculated using Pandas.
    The results were plotted using Matplotlib.

Station Analysis

For station analysis:

    A query was designed to calculate the total number of stations in the dataset and identify the most active stations in descending order.
    The ID of the most active station was used to design a query to calculate the lowest, highest, and average temperatures.
    Another query was designed to retrieve the previous 12 months of temperature observation data, and the results were plotted as a histogram.

Part 2: Design the Climate App

For the second part of the project, a Flask API was designed based on the queries developed in the first part. The following routes were created:

    /: Homepage. Lists all the available routes.
    /api/v1.0/precipitation1617: Converts the query results from the precipitation analysis of 2016-2017 to a dictionary using date as the key and precipitation as the value. Returns the JSON representation of the dictionary.
    /api/v1.0/stations: Returns a JSON list of stations from the dataset.
    /api/v1.0/tobs: Queries the dates and temperature observations of the most active station for the previous year of data. Returns a JSON list of temperature observations for the previous year.
    /api/v1.0/yyyy-mm-dd: For a specified start date, calculates TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date to the most recent date. Returns a JSON list.
    /api/v1.0/yyyy-mm-dd/yyyy-mm-dd: Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

References

    Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910. Link
