import json
import requests
import os


#simple scraper using API
#reads all vote data for disticts and municipalites
#saves data in local JSON file
#sometimes web pages are down so we aggregate the data in the local file and rerun the script as necessary


Perif={}
Dimoi={}


f1=open("kwdikoi.csv")
lines=f1.readlines()
for line in lines:
    if line[0]=="#": continue
    l=line.strip()
    l=l.split(",")
    l1=[int(l[0]),l[1],int(l[2]),l[3]]
    #print(l1)
    pc=l1[0]
    pn=l1[1]
    dc=l1[2]
    dn=l1[3]
    Dimoi[dc]=[dn,pn]
    if pc not in Perif:
       Perif[pc]={"name":pn,"dimoic":[],"dimoin":[]}
    Perif[pc]["dimoic"].append(dc)
    Perif[pc]["dimoin"].append(dn)


#create two dics, one witi DISTRICT names-codes : Perif
#one with Municipalities names-codes, as well as with Districts in which they belong


#local file to save all data for districts
if os.path.isfile("PSIFOI_p.json"):
    with open("PSIFOI_p.json") as f:
        data=f.read()
        js = json.loads(data)
else:
    js={}


link_tmp="http://ekloges-prev.singularlogic.eu/2023/may/dyn/v/ep_"
PerifData={}
#single dictionary holding all vote data for districts

for p in Perif:
    if(str(p) in js):
        PerifData[p]=js[str(p)]
        continue
    print("District :",p," not in file. Read from Web")
    link=link_tmp+str(p)+".js"
    r=requests.get(link,timeout=25)
    h=r.text
    if(len(h)<10):continue
    PerifData[p]=h
    #include all data of district in the single dictionary
file2 = open("PSIFOI_p.json", 'w')
file2.write(json.dumps(PerifData))
file2.close()



#local fil with all vote data for municipalities
if os.path.isfile("PSIFOI_d.json"):
    with open("PSIFOI_d.json") as f:
        data=f.read()
        js = json.loads(data)
else:
    js={}

#link="http://ekloges-prev.singularlogic.eu/2023/may/stat/v/ep_3.js"
#link for stats ...  added data TBI

link_tmp="http://ekloges-prev.singularlogic.eu/2023/may/dyn/v/dhm_"
DhmData={}
#single dictionary of all vote data for all municipalities

for p in Dimoi:
    if(str(p) in js):
        DhmData[p]=js[str(p)]
        continue
    print("Dimos :",p," not in file. Read from Web")
    link=link_tmp+str(p)+".js"
    r=requests.get(link,timeout=25)
    h=r.text
    if(len(h)<10):continue
    DhmData[p]=h
file2 = open("PSIFOI_d.json", 'w')
file2.write(json.dumps(DhmData))
file2.close()
