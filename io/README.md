[Community Data](/community-data/)

# Our Zip Pipeline

Also see our [industry naics zip pipeline](/community-data/process/naics/).

File name format: zip/US/NY/US-NY-zip-2023.csv


## Geonames International Postal Data

[Geonames postal code data sources](https://www.geonames.org/datasources/)  
[Midwire](https://github.com/midwire/free_zipcode_data) pulls data from geonames (but it's not a Python library).
 

## USZipcode python library

We used this for the data displayed to the right.

Data Source: [data.census.gov](https://data.census.gov) crawled by [uszipcode](https://uszipcode.readthedocs.io/).

Run the following in the "io" folder to initiate a virtual environment folder called env (optional, may differ on PC). On some machines, run "python" rather than "python3"  

	python3 -m venv env &&
	source env/bin/activate

Load the zip data into an object

	pip install uszipcode

To generate a .json file for each zip code, run in the current folder.
Output is stored in nested folders in the format: zip/io/data/3/0/3/1/8

	python3 generatezip.py

Contribute to our "[zip/io](https://github.com/modelearth/zip/tree/master/io)" folder at: [github.com/modelearth/zip](https://github.com/modelearth/zip)  
Our fork extends the work of [uszipcode.readthedocs.io](https://uszipcode.readthedocs.io/)  


**Processing Note**

Update Feb 16, 2024 - Better data, but Puerto Rico (example zip 00606) population became none. The zip/io/data folder is now 4.27 GB. It was previously 4.41 GB.
The smaller size is thanks rounding more digits, and using numbers (0 to 7) rather than strings to convey Head of Households and Population by Age.

The 450+ MB data file is downloaded automatically when in cluding the parameter SearchEngine(simple_or_comprehensive=SearchEngine.SimpleOrComprehensiveArgEnum.comprehensive). Older examples used SearchEngine(simple_zipcode=False) which produced the AttributeError: 'SearchEngine' object has no attribute 'ses'.

You can download the [zip SQLite file](https://github.com/MacHu-GWU/uszipcode-project/releases/download/1.0.1.db/comprehensive_db.sqlite) independently. 

Without a parameter in SearchEngine() fewer detail fields are generated. Population by year is gone in .md file.
Polygon is gone in .json file.

Avoid deploying data update until fixed.

Date for Grand Rapids zip 49501 is still not generated.



## Address Lookup

We're not using the following currently. Primarily useful for address validation lookups and Machine Learning about the built environment.

[OpenAddresses](https://opencollective.com/openaddresses) - All the world's addresses and building footprints.
[Geopy](https://geopy.readthedocs.io) - international postal code Python library.
[PyGeocoder](https://www.google.com/search?q=PyGeocoder) - Uses Google's geolocation API for address lookup.
