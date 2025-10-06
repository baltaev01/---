import  re
xbet_nomi = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

emails = [
    "ali@gmail.com",  # ✓
    "test.user@yahoo.uz",  # ✓
    "invalid@",  # ✗
    "@example.com",  # ✗
    "user@domain"  # ✗
]
for email in emails:
    if re.match(xbet_nomi, email):
        print(f"{email}✓ ")
    else:
        print(f"{email}✗ ")


import re

andova_tel = r'^\+998[-\s\.]?\(?\d{2}\)?[-\s\.]?\d{3}[-\s\.]?\d{2}[-\s\.]?\d{2}$'

while True:
    telifon_n = input("Telefon raqamingizni kiriting: ")
    if re.match(andova_tel, telifon_n):
        print(f" Qabul qilindi: {telifon_n}")
        break
    else:
        print(" (+998) formatida qabul qilamiz.")
