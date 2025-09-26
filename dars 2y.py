class Foydalanuvchi:
    def __init__(self, ismi, familyasi, email, yoshi):
        self.ismi = ismi
        self.familyasi = familyasi
        self.email = email
        self.yoshi = yoshi

    def get_info(self):
        return (f"Ismi: {self.ismi}\n"
                f"Familiyasi: {self.familyasi}\n"
                f"Email: {self.email}\n"
                f"Yoshi: {self.yoshi}\n")

M1 = Foydalanuvchi("Alisher", "Morgen Shtern", "morgen@gmail.com", 31)
print(M1.get_info())


class Moshinalar:
    def __init__(self, Lamborghini, mator, rang, qaropka, km, tezlik, km0dan100):
        self.Lamborghini = Lamborghini
        self.mator = mator
        self.rang = rang
        self.qaropka = qaropka
        self.km = km
        self.tezlik = tezlik
        self.km0dan100 = km0dan100

    def get_awto(self):
        return (f"Lamborghini: {self.Lamborghini}\n"
                f"Mator: {self.mator}\n"
                f"Rang: {self.rang}\n"
                f"Qaropka: {self.qaropka}\n"
                f"Km: {self.km}\n"
                f"Tezlik: {self.tezlik}\n"
                f"0 dan 100 km/soat: {self.km0dan100}\n")

L1 = Moshinalar("SVJ", "V12", "Yashil", "Robot avtomat", "0000", "350+ km/soat", "2.8 soniya")
print(L1.get_awto())

class Avto:
    def __init__(self, kompaniya, model,
                 rang=None, karobka=None,
                 yil=None, km=0,
                 tezlik=None, km0dan100=None,
                 narh=None):
        self.kompaniya = kompaniya
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.yil = yil
        self.km = km
        self.tezlik = tezlik
        self.km0dan100 = km0dan100
        self.narh = narh

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):   # agar obyekt ichida bunday xususiyat bo'lsa
                setattr(self, key, value)

    def get_info(self):
        return (f"Kompaniya: {self.kompaniya}\n"
                f"Model: {self.model}\n"
                f"Rang: {self.rang}\n"
                f"Karobka: {self.karobka}\n"
                f"Yili: {self.yil}\n"
                f"Yurgan masofa: {self.km} km\n"
                f"Maksimal tezlik: {self.tezlik} km/soat\n"
                f"0→100 km/s: {self.km0dan100} s\n"
                f"Narxi: {self.narh} USD")

    def __str__(self):
        return self.get_info()
avto1 = Avto("BMW", "X6", rang="Oq", yil=2022, km=15000, narh=85000)
print("Eski holat:\n", avto1)
avto1.update(rang="Qora", km=18000, narh=82000)
print("\nYangi holat:\n", avto1)










