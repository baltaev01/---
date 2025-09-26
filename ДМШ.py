# class Foydalanuvchi:
#     def __init__(self, ismi, familyasi, email, yoshi):
#         self.ismi = ismi
#         self.familyasi = familyasi
#         self.email = email
#         self.yoshi = yoshi
#
#     def get_info(self):
#         return (f"Ismi: {self.ismi}\n"
#                 f"Familiyasi: {self.familyasi}\n"
#                 f"Email: {self.email}\n"
#                 f"Yoshi: {self.yoshi}\n")
#
# M1 = Foydalanuvchi("Alisher", "Morgen Shtern", "morgen@gmail.com", 31)
# print(M1.get_info())
#
#
# class Moshinalar:
#     def __init__(self, Lamborghini, mator, rang, qaropka, km, tezlik, km0dan100):
#         self.Lamborghini = Lamborghini
#         self.mator = mator
#         self.rang = rang
#         self.qaropka = qaropka
#         self.km = km
#         self.tezlik = tezlik
#         self.km0dan100 = km0dan100
#
#     def get_awto(self):
#         return (f"Lamborghini: {self.Lamborghini}\n"
#                 f"Mator: {self.mator}\n"
#                 f"Rang: {self.rang}\n"
#                 f"Qaropka: {self.qaropka}\n"
#                 f"Km: {self.km}\n"
#                 f"Tezlik: {self.tezlik}\n"
#                 f"0 dan 100 km/soat: {self.km0dan100}\n")
#
# L1 = Moshinalar("SVJ", "V12", "Yashil", "Robot avtomat", "0000", "350+ km/soat", "2.8 soniya")
# print(L1.get_awto())
#
#
# class dokon :
#     def __init__(self,sular,shkalatlar,pichenyalar,oyinchoqlar):
#        self.sular = sular
#        self.shkalatlar = shkalatlar
#        self.pichenyalar = pichenyalar
#        self.oyinchqlar = oyinchoqlar
#     def get_dokon(self):
#         return (
#            f"sular: {self.sular}\n"
#            f"shukalatlar: {self.shkalatlar}\n"
#             F"pichenyalar: {self.pichenyalar}\n"
#             f"oyinchoqlar: {self.oyinchqlar}\n")
# casa1 = dokon( "Coca-Cola","Nestle",  "Oreo", "Lego")
# casa2 = dokon("Pepsi","Millennium", "Yubileynoe", "Hot Wheels")
# casa3 = dokon("Fanta", "Korona", "BonGenie", "Barbie")
# casa4 = dokon("Sprite", "Alpen Gold", "Sladushka", "Puzzle")
#
# print(casa1.get_dokon())
# print(casa2.get_dokon())
# print(casa3.get_dokon())
# print(casa4.get_dokon())
#
#
# class Awto:
#     def __init__(self, nomi, mator, yil, probeg):
#         self.nomi = nomi
#         self.mator = mator
#         self.yil = yil
#         self.probeg = probeg
#
#     def get_avto(self):
#         return (
#             f"nomi: {self.nomi}, "
#             f"mator: {self.mator}, "
#             f"yil: {self.yil}, "
#             f"probeg: {self.probeg}"
#         )
#
# Mod1 = Awto("Treker", "1.7L", "2024", "0 km")
# Mod2 = Awto("Cobalt", "1.6L", "2025", "15 km")
#
# print(Mod1.get_avto())
# print(Mod2.get_avto())
#
#\
# class Avto :
#     def __init__(self, nomi, motor, yil, probeg):
#         self.nomi = nomi
#         self.motor = motor
#         self.yil = yil
#         self.probeg = probeg
#     def  get_Avto(self):
#      return (
#          f"nomi{self.nomi}\n"
#          f"motor{self.motor}\n"
#          f"yil{self.yil}\n"
#          f"probeg{self.probeg}\n"
#      )
#
# malumot = Avto("Toyota Camry", "2.5L I4", 2020, 54000)
# print(malumot.get_Avto())
#
# class AwtoSalon:
#     def __init__(self, awto_salon_nomi, tochkalar, manzil, moshinalar, rangi, motor):
#         self.awto_salon_nomi = awto_salon_nomi
#         self.tochkalar = tochkalar
#         self.manzil = manzil
#         self.moshinalar = moshinalar
#         self.rangi = rangi
#         self.motor = motor
#
#     def get_awto_salon(self):
#         return (
#             f"Avto salon nomi: {self.awto_salon_nomi}\n"
#             f"Filial(lar): {self.tochkalar}\n"
#             f"Manzil: {self.manzil}\n"
#             f"Mashinalar: {self.moshinalar}\n"
#             f"Rangi: {self.rangi}\n"
#             f"Motor: {self.motor}"
#         )
#
# malumot1 = AwtoSalon(
#     "GM Uzbekistan",
#     "Toshkent, Samarqand",
#     "Toshkent sh. Chilonzor",
#     ["Cobalt", "Gentra", "Malibu"],
#     ["oq", "qora", "kumush"],
#     ["1.5L", "1.6L", "2.0L"]
# )
# malumot2 = AwtoSalon(
#     "Kia Motors",
#     "Toshkent, Andijon",
#     "Andijon sh. Bobur ko'chasi",
#     ["K5", "Sportage", "Sorento"],
#     ["qizil", "ko‘k", "oq"],
#     ["2.0L", "2.5L", "3.0L"]
# )
#
# print(malumot1.get_awto_salon())
# print(malumot2.get_awto_salon())

# class avto_malumot:
#     def __init__(self,nomi, mator, rang, yil, yurgani, qanchaga_chiqishi, kg, qaropka):
#         self.nomi = nomi
#         self.mator = mator
#         self.rang = rang
#         self.yil = yil
#         self.yurgani = yurgani
#         self.qanchaga_chiqishi = qanchaga_chiqishi
#         self.kg = kg
#         self.qaropka = qaropka
#
#     def get_malumot(self):
#         return (
#             f"nomi{self.nomi}"
#             f"mator: {self.mator}, "
#             f"rang: {self.rang}, "
#             f"yil: {self.yil}, "
#             f"yurgani: {self.yurgani}, "
#             f"qanchaga chiqishi: {self.qanchaga_chiqishi}, "
#             f"kg: {self.kg}, "
#             f"qaropka: {self.qaropka}"
#         )
#
#
# mal1 = avto_malumot("Cobalt", "1.5L Turbo", "oq", 2022, 150000, 18000, 1250, "avtomat")
# mal2 = avto_malumot("BMW X5", "2.0L", "qora", 2020, 45000, 22000, 1350, "mexanik")
# mal3 = avto_malumot("Mercedes C300", "3.0L V6", "qizil", 2023, 50000, 40000, 1600, "avtomat")
# mal4 = avto_malumot("Tesla Model 3", "Elektr 150 Kvh", "ko‘k", 2024, 0, 35000, 1400, "1 tezlikli (elektr)")
# mal5 = avto_malumot("Toyota Prius", "1.8L Hybrid", "kumush", 2021, 30, 25000, 1300, "avtomat")
#
# print(mal1.get_malumot())
# print(mal2.get_malumot())
# print(mal3.get_malumot())
# print(mal4.get_malumot())
# print(mal5.get_malumot())










