# Royxatdadi bazisini katta harf bn bazisining bosh harfini katta qilish dasturi

cars = ['mazda','bmw','toyota','gm','kia']
for car in cars:
    if car == 'gm' or car == 'bmw':
        print(car.upper())
    else:
        print(car.title())



# Istalgan sonni musbat yoki manfiy ekanligini aniqlaydigan dastur

son = float(input("Istalgan sonni kiriting: "))
if son < 0:
    print(f"Kiritganingiz manfiy son")
else:
    print(f"Kiritganingiz musbat son")
#  Yoki >>>
son = float(input("Istalgan son kiriting:"))
print("Manfiy son") if son < 0 else print("Musbat son")


# Yoshingizga qarab chipta narxini belgilovchi dastur

yosh = int(input("Yoshingizni kiriting: "))
if yosh <= 4 or yosh > 60:
    print("4 yoshdan kichiklar va 60 yoshdan kattalarga chipta bepul !!!")
elif yosh <= 18:
    print("Sizga chipta 10 000 so'm")
elif yosh <= 35:
    print("Sizga chipta 15 000 so'm")
elif yosh <= 60:
    print("Sizga chipta 20 000 so'm")
else:
    print("Sizga bepul !!!")


# Siz so'ragan maxsulot do'konda(ro'yxatda) bor yoki yo'q ekanini aytuvchi dastur

maxsulotlar = ['yog\'','guruch','tuxum','shakar','choy','go\'sht','qaymoq','non','sut','qatiq','makaron']
savat = []
for n in range(5):
    savat.append(input(f"{n + 1} - mahsulotni kiriting: "))

for mahsulot in savat:
    if mahsulot in maxsulotlar:
        print(f"Do'konimizda {mahsulot} bor.")
    else:
        print(f"Do'konimizda {mahsulot} yo'q.")


# 10 dan 40 gacha bolgan, 2 ga qoldiqsiz bolinadigan sonlarni chiqaradi

for i in range(10,40):
    if i % 2 == 0:
        print(i)
    else:
        continue


# Login tekshiruvchi dastur

sorov = input('Assalamu_Alaykum, Login kiriting: ')
if sorov != 'Admin':
    print(f"Hush kelibsiz, {sorov.title()}")
else:
    print(f"Salom {sorov.title()}, Foydalanuvchilar royxatini korasizmi? ")


# Sonlar teng yoki teng emasligini aniqlaydi

son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
if son1 != son2:
    print("Sonlar teng emas")
else:
    print("Sonlar teng")


# Taom buyurtma berish

menyu = {
    'osh' : 14000,
    'lag\'mon' : 12000,
    'do\'lma' : 18000,
    'shashlik' : 10000,
    'somsa' : 15000,
    'mastava' : 8000,
    'sho\'rva' : 11000,
}
print('3 ta taom buyurtma bering: ')
buyutmalar = []
for n in range(3):
    buyutmalar.append(input(f"{n+1} - taom: ").lower())

for buyurtma in buyutmalar:
    if buyurtma in menyu:
        print(f"{buyurtma.title()} {menyu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz,bizda {buyurtma} yo'q")


# Kiritilgan sonni ildizini qaytaradi

son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')

