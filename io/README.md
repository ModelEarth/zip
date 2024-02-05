[Community Data](/community-data/)

# Our Zip Pipeline

Also see our [industry naics zip pipeline](/community-data/process/naics/).

File name format: zip/US/NY/US-NY-zip-2023.csv

## Geopy

Gary is investigating the Geopy international postal code Python library.

[geopy.readthedocs.io](https://geopy.readthedocs.io)

## PyGeocoder

Might use PyGeocoder also - Google API, might include Yahoo data
Gary is also investigating PyGeocoder

## Geonames International Postal Data

[Geonames postal code data sources](https://www.geonames.org/datasources/)  
[Midwire](https://github.com/midwire/free_zipcode_data) pulls data from geonames (but it's not a Python library).
 

## USZipcode python library

We used this for the data displayed to the right.

Data Source: [data.census.gov](https://data.census.gov) crawled by [uszipcode](https://uszipcode.readthedocs.io/).

Initiate a virtual environment folder called env (optional, may differ on PC). On some machines, run "python" rather than "python3"  

	python3 -m venv env
	source env/bin/activate

Load the zip data into an object

	pip install uszipcode

To generate a .json file for each zip code, run in the current folder.
Output is stored in nested folders in the format: zip/io/data/3/0/3/1/8

	python3 generatezip.py

Contribute to our "[zip/io](https://github.com/modelearth/zip/tree/master/io)" folder at: [github.com/modelearth/zip](https://github.com/modelearth/zip)  
Our fork extends the work of [uszipcode.readthedocs.io](https://uszipcode.readthedocs.io/)  


**Problem**
Changed SearchEngine(simple_zipcode=False) to SearchEngine() to resolve error.
(See hidden comment below)

Now fewer detail fields are generated. Population by year is gone in .md file.
Polygon is gone in .json file.

Avoid deploying data update until fixed.

Date for Grand Rapids zip 49501 is still not generated.

<!-- 
Fixed error below by changing SearchEngine(simple_zipcode=False) to SearchEngine()

Katherine W. ran successfully in 2021, but L.H. ran into the following on his Mac in Feb 2022:  

File "/Users/helix/Library/Data/zip/env/lib/python3.8/site-packages/uszipcode/search.py", line 195, in __del__
    if self.ses:
AttributeError: 'SearchEngine' object has no attribute 'ses'
Traceback (most recent call last):
  File "generatezip.py", line 105, in <module>
    main()
  File "generatezip.py", line 12, in main
    search = SearchEngine(simple_zipcode=False)
TypeError: __init__() got an unexpected keyword argument 'simple_zipcode'
(env) (base) helix@localhost io % python generatezip.py
-->