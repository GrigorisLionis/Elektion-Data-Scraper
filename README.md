# Election-Data-Scraper
Simple scraper for greek parliamentary election data from the official web site (https://ekloges.ypes.gr/)  
As  gioiliop7   suggested there is an API for scraping some of the data.  
The older python scipt using headless selenium is also included.  
The code consists of a  python script for downloading the election data, and saving them to a JSON file as a dictionary  
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
## Older elections - TBI
The scaper with minimal changes should be able to also read the 2019 elections as is.  
There are two problems
* division into municipalities and districts is not constant
* parties come and go

The first problem is easier to solve.The are in the main site stat data (names etc), it is relatively easy to parse them and reconstruct votes for previous elections as well.  
The second problem is more difficult, as an online source has not yet identified

