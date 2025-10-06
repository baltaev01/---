import datetime as dt

hozir = dt.datetime.now()
print(hozir)

print(hozir.date())
print(hozir.time())
print(hozir.hour)
print(hozir.minute)
print(hozir.second)

bugun = dt.datetim.today()
print(f"Bugungi sana: {bugun}")
ertaga = dt.date(2025,10,7)
print(f"Bugungi sana: {ertaga}")

vaqtKeyin = dt.time(23,45,00)
print(vaqtKeyin)

bugun = dt.date.today()
new_year = dt.date(2025,12,31)
farq = new_year - bugun
print(farq)
print(f"Yangi yilga {farq.days} kun qoldi")


hozir = dt.datetime.now()

vaqt = hozir.strftime("%H/%M/%S")
print(f"Hozirgi soat{vaqt}")

sana = hozir.strftime("%d/%m/%Y")
print(f"Bugungi sana:{sana}")

sana = hozir.strftime("%d/%m/%Y %H:%M")
print(sana)

import re
from uzwords import words

andoza = "^ж..а$"

matches = []

for words in words:
    if re.search(andoza, words):
        matches.append(words)
print(matches)

import  re

matn = """Символы стали активно использоваться в пропаганде. Россияне, поддерживающие вторжение, используют, jaxongirbaltaev582@gmail.com, букву «Z» на своих машинах и одежде, но чаще знак появляется на провластных демонстрациях,ff4591997@gmail.com, билбордах, зданиях и в виде инсталляций. Государство организует «Z»-флешмобы в социальных сетях и на улицах. На выступающих против использования «Z» в России периодически заводят уголовные дела. «Z» часто окрашивают в цвета"""
andoza1 ='[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza1,matn)
print(email)

import re

andoza = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[#!?@$%^&*-]).{8,}$'

msg = "Yangi parol kiriting"
msg += ' (kamida 8 belgidan iborat, kamida 1 ta Lotin bosh harfi, 1 ta kichik harf,'
msg += ' 1 ta son va 1 ta maxsus belgi bo‘lishi kerak): \n'

while True:
    password = input(msg)
    if re.match(andoza, password):
        print("Maxfiy so‘z qabul qilindi")
        break
    else:
        print("Maxfiy so‘z talabga javob bermadi")
