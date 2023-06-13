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

parties={  2: "ΝΕΑ ΔΗΜΟΚΡΑΤΙΑ",
    4: "ΣΥΝΑΣΠΙΣΜΟΣ ΡΙΖΟΣΠΑΣΤΙΚΗΣ ΑΡΙΣΤΕΡΑΣ-ΠΡΟΟΔΕΥΤΙΚΗ ΣΥΜΜΑΧΙΑ",
    106: "ΠΑΣΟΚ - Κίνημα Αλλαγής",
    3: "ΚΟΜΜΟΥΝΙΣΤΙΚΟ ΚΟΜΜΑ ΕΛΛΑΔΑΣ",
    108: "Ελληνική Λύση",
    122: "ΜέΡΑ25-ΣΥΜΜΑΧΙΑ ΓΙΑ ΤΗ ΡΗΞΗ",
    131: "Νίκη",
    123: "ΠΛΕΥΣΗ ΕΛΕΥΘΕΡΙΑΣ - ΖΩΗ ΚΩΝΣΤΑΝΤΟΠΟΥΛΟΥ",
    135: "Συμμαχία Ανατροπής",
    60: "Εθνική Δημιουργία",
    128: "ΕΝΩΝΩ ΣΥΜΜΑΧΙΑ ΕΛΕΥΘΕΡΙΑΣ",
    28: "Οικολόγοι ΠΡΑΣΙΝΟΙ - ΠΡΑΣΙΝΗ ΕΝΟΤΗΤΑ",
    129: "Κίνημα 21",
    44: "ΑΝΤ.ΑΡ.ΣΥ.Α - ΑΝΤΙΚΑΠΙΤΑΛΙΣΤΙΚΗ ΑΡΙΣΤΕΡΗ ΣΥΝΕΡΓΑΣΙΑ για την ΑΝΑΤΡΟΠΗ",
    140: "Πνοή Δημοκρατίας",
    15: "Ένωση Κεντρώων",
    138: "ΕΛΕΥΘΕΡΟΙ ΞΑΝΑ",
    130: "Κίνημα Φτωχών",
    142: "ΕΑΝ...",
    141: "Πράσινο Κίνημα",
    134: "ΤΩΡΑ ΟΛΟΙ ΜΑΖΙ (Τ.ΟΛ.ΜΑ)",
    125: "ΚΟΜΜΟΥΝΙΣΤΙΚΟ ΚΟΜΜΑ ΕΛΛΑΔΑΣ (μαρξιστικό-λενινιστικό)",
    113: "ΕΛΛΗΝΩΝ ΣΥΝΕΛΕΥΣΙΣ",
    54: "ΚΑΠΝΙΣΤΙΚΕΣ ΟΜΑΔΕΣ ΓΙΑ ΤΗΝ ΤΕΧΝΗ ΚΑΙ ΤΗΝ ΕΙΚΑΣΤΙΚΗ ΣΥΓΚΡΟΤΗΣΗ",
    143: "ΕΝΟΤΗΤΑ - ΑΛΗΘΕΙΑ ΕΝ.Α",
    137: "ΠΟΛΙΤΙΚΗ ΠΡΩΤΟΒΟΥΛΙΑ",
    85: "ΚΟΙΝΩΝΙΑ ΑΞΙΩΝ - ΦΙΛΕΛΕΥΘΕΡΗ ΣΥΜΜΑΧΙΑ",
    133: "ΒΟΡΕΙΑ ΛΕΓΚΑ - ΚΡΑΜΑ",
    10: "Μαρξιστικό-Λένινιστικό Κομμουνιστικό Κόμμα Ελλάδας",
    66: "ΟΡΓΑΝΩΣΗ ΚΟΜΜΟΥΝΙΣΤΩΝ ΔΙΕΘΝΙΣΤΩΝ ΕΛΛΑΔΑΣ",
    139: "SOCIAL Σύγχρονο Δημοκρατικό Κόμμα",
    11: "ΟΑΚΚΕ-ΟΡΓΑΝΩΣΗ ΓΙΑ ΤΗΝ ΑΝΑΣΥΓΚΡΟΤΗΣΗ ΤΟΥ ΚΚΕ",
    136: "ΝΕΑ ΔΟΜΗ",
    132: "ΕΛΛΗΝΙΚΟ ΟΡΑΜΑ",
    20: "Δημοσθένης Βεργής ΕΛΛΗΝΕΣ ΟΙΚΟΛΟΓΟΙ",
    998: "Ανεξάρτητοι/Μεμονωμένοι Υποψήφιοι"}

partis_code={
    2: "nd",
    4: "syriza",
   106: "pasok",
     3: "kke",
     108: "ellinikiLysi",
     122: "mera25",
     131: "niki",
     123: "pleusi",
     135:  "simaxeia_anatropis",
     60:  "ethDim",
    128: "enono",
    28: "oikologoi_prasinoi",
    129: "kinima21",
    44: "antarsya",
    140:"pnoi_dimokratias",
    15: "enosi_kentroon",
    138: "eleutheroi_ksana",
    130: "kinimaftoxon",
    142: "ean",
    141:"prasino_kinima",
    134:"tolma",
    125: "kkeml",
    113: "elsyn",
    54: "kotes",
    143: "ena",
    137: "polprot",
    85:  "axia",
    133: "krama",
    10: "mlkkke",
    66: "okde",
    139: "social",
    11: "oakke",
    136: "ndomi",
    132: "orama",
    20: "vergis"}


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
file2 = open("PSIFOI_p_.json", 'w')
file2.write(json.dumps(PerifData))
file2.close()
#print(PerifData)



if os.path.isfile("PSIFOI_d.json"):
    with open("PSIFOI_d.json") as f:
        data=f.read()
        js = json.loads(data)
else:
    js={}
# reconstructing the data as a dictionary

link="http://ekloges-prev.singularlogic.eu/2023/may/stat/v/ep_3.js"
#link for stats ...  epiploen, plithismo klp

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
