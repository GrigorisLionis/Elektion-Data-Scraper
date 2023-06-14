import json
import requests
import os

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




if os.path.isfile("PSIFOI_p.json"):
    with open("PSIFOI_p.json") as f:
        data=f.read()
        js = json.loads(data)
else:
    js={}

link_tmp="http://ekloges-prev.singularlogic.eu/2023/may/dyn/v/ep_"
PerifData={}
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
file2 = open("PSIFOI_p.json", 'w')
file2.write(json.dumps(PerifData))
file2.close()
#print(PerifData)



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
