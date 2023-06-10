# Election-Data-Scraper
Simple scraper for greek parliamentary election data from the official web site (https://ekloges.ypes.gr/)  
There does not seem to be an API for providing the data, nor a JSON scheme, so a selenium approach was deemed necessary.
The scaper use selenium and a simple pattern recognition to scape district level election data.  
An -almost- tidy format is produced.    
Ενας απλός scraper για τα αποτελέσματα των εκλογών του 2023. Λειτουργεί σε επίπεδο περιφέρειας
## Finer - grained data
The same  scaper could be also used for scraping municipality level election data.  
The format is more or less the same  
### Changes necessary for finer data 
* for municipality data the votes are presented inside a div class of type
"w-24 text-right pl-3 mr-3 md:mr-6" instead of "w-24 text-right pl-3" which is used for district level data
* the district file should be parsed to find municipality numbering
## Output 
The output of the scraper is also given.
The file perifereies.csv contains votes for all parties, for all districts.     
CSV αρχείο με τα αποτελέσματα των εκλογών του Μαίου 2023 για όλες τις περιφέρειες και όλα τα κόμματα.   
## Possible problems
The number of voters that actually voted in each district, the number of invalid and white ballots
is computed from percentages. There might be a small discrepancy
## Bug 
A time out , and a better isValid test  should be added. The initial version did not scrape cortrectly a number of districts.
