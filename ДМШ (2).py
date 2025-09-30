class User:
    def __init__(self,ism,foydalanuvchi_ismi,parol , email):
        self.name = ism
        self.username = foydalanuvchi_ismi
        self.pochta = email
        self.parol = parol
        self.kurs = 2
    def get_name(self):
        print(self.name)
    def get_username(self):
        print(self.username)
    def get_password(self):
        print(self.parol)
    def update_kurs(self):
        self.kurs+=1
    def get_info(self):
        print(f"{self.name} {self.username} {self.parol} {self.pochta}, {self.kurs}-kurs")

user1 = User("Mirzo","@MIRZO","19861987","Mirzo@mail.com")
user2 = User("Asal","@ASALI","ddr4salom1","Asal@mail.com")


user1.get_info()
user2.get_info()


class Avto:
    def __init__(self, nomi, rangi, korobka, narxi, yili, km=21000):
        self.nomi = nomi
        self.rangi = rangi
        self.korobka = korobka
        self.narxi = narxi
        self.yili = yili
        self.km = km

    def get_info(self):
        return f"{self.nomi}, {self.rangi}, {self.korobka}, {self.narxi}$, {self.yili}-yil, {self.km} km"


class Salon:
    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.avtolar = []

    def add_avto(self, avto):
        self.avtolar.append(avto)

    def get_avtos(self):
        return [avto.get_info() for avto in self.avtolar]


avto1 = Avto("Damas", "Oq", "Mexanik", 12030, 2025)
avto2 = Avto("Labo", "Oq", "Mexanik", 12300, 2024, km=700)

salon = Salon(nomi="UZ Avto Motrus", manzil="pitnak")
salon.add_avto(avto1)
salon.add_avto(avto2)

for info in salon.get_avtos():
    print(info)

print(avto1.get_info())
