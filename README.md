#  Climate Analysis and Data Exploration of Hawaii 

In this project, I used Python and SQLAlchemy to perform climate analysis and data exploration of the Hawaii climate database. Specifically, SQLAlchemy ORM queries, Pandas, and Matplotlib are employed.

##  Part 1: Analyze and Explore the Climate Data 

In the first part of the project, I used the following steps:

1.	Employed the SQLAlchemy create_engine() function to connect to the SQLite database.
2.	Employed the SQLAlchemy automap_base() function to reflect tables into classes and then saved references to the classes named Station and Measurement.
3.	Linked Python to the database by creating a SQLAlchemy session.


###  Precipitation Analysis 

For precipitation analysis, I found the most recent date in the dataset and I used this date to get the previous 12 months of precipitation data by querying the previous 12 months from the dataset. After selecting the date and precipitation data I load the query into a Pandas DataFrame and plot the results by using the DataFrame plot method, as the following image shows:

![Precipitation_analysis](https://github.com/MarcoN16/sqlalchemy-challenge/assets/150491559/968e485f-e4ca-4762-ab4a-b34476317921)

I used Pandas to calculate the summary statistics for the precipitation data. 

###  Station Analysis 

For the station analysis, I designed a query to calculate the total number of stations in the dataset and identified the most active stations, listing them in descending order. Using the ID of the most active station, I then designed a query to calculate the lowest, highest, and average temperatures recorded. Finally, I formulated a query to retrieve the previous 12 months of temperature observation data for the most active station and plotted the results as a histogram, as depicted in the following image:

![Temperature_analysis](https://github.com/MarcoN16/sqlalchemy-challenge/assets/150491559/044a55e1-c2b6-4329-9207-e11191397edc)


## Part 2: Design the Climate App

For the second part of the project, I designed a Flask API based on the queries developed in the first part. I used Flask to create routes as follows:

1. /: Homepage. Lists all the available routes.
2. /api/v1.0/precipitation1617: Converts the query results from my precipitation analysis of 2016-2017 to a dictionary using date as the key and precipitation as the value.     Returns the JSON representation of the dictionary.
3. /api/v1.0/stations: Returns a JSON list of station ID, name, latitude, longitude, and elevation.
4. /api/v1.0/tobs: Queries the dates and temperature observations of the most active station for the previous year of data. Returns a JSON list of temperature observations     for the previous year.
5. /api/v1.0/yyyy-mm-dd: For a specified start date, calculates TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date to the most recent date.         Returns a JSON list.
6. /api/v1.0/yyyy-mm-dd/yyyy-mm-dd: Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start-end range.
7. /api/v1.0/station_ID/yyyy-mm-dd/yyyy-mm-dd: Returns a JSON list of the min, max, average of Temperature and Precipitation from a specific period and for a specific station


### References
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910. [Link](https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml) https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml
