import json
JSON = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

faylnomi = '.txt'
with open(faylnomi,'w') as fayl:
    fayl.write(json.dumps(JSON))

talaba_json = {"ism" : "Hasan" , "familiya" : "Husanov" , "tyil" : 2000}
fayil = 'talaba.txt'
with open(fayil,'w') as talaba:
    talaba.write(json.dumps(talaba_json))

with open(fayil, 'r') as talaba:
    data = json.load(talaba)
print(f"Talaba: {data['ism']} {data['familiya']} {data['tyil']}-tug'uli")
