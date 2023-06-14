# Election-Data-Scraper
Simple scraper for greek parliamentary election data from the official web site (https://ekloges.ypes.gr/)  
As  gioiliop7   suggested there is an API for scraping some of the data.  
Implemeted a python script for downloading the election data, and saving them to a JSON file as a dictionary  
A second script -exportcsv.py- reads the JSON files and exports data to csv
## Usage
* ekloges_parser_json.py is run, probably more than one time, to download all data into two JSON files
* exportscv.py reads the two JSON files and outputs csv
## Output
A csv file with election data for the 2023 May elections is included  
The file has 7 columns
* Date
* String identification of whether the data is MUNICIPALITY of DISTRICT
* name of MUNICIPALITY or DISTRICT (in greek)
* String DISTRICT (could be ommited)
* String whith the district name in which "name" belongs
* party/code name (codes are LEFKA/AKYRA/GRAMMENOI/EGYRA correspondig to WHITE/INVALID/REGISTERED/VALID)
* number of votes

