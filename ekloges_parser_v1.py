from selenium import webdriver
import os
import codecs
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium_stealth import stealth
import sys



#simple web scrapper for Greek Parliament election data 
#outpouts data in almost.. tidy format
#District,Party,Votes2023May,Votes2019
#should have two entries for each for full tidy format



#open stealth chrome driver for selenium
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )






def ReadPage(link):

   driver.get(link)
   h=driver.page_source
   #print(h)
   soup = BeautifulSoup(h,features="lxml")
   #print(soup)
   chl=soup.findChildren()
   if(len(chl)==0): 
      print ("ERROR. PAGE DOES NOT EXIST",file=sys.stderr)
      return()
   af=0
   idx=1

   kommata={}
   psifoi={}
   psifoi_2019={}
   for c in chl:
      

      if (c.has_attr("title")):
       tt=c.find_all(text=True)
       
       #party name has attribte "title"
       #there are two entries for each party, the full and the small name. we keep the small
       if len(tt)>0:
          if(af==0):
               kommata[idx]=(tt[0].strip()).replace(",","-") #replace necessary jic a party has a comma in its name
          af=af+1
          if(af==2):
             idx=idx+1
             af=0




   pt=soup.find_all("div", {"class": "w-24 text-right pl-3"})
   #the results of the election are given with entries of this class type
   #the sequence is the same as the sequence of the title entries
   #we use an index idx to correspond parties to results
   #there is an offset of 1, because the first entry with this class type is the word "votes"
   
   # "w-24 text-right pl-3" shoud be replaced with  "w-24 text-right pl-3 mr-3 md:mr-6" for scrapping municipalitiy level data
   # the web layout is slightly different
        
   idx=0
   if(len(pt)==0): 
      print ("ERROR. PAGE DOES NOT EXIST",file=sys.stderr)
      return() #check if page is empty
   for p in pt:
       tt=p.find_all(text=True)
       idx=idx+1
       if(idx>1):psifoi[idx-1]=(tt[0].strip()).replace(".","")

   pt=soup.find_all("div", {"class": "hidden lg:block w-24 text-right pl-3 text-sm"})
   idx=1
   #this class type contains results of the previous elections
   for p in pt:
       tt=p.find_all(text=True)
       psifoi_2019[idx]=(tt[0].strip()).replace(".","")
       if psifoi_2019[idx]=="":psifoi_2019[idx]="0"
       idx=idx+1



   pt=soup.find("div", {"class": "truncate pb-3"})
   tt=pt.find_all(text=True)
   perif=tt[0]
   #this class type is used for the disctrict name

   #in order to locate the other info 
   #we use all the text of the screen 
   tt=soup.find_all(text=True)
   res= " ".join(map(str,tt))
   #cast it in a single string  

   ttl=res.split()
   #put the string in a list

   #and locate the words we need 
   egger=ttl[ttl.index("Εγγεγραμμένοι")+1] #number of voters registered 
   egger=egger.replace(".","")
   egger=int(egger)  #we remove the "." corresponding to thousands and cast to int


   psif=ttl[ttl.index("Συμμετοχή")+1] #percentage of people actually voted
   psif=egger*0.01*float(psif.replace(",",".")) #replace , with . as decimal point, make float, divide with 100
                                                # and multiply with registered voters

   egyr=float(ttl[ttl.index("Έγκυρα")+1].replace(",","."))*0.01*psif
   aky=float(ttl[ttl.index("Άκυρα")+1].replace(",","."))*0.01*psif
   lef=float(ttl[ttl.index("Λευκά")+1].replace(",","."))*0.01*psif
   #the same for Valid,Invalid, White ballots respectivily. Thses percentages over voters


   for k in kommata:
      if psifoi[k]=="":psifoi[k]="0"  #if no data print zero
      print (perif,kommata[k],psifoi[k],psifoi_2019[k],sep=",")  #print data
 
   print(perif,"ΕΓΓΕΓΡΑΜΜΕΝΟΙ",egger,"-",sep=",")  #print other info
   print(perif,"ΑΚΥΡΑ",int(round(aky)),"-",sep=",")
   print(perif,"ΛΕΥΚΑ",int(round(lef)),"-",sep=",")
   print(perif,"ΕΓΚΥΡΑ",int(round(egyr)),"-",sep=",")
   print(perif,"ΣΥΜΜΕΤΟΧΗ",int(round(psif)),"-",sep=",")



#link template
link_tmp="http://ekloges-prev.singularlogic.eu/2023/may/v/home/districts/"

print("PERIF,KOMMA,PSIFOI2023,PSIFOI2019")
#csv header


#iterate function over all districts
#errors are on stderr
#std out should be redirected to csv file
for l in range(1,75):
   link=link_tmp+str(l)+"/"
   print ("Reading Districe",l,file=sys.stderr)
   ReadPage(link)
