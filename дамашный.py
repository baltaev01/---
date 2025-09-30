from uuid import uuid4
class shahs:
    def __init__(self, ism, familya, telefon_nomer,):
        self.__ism = ism
        self.__familya = familya
        self.__telefon_nomer = telefon_nomer
        self.__id = uuid4()

    def get_ism(self):
        return self.__ism

    def get_familya(self):
        return self.__familya

    def get_telefon_nomer(self):
        return self.__telefon_nomer
    def get_id(self):
        return self.__id

class talaba(shahs):
    def __init__(self, ism, familya, telefon_nomer,oligoh_nomi,kurs):
        super().__init__(ism,familya,telefon_nomer)
        self.__oligoh_nomi = oligoh_nomi
        self.__kurs = kurs

    def get_oliogo_nomi(self):
        return self.__oligoh_nomi
    def get_kurs(self):
        return self.__kurs


talaba1 = talaba("Ali", "Valiyev", 12345, "+998-93-333-09-08", 1)
talaba2 = talaba("Vali","Aliyev","+998-99-456-12-21","Tatu",2)
talaba3 = talaba("Aziz","Ozadov","+988-50-550-05-50","Tatu",3)
talaba4 = talaba("O'tabek","O'tabaev","+998-77-077-05-50","Tatu",4)

print(talaba1.get_ism())
print(talaba1.get_familya())
print(talaba1.get_id())
print(talaba1.get_telefon_nomer())
print(talaba1.get_kurs())
print(talaba1.get_oliogo_nomi())

# ///////////////////////////////////////

print(talaba2.get_ism())
print(talaba2.get_familya())
print(talaba2.get_id())
print(talaba2.get_telefon_nomer())
print(talaba2.get_kurs())
print(talaba2.get_oliogo_nomi())

# ///////////////////////////////////////

print(talaba3.get_ism())
print(talaba3.get_familya())
print(talaba3.get_id())
print(talaba3.get_telefon_nomer())
print(talaba3.get_kurs())
print(talaba3.get_oliogo_nomi())

# ///////////////////////////////////////

print(talaba4.get_ism())
print(talaba4.get_familya())
print(talaba4.get_id())
print(talaba4.get_telefon_nomer())
print(talaba4.get_kurs())
print(talaba4.get_oliogo_nomi())


from uuid import uuid4
class shahs:
    def __init__(self, ism, familya, telefon_nomer,talabalar_soni):
        self.__ism = ism
        self.__familya = familya
        self.__telefon_nomer = telefon_nomer
        self.__talabalar_soni = talabalar_soni
        self.__id = uuid4()
    def get_talabalr_soni(self):
        return self.__talabalar_soni

    def get_ism(self):
        return self.__ism

    def get_familya(self):
        return self.__familya

    def get_telefon_nomer(self):
        return self.__telefon_nomer
    def get_id(self):
        return self.__id

class talaba(shahs):
    def __init__(self, ism, familya, telefon_nomer,oligoh_nomi,kurs,odamlar_soni):
        super().__init__(ism,familya,telefon_nomer)
        self.__oligoh_nomi = oligoh_nomi
        self.__kurs = kurs
        self.__odamlar_soni = odamlar_soni

    def get_oliogo_nomi(self):
        return self.__oligoh_nomi
    def get_kurs(self):
        return self.__kurs
    def get_odamlar_soni(self):
        return self.__odamlar_soni


talaba1 = talaba("Ali", "Valiyev", 12345, "+998-93-333-09-08", 1,"4-milyon",)
talaba2 = talaba("Vali","Aliyev","+998-99-456-12-21","Tatu",2,"4-milyon",)
talaba3 = talaba("Aziz","Ozadov","+988-50-550-05-50","Tatu",3,"4-milyon",)
talaba4 = talaba("O'tabek","O'tabaev","+998-77-077-05-50","Tatu",4,"4milyon",)

print(talaba1.get_ism())
print(talaba1.get_familya())
print(talaba1.get_id())
print(talaba1.get_telefon_nomer())
print(talaba1.get_kurs())
print(talaba1.get_oliogo_nomi())
print(talaba1.get_talabalr_soni())
print(talaba1.get_odamlar_soni())

# ///////////////////////////////////////

print(talaba2.get_ism())
print(talaba2.get_familya())
print(talaba2.get_id())
print(talaba2.get_telefon_nomer())
print(talaba2.get_kurs())
print(talaba2.get_oliogo_nomi())
print(talaba1.get_talabalr_soni())
print(talaba1.get_odamlar_soni())

# ///////////////////////////////////////

print(talaba3.get_ism())
print(talaba3.get_familya())
print(talaba3.get_id())
print(talaba3.get_telefon_nomer())
print(talaba3.get_kurs())
print(talaba3.get_oliogo_nomi())
print(talaba1.get_talabalr_soni())
print(talaba1.get_odamlar_soni())

# ///////////////////////////////////////

print(talaba4.get_ism())
print(talaba4.get_familya())
print(talaba4.get_id())
print(talaba4.get_telefon_nomer())
print(talaba4.get_kurs())
print(talaba4.get_oliogo_nomi())
print(talaba1.get_talabalr_soni())
print(talaba1.get_odamlar_soni())





