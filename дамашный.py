with open('pi.txt') as  fayl:
    print(fayl.read())
fayl = open("pi.txt")
pi = fayl.read()
print(pi)
print(type(pi))
fayl.close()
pi = pi.rstrip()
pi = pi.replace("\n","")
pi = float(pi)
print(type(pi))
print(pi)
filename = 'data/Talaba.txt'
with open(filename) as file:
    talaba = file.readlines()
print(talaba)
talaba =[tal.rstrip() for tal in talaba]
print(talaba)
faylnomi = 'new_file.txt'
with open(faylnomi,'w') as fayl:
    fayl.write('Olmo  Hasanow ')
ism = 'Olmo  Hasanow'
tyil = 2010
with open(faylnomi,'w') as fayl:
    fayl.write(ism)
    fayl.write(str(tyil))
import pickle
talaba1 = {'ism':'hasan','familya':'husanov','tiyil':2010,'kurs':2}
talaba2 = {'ism':'hasan','familya':'husanov','tiyil':2010,'kurs':2}

with open('info', 'wb') as fail:
    pickle.dump(talaba1, fail)
    pickle.dump(talaba2, fail)
with open('info', 'rb') as fail:
    talaba1 = pickle.load(fail)
    talaba2 = pickle.load(fail)
print(talaba2)
print(talaba1)