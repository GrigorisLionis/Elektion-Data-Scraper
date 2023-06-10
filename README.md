# Election-Data-Scraper
Simple scraper for greek parliamentary election data from the official web site (https://ekloges.ypes.gr/)  
There does not seem to be an API for providing the data, nor a JSON scheme, so a selenium approach was deemed necessary.
The scaper use selenium and a simple pattern recognition to scape district level election data.  
Robots.txt for the website was not located.  
An -almost- tidy format is produced.    
Ενας απλός scraper για τα αποτελέσματα των εκλογών του 2023. Λειτουργεί σε επίπεδο περιφέρειας
## Finer - grained data
The same  scaper could be also used for scraping municipality level election data.  
The format is more or less the same  
Furthermore, the same web page is also used for presenting older data
### Changes necessary for finer data 
* for municipality data the votes are presented inside a div class of type
"w-24 text-right pl-3 mr-3 md:mr-6" instead of "w-24 text-right pl-3" which is used for district level data
* the district file should be parsed to find municipality numbering
## Output 
The output of the scraper is also given.
The file perifereies.csv contains votes for all parties, for all districts.     
CSV αρχείο με τα αποτελέσματα των εκλογών του Μαίου 2023 για όλες τις περιφέρειες και όλα τα κόμματα.  
The  file has four columns
* District name (in Greek)
* Party name or Code  (in Greek) ( Code could be ΕΓΓΕΓΡΑΜΜΕΝΟΙ=REGISTERED, ΑΚΥΡΑ=INVALD, ΛΕΥΚΑ=WHITE,ΕΓΚΥΡΑ=VALID,ΣΥΜΜΕΤΟΧΗ=VOTERS THAT VOTED
* Number of votes for May 2023
* Number of votes for 2019
## Possible problems
The number of voters that actually voted in each district, the number of invalid and white ballots
is computed from percentages. There might be a small discrepancy
## Bug - ToDo
* A time out for loading the page, since some pages are considered invalid. 
* and a better isValid test  
* Scarping older election data
* Add checks on the data to verify correctnes (i.e. sum of votes)
