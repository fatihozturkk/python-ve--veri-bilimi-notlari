"""
# Python Temel Notlari

Bu dosya, Python'un temel konularini içeren notlarinizi düzenlenmiş ve geliştirilmiş haliyle sunmaktadir.
"""
  
# Matematiksel Operatörler
# ------------------------
# (+)   Toplama
# (-)   Çıkarma
# (*)   Çarpma
# (/)   Bölme
# (**)  Üs Alma
# (%)   Mod Alma (Kalanı verir)
# (//)  Tam Bölme


# Değişken Tanımlama
# ------------------------
maas_ali = 5000
maas_ahmet = 4000
vergi = 0.27

print("Ali'nin vergisiz maaşi:", maas_ali - (maas_ali * vergi))
print("Ahmet'in vergisiz maaşi:", maas_ahmet - (maas_ahmet * vergi))


# Değişken tanımlarken dikkat edilmesi gerekenler:
# - Değişken isimleri rakamla başlayamaz.
# - Anlamlı ve açıklayıcı olmalıdır.


# Veri Tipleri
# ------------------------
x = 1                # int
y = 2.3              # float
name = "Fatih"       # string
is_student = True    # bool


# Veri Tipi Dönüşümleri
# ------------------------
x = int(input("Sayi 1: "))
y = int(input("Sayi 2: "))
toplam = x + y
print("Toplam:", toplam)


# Veri tiplerini kontrol etme
print(type(x))
print(type(y))
print(type(name))
print(type(is_student))


# Daire Alan ve Çevre Hesaplama
# ------------------------
pi = 3.14
r = float(input("Yari çap: "))
alan = pi * (r ** 2)
cevre = 2 * pi * r
print("Alan:", alan)
print("Çevre:", cevre)


# String İşlemleri
# ------------------------
name = "Fatih"
surname = "Öztürk"
age = 36


# String formatlama
print("My name is {} {} and I am {} years old.".format(name, surname, age))


# Alternatif string formatlama (f-string)
print(f"My name is {name} {surname} and I am {age} years old.")



# Formatlı Yazım
# ------------------------
name = "Fatih"
surname = "Öztürk"
print("My name is {} {}".format(name, surname))
print("My name is {1} {0}".format(name, surname))  # İndeks numaralarıyla sıralama


result = 200 / 700
print("The result is {:.2f}".format(result))  # Virgülden sonra 2 basamak göster


# String İndeksleme
# ------------------------
greeting = "My name is Fatih Öztürk and I am 21 years old."
length = len(greeting)
print("İlk harf:", greeting[0])
print("Üçüncü harf:", greeting[3])
print("Toplam uzunluk:", length)
print("Son harf:", greeting[length-1])
print("Son harf (alternatif):", greeting[-1])


# String Metodları
# ------------------------
message = "Hello there. My name is Fatih Öztürk"
print(message.upper())      # Bütün harfleri büyük yapar.
print(message.lower())      # Bütün harfleri küçük yapar.
print(message.title())      # Her kelimenin ilk harfini büyük yapar.
print(message.capitalize()) # Sadece ilk harfi büyük yapar.
print(message.strip())      # Baştaki ve sondaki boşlukları temizler.
print(message.split())      # Kelimeleri listeye çevirir.


# Ekstra String Metodları
# ------------------------
message = "Hello there. My name is Fatih Ötürk"
print(message.replace("Fatih", "Ahmet"))  # Kelime değiştirme
print(message.count("a"))  # Belirtilen harfin kaç defa geçtiğini bulma
print(message.startswith("Hello"))  # Metin belirli bir kelimeyle başlıyor mu?
print(message.endswith("Öztürk"))  # Metin belirli bir kelimeyle bitiyor mu?


# 1- 'hello world ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = ' hello world '.strip()  # Hem baştaki hem de sondaki boşlukları kaldırır.
result = ' hello world '.lstrip()  # Sadece baştaki boşlukları kaldırır.
result = ' hello world '.rstrip()  # Sadece sondaki boşlukları kaldırır.
print(result)  # Doğru sonucu ekrana yazdırmak için tırnak içinden çıkardık.



# 2- 'www.fatihöztürk.com' içindeki 'fatihöztürk' bilgisi haricindeki karakterleri sil

result = 'www.fatihöztürk.com'.strip('w.moc')  

# Burada belirtilen karakterler (w, ., m, o, c) baştan ve sondan kaldırılır.


# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

course = "Python Programming"
result = course.lower()  # Tüm harfleri küçük harfe çevirir.


# 4- 'website' içinde kaç tane 'a' karakteri vardır?

website = "www.example.com"
result = website.count('a')  # 'a' harfinin kaç kez geçtiğini sayar.


# 5- 'website' "www" ile başlayıp "com" ile bitiyor mu?

result = website.startswith('www')  # 'www' ile başlıyorsa True döner.
result = website.endswith('com')  # 'com' ile bitiyorsa True döner.


# 6- 'website' içinde '.com' ifadesi var mı?

result = website.find('.com')  # '.com' ifadesinin başladığı indeksi döner, yoksa -1 döner.
result = website.find('.com', 0, 10)  # İlk 10 karakter içinde '.com' arar.
result = course.find('Python')  # 'Python' kelimesinin indeksini bulur.
result = course.rfind('Python')  # 'Python' kelimesinin en son geçtiği yeri bulur.


result = website.index('.com')  # '.com' bulunamazsa hata verir.
result = website.rindex('.com')  # '.com' ifadesinin en son geçtiği yeri bulur.

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi?

result = course.isalpha()  # Sadece harflerden oluşuyorsa True döner.
result = 'Hello'.isalpha()  # 'Hello' harflerden oluştuğu için True döner.
result = course.isdigit()  # Sadece rakamlardan oluşuyorsa True döner.
result = '123'.isdigit()  # '123' tamamen rakam olduğu için True döner.



# 8- 'contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

result = 'contents'.center(50, '*')  # 'contents' ortalanarak etrafına * eklenir.
result = 'contents'.ljust(50, '*')  # 'contents' sola yaslanır, sağa * eklenir.
result = 'contents'.rjust(50, '*')  # 'contents' sağa yaslanır, sola * eklenir.


# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

result = course.replace(' ', '-')  # Boşlukları '-' ile değiştirir.
result = course.replace(' ', '-', 5)  # İlk 5 boşluğu '-' ile değiştirir.
result = course.replace(' ', '')  # Tüm boşlukları kaldırır.


# 10- 'Hello world' karakter dizisindeki 'world' ifadesini 'There' olarak değiştirin.

result = 'Hello World'.replace('World', 'There')


# 11- 'course' karakter dizisini boşluk karakterinden ayırın.

result = course.split(' ')  # Boşlukları baz alarak parçalar listesi oluşturur.
result = result[2]  # 3. kelimeyi seçmek için kullanılır (Eğer yeterli eleman varsa).



# -------------------------------
# PYTHON LİSTELER (BASİT SEVİYE)
# -------------------------------


# Liste veri tipi farklı veri türlerini birlikte tutabilir.
my_list = ['bir', 2, True, 5.6]
print("Karişik tiplerde liste:", my_list)


# İki listeyi birleştiriyoruz.
list1 = ['one', 'two', 'three']
list2 = ['four', 'five', 'six']
combined = list1 + list2

print("Birleşmiş liste:", combined)
print("Toplam eleman sayisi:", len(combined))
print("Üçüncü eleman:", combined[2])  # "three"


# İç içe listeler ile kullanıcı bilgilerini tutalım.
userA = ['Fatih', 21]
userB = ['Batuhan', 25]


# Listeyi doğrudan birleştirirsek düz bir yapı olur
users_flat = userA + userB
print("Düz yapi:", users_flat)


# Listeyi iç içe yerleştirirsek veri yapısı daha anlamlı olur
users_nested = [userA, userB]
print("İç içe yapi:", users_nested)
print("İkinci kullanicinin yaşi:", users_nested[1][1])
print("İkinci kullanicinin ismi:", users_nested[1][0])


# -----------------------------------------
# LİSTE UYGULAMASI: ARAÇ MARKALARI ÜZERİNDE
# -----------------------------------------

car_models = ['BMW', 'Mercedes', 'Opel', 'Mazda']
print("Başlangiç listesi:", car_models)

# Listenin uzunluğu
print("Liste uzunluğu:", len(car_models))

# İlk ve son eleman
print("İlk eleman:", car_models[0])
print("Son eleman:", car_models[-1])

# Son elemanı (Mazda) Toyota ile değiştiriyoruz
car_models[-1] = 'Toyota'
print("Güncel liste:", car_models)

# 'Mercedes' listede var mı?
is_mercedes_in_list = 'Mercedes' in car_models
print("'Mercedes' listede var mi?:", is_mercedes_in_list)

# -2 indeksindeki değer
print("Sondan ikinci eleman:", car_models[-2])

# İlk üç eleman
print("İlk 3 marka:", car_models[:3])

# Son iki elemanı yeni markalarla değiştir
car_models[-2:] = ['Toyota', 'Renault']
print("Yeni güncellenmiş liste:", car_models)

# Listenin sonuna yeni markalar ekleyelim
car_models += ['Audi', 'Nissan']
print("Yeni elemanlarla birlikte:", car_models)

# Son elemanı kaldıralım
del car_models[-1]
print("Son eleman silindikten sonra:", car_models)

# Listeyi tersten yazdırmak
print("Ters liste:", car_models[::-1])


# -------------------------------------
# VERİ YAPISI ÖRNEĞİ: ÖĞRENCİ BİLGİLERİ
# -------------------------------------

studentA = ['Fatih', 'Öztürk', 2004, [70, 60, 70]]
studentB = ['İbrahim', 'Culfa', 1999, [80, 80, 70]]
studentC = ['Emre', 'Biçer', 1998, [80, 70, 90]]

# Öğrenci bilgilerinden bazılarını yazdıralım
print("Öğrenci A'nin adi:", studentA[0])
print("Öğrenci B'nin soyadi:", studentB[1])
print("Öğrenci C'nin ikinci notu:", studentC[3][1])


# -----------------------------------
# LİSTE METOTLARI (SAYILAR & HARFLER)
# -----------------------------------

numbers = [1, 13, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

# Sayısal işlemler
print("Minimum sayi:", min(numbers))
print("Maksimum sayi:", max(numbers))

# Harfsel işlemler
print("Alfabetik olarak ilk harf:", min(letters))
print("Alfabetik olarak son harf:", max(letters))

# Dilimleme örnekleri
print("3. ile 6. indeks arasindaki sayilar:", numbers[3:6])
print("İlk üç sayi:", numbers[:3])

# Eleman ekleme
numbers.append(49)           # Listenin sonuna
numbers.insert(3, 78)        # Belirli bir konuma
numbers.insert(-1, 52)       # Sona yakın bir yere
print("Yeni sayi listesi:", numbers)

# Eleman silme
numbers.pop()                # Son elemanı sil
numbers.pop(0)               # İlk elemanı sil
numbers.remove(49)           # Belirli bir değeri sil

# Sıralama ve ters çevirme
numbers.sort()
letters.sort()

numbers.reverse()
letters.reverse()

print("Sirali ve ters çevrilmiş sayilar:", numbers)
print("Sirali ve ters çevrilmiş harfler:", letters)



# ----------------- TUPLE (Demetler) -----------------
# Tuple'lar listeler gibi sıralı yapılardır ama değiştirilemezler (immutable)

liste = [1, 2, 3]                        # Liste tanımı
tuple = (1, 'iki', 3)                   # Tuple tanımı (farklı veri tipleri içerebilir)

print(type(liste))                      # <class 'list'>
print(type(tuple))                      # <class 'tuple'>

print(liste[2])                         # Liste 3. eleman: 3
print(tuple[2])                         # Tuple 3. eleman: 3

print(len(liste))                       # Liste uzunluğu: 3
print(len(tuple))                       # Tuple uzunluğu: 3

liste = ['ali', 'veli']
tuple = ('damla', 'ayşe', 'ayşe')

names = ('demet', 'emel', 'ayşe') + tuple  # Tuple'lar birleştirilebilir
print(names)                              # ('demet', 'emel', 'ayşe', 'damla', 'ayşe', 'ayşe')

print(tuple.count('ayşe'))                # 'ayşe' kaç kez geçiyor? → 2
print(tuple.index('ayşe'))                # 'ayşe' ilk hangi indexte? → 1



# ----------------- DICTIONARY (Sözlükler) -----------------
# Anahtar:değer (key:value) yapısı ile çalışırlar

sehirler = ['kocaeli', 'istanbul']
plakalar = [41, 34]

# Şehir ismine göre plaka almak
print(plakalar[sehirler.index('kocaeli')])  # 41

# Sözlük yapısıyla:
plakalar = {
    'kocaeli': 41,
    'istanbul': 34
}

print(plakalar['istanbul'])   # 34
print(plakalar['kocaeli'])    # 41

plakalar['ankara'] = 6        # Yeni anahtar-değer ekleme
print(plakalar)               # {'kocaeli': 41, 'istanbul': 34, 'ankara': 6}

# Kullanıcı bilgileri:
users = {
    'fatihöztürk': 36,
    'batuhanöztürk': 21
}
print(users['fatihöztürk'])    # 36

# İç içe sözlük (nested dictionary)
users = {
    'fatihöztürk': {
        'age': 36,
        'email': 'fatihöztürk@gmail.com',
        'address': 'istanbul,esenyurt',
        'phone': '05341231234'
    },
    'batuhanöztürk': {
        'age': 21,
        'email': 'batuhan@gmail.com',
        'address': 'istanbul,esenkent',
        'phone': '05313253654'
    },
}

print(users['fatihöztürk'])    # fatihöztürk'ün tüm bilgileri
print(users['batuhanöztürk'])    # batuhanöztürk'ün tüm bilgileri



# ----------------- SET (Küme) -----------------
# Sırasız, benzersiz öğelerden oluşur. Index yoktur, aynı eleman tekrar edemez.

fruits = {'orange', 'apple', 'banana'}

# print(fruits[0])  # HATA: set'ler indekslenemez

for x in fruits:
    print(x)  # Her meyveyi yazdır (sıra rastgele olabilir)

# Eleman ekleme
fruits.add('cherry')

# Çoklu eleman ekleme
fruits.update(['mango', 'grape'])

# Eleman silme
fruits.remove('mango')   # mango varsa siler, yoksa HATA verir
fruits.discard('apple')  # apple varsa siler, yoksa HATA vermez
fruits.pop()             # rastgele bir elemanı siler

fruits.clear()           # tüm elemanları siler
print(fruits)            # boş küme → set()

# Listeyi kümeye dönüştürme (aynı olanlar silinir)
myList = [1, 2, 5, 4, 4, 2, 1]
print(myList)         # Orijinal liste
print(set(myList))    # {1, 2, 4, 5}



# ----------------- VALUE & REFERENCE TYPES -----------------

# VALUE TYPE (değer tipi): sayılar gibi
x = 5
y = 25

x = y      # x artık 25 olur
y = 10     # y değiştirilse de x değişmez

print(x, y)   # 25 10

# REFERENCE TYPE (referans tipi): listeler gibi
a = ['apple', 'banana']
b = ['apple', 'banana']

a = b        # a artık b ile aynı listeyi gösteriyor (aynı adres)

b[0] = 'grape'   # b'de yapılan değişiklik a'ya da yansır

print(a, b)      # ['grape', 'banana'] ['grape', 'banana']




# 🔹 ATAMA OPERATÖRLERİ ÖRNEKLERİ

x, y, z = 5, 10, 20  # Çoklu atama: x=5, y=10, z=20

x, y = y, x          # x ve y'nin değerlerini yer değiştiriyoruz

x += 5               # x = x + 5
x -= 5               # x = x - 5
x *= 5               # x = x * 5
x /= 5               # x = x / 5
x %= 5               # x = x % 5
x **= 5              # x = x ** 5 (x'in 5. kuvveti)

print(x, y, z)       # Sonuçları yazdırır



# 🔹 UYGULAMALI ATAMA OPERATÖRLERİ SORULARI

x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6  # Tuple (demet) tanımlandı

# ✅ 1. Kullanıcıdan alınan 2 sayının çarpımı ile (x + y + z) farkı nedir?
a = int(input('1. sayi: '))
b = int(input('2. sayi: '))
result = (a * b) - (x + y + z)
print("1. Sonuç:", result)

# ✅ 2. y'nin x'e kalansız bölümünü hesaplayın
result = y // x
print("2. Sonuç:", result)

# ✅ 3. (x + y + z) % 3 nedir?
toplam = x + y + z
result = toplam % 3
print("3. Sonuç:", result)

# ✅ 4. y'nin x. kuvvetini hesaplayınız
result = y ** x
print("4. Sonuç:", result)

# ✅ 5. x, *y, z = numbers işlemine göre z'nin küpü nedir?
x, *y, z = numbers  # Unpacking: x=1, y=[5,7,10], z=6
result = z ** 3
print("5. Sonuç:", result)

# ✅ 6. x, *y, z = numbers işlemine göre y'nin toplamı nedir?
x, *y, z = numbers  # y = [5, 7, 10]
result = sum(y)
print("6. Sonuç:", result)
 
 
 # ============================
# KARŞILAŞTIRMA OPERATÖRLERİ
# ============================

a, b, c, d = 5, 5, 10, 4
username = 'fatihozturk'
password = '1234'

# == operatörü: Eşit mi?
print(a == b)              # True
print(a == c)              # False
print('fthztrk' == username)      # False
print('fatihozturk' == username)  # True

# != operatörü: Eşit değil mi?
print(a != b)              # False
print(a != c)              # True

# >, <, >=, <=: Büyüklük/küçüklük karşılaştırmaları
print(a > c)               # False
print(a < c)               # True
print(a >= b)              # True
print(c <= b)              # False

# True == 1 ve False == 0 kontrolü
print(True == 1)           # True
print(False == 0)          # True

# Toplama işlemi: False(0) + True(1) + 40 = 41
print(False + True + 40)   # 41


# ===================================================
# 1. GİRİLEN 2 SAYIDAN HANGİSİ DAHA BÜYÜKTÜR?
# ===================================================

a = int(input('a: '))
b = int(input('b: '))

result = a > b
print(f'a: {a} b: {b} den büyüktür: {result}')


# ===================================================
# 2. VİZE VE FİNAL NOTUYLA ORTALAMA HESAPLAMA
# Vize %60 (iki vizenin ortalaması), Final %40
# ===================================================

vize1 = int(input('1. Vize notu: '))
vize2 = int(input('2. Vize notu: '))
final = int(input('Final notu: '))

vize_ortalama = (vize1 + vize2) / 2
ortalama = (vize_ortalama * 0.6) + (final * 0.4)

print(f'Ortalama: {ortalama}')


# ===================================================
# 3. BİR SAYININ TEK Mİ ÇİFT Mİ OLDUĞUNU BULMA
# ===================================================

sayi = int(input('Sayı: '))
tek_mi = (sayi % 2 == 0)
print(f'Girilen sayının çift olma durumu: {tek_mi}')


# ===================================================
# 4. BİR SAYI POZİTİF Mİ NEGATİF Mİ?
# ===================================================

sayi = int(input('Sayi: '))
pozitif_mi = sayi > 0
print(f'Sayinin pozitif olma durumu: {pozitif_mi}')


# ===================================================
# 5. EMAIL ve PAROLA DOĞRULAMA
# ===================================================

kayitli_email = 'email@sadikturan.com'
kayitli_parola = 'abc123'

girilen_email = input('Email: ')
girilen_parola = input('Parola: ')

dogru_email = kayitli_email == girilen_email
dogru_parola = kayitli_parola == girilen_parola

print(f'Email doğru mu?: {dogru_email}')
print(f'Parola doğru mu?: {dogru_parola}')



# ===================================================
# MANTIKSAL OPERATÖRLER (and, or, not)
# ===================================================

x = 6

# Karşılaştırmalı aralık sorgusu
print(5 < x < 10)  # True

# AND operatörü: Her iki koşul da True olmalı
print((x > 5) and (x < 10))  # True

# OR operatörü: En az bir koşul True olmalı
print((x > 0) or (x % 2 == 0))  # True

# NOT operatörü: Koşulun tersini verir
print(not (x > 0))  # False

# x, 5-10 arasında VE çift mi?
sonuc = ((x > 5) and (x < 10)) and (x % 2 == 0)
print(f'x, 5-10 arasinda ve çift mi?: {sonuc}')




# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.


x = int(input("Sayi: "))
result = (0 <= x <= 100)
print(f"0-100 arasinda mi?: {result}")


# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.


x = int(input("Sayi: "))
result = (x > 0) and (x % 2 == 0)
print(f"Girilen sayi pozitif çift mi?: {result}")

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.


email = "fatihztrk@gmail.com"
password = 1453

girilen_email = input("Email: ")
girilen_password = int(input("Parola: "))

result = (girilen_email == email) and (girilen_password == password)
print(f"Giriş bilgileri doğru mu?: {result}")


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(f"a en büyük mü?: {(a > b) and (a > c)}")
print(f"b en büyük mü?: {(b > a) and (b > c)}")
print(f"c en büyük mü?: {(c > a) and (c > b)}")

# İsteğe bağlı olarak eşitlikleri de kontrol edebilirsin.


# 5- 2 vize (%60) ve final (%40) ile ortalama hesaplayın
# ve geçip geçmediğini  şarta göre değerlendirin.


vize1 = float(input("1. Vize: "))
vize2 = float(input("2. Vize: "))
final = float(input("Final: "))

vize_ort = (vize1 + vize2) / 2
ortalama = (vize_ort * 0.6) + (final * 0.4)

print(f"Not ortalamasi: {ortalama}")

# a) Ortalama 50 ve üstüyse geçti, değilse kaldı
gecti_mi = (ortalama >= 50) and (final >= 50)
print(f"Geçti mi (ortalama >= 50 ve final >= 50)?: {gecti_mi}")

# b) Eğer final 70 ve üstüyse ortalamaya bakmadan geçer
gecti_finalle = (final >= 70)
print(f"Final notu 70 ve üstü mü (direkt geçer mi?): {gecti_finalle}")



# =======================================
# IDENTITY OPERATÖRLERİ: is / is not
# =======================================
# "is" => aynı nesne mi (hafıza adresi olarak)
# "==" => içerik olarak eşit mi

x = y = [1, 2, 3]  # x ve y aynı listeyi gösteriyor (aynı adres)
z = [1, 2, 3]      # z farklı bir listedir (içeriği aynı olsa da)

print(x == y)   # True: içerikler aynı
print(x == z)   # True: içerikler aynı
print(x is y)   # True: x ve y aynı nesne
print(x is z)   # False: x ve z içerik olarak aynı ama adres olarak farklı



# =======================================
# Liste içeriğini değiştirip tekrar kontrol
# =======================================

x = [1, 2, 3]
y = [2, 4]

del x[2]        # x = [1, 2]
y[1] = 1        # y = [2, 1]
y.reverse()     # y = [1, 2]

print(x == y)       # True: içerik olarak eşit
print(x is y)       # False: farklı nesneler
print(x is not y)   # True: aynı nesne değiller



# =======================================
# MEMBERSHIP OPERATÖRÜ: in / not in
# =======================================

meyveler = ['apple', 'banana']

print('banana' in meyveler)     # True: 'banana' listede var

isim = 'fatih'
print('a' in isim)              # True: 'a' harfi var
print('a' not in isim)          # False: çünkü var zaten



# ===============================
# PYTHONDA KOŞUL İFADELERİ
# ===============================

# 1. Kullanıcı Giriş Doğrulama (Basit Koşul)
username = 'fatihöztürk'
password = '1453'

isLoggedIn = (username == 'fatihöztürk') and (password == '1453')

if isLoggedIn:
    print('Hoş Geldiniz ' + username)
else:
    print('Kullanici adi ya da şifre yanliş')


# 2. Gelişmiş Koşul ile Giriş Kontrolü (İç içe if)
username = 'fatihöztürkkk'
password = '1453'

if username == 'fatihöztürk':
    if password == '1453':
        print('Hoş Geldiniz ' + username)
    else:
        print('Şifre yanliş')
else:
    print('Kullanici adi yanliş')


# 3. İki Sayı Karşılaştırma
x = int(input('x: '))
y = int(input('y: '))

if x > y:
    print('x, y\'den büyüktür')
elif x == y:
    print('x ile y eşittir')
else:
    print('x, y\'den küçük')


# 4. Sayının Pozitif, Negatif veya Sıfır Olduğunu Bulma
num = int(input('Sayi: '))

if num > 0:
    print('Pozitif bir sayi')
elif num == 0:
    print('Sayi sifir (ne pozitif ne negatif)')
else:
    print('Negatif bir sayi')


# 5. Ehliyet Alma Uygulaması
# Koşul: yaş ≥ 18 ve eğitim durumu lise veya üniversite olmalı
name = input('Adiniz: ')
yas = int(input('Yaşiniz: '))
egitim = input('Eğitim durumunuz (ilkokul/ortaokul/lise/üniversite): ').lower()

if yas >= 18 and (egitim == 'lise' or egitim == 'üniversite'):
    print('Ehliyet alabilirsiniz.')
else:
    print('Ehliyet almak için yaşiniz ya da eğitiminiz yetersiz.')


# 6. Not Ortalaması ile Harf Notu Hesaplama
not1 = int(input('1. Yazili: '))
not2 = int(input('2. Yazili: '))
sozlu = int(input('Sözlü: '))

ortalama = (not1 + not2 + sozlu) / 3

if 0 <= ortalama < 25:
    print('Not araliği: 0')
elif 25 <= ortalama < 45:
    print('Not araliği: 1')
elif 45 <= ortalama < 55:
    print('Not araliği: 2')
elif 55 <= ortalama < 70:
    print('Not araliği: 3')
elif 70 <= ortalama < 85:
    print('Not araliği: 4')
elif 85 <= ortalama <= 100:
    print('Not araliği: 5')
else:
    print('Geçersiz not girdiniz.')


# 7. Araç Servis Süresi Hesaplama
# 1. bakım: 1. yıl
# 2. bakım: 2. yıl
# 3. bakım: 3. yıl

alim_yili = int(input('Araç hangi yilda alindi? '))
mevcut_yil = int(input('Şu an hangi yildayiz? '))

arac_yasi = mevcut_yil - alim_yili

if arac_yasi == 1:
    print('1. bakim yili')
elif arac_yasi == 2:
    print('2. bakim yili')
elif arac_yasi == 3:
    print('3. bakim yili')
elif arac_yasi > 3:
    print('3 yil üzeri - genel bakim zamani')
else:
    print('Henüz bakim zamani gelmemiş.')


# ===============================
# KOŞUL İFADELERİ UYGULAMALARI
# ===============================


# 1. Girilen sayının 0-100 arasında olup olmadığını kontrol etme
sayi = int(input('Sayi: '))

if 0 < sayi < 100:
    print('Girilen sayi 0 ile 100 arasindadir.')
else:
    print('Girilen sayi 0 ile 100 arasinda değildir.')



# 2. Girilen sayının pozitif ve çift olup olmadığını kontrol etme
sayi = int(input('Sayi: '))

if sayi > 0 and sayi % 2 == 0:
    print('Sayi hem pozitif hem de çift sayidir.')
elif sayi > 0:
    print('Sayi pozitif ama çift değil.')
elif sayi % 2 == 0:
    print('Sayi çift ama pozitif değil.')
else:
    print('Sayi ne pozitif ne de çift.')



# 3. E-posta ve parola ile giriş kontrolü
email = 'fatihztrk1453@gmail.com'
password = 'fatih1453'

girilen_eposta = input('E-posta: ')
girilen_sifre = input('Parola: ')

if girilen_eposta == email and girilen_sifre == password:
    print('Giriş başarili.')
elif girilen_eposta == email and girilen_sifre != password:
    print('E-posta doğru ama parola yanliş.')
elif girilen_eposta != email and girilen_sifre == password:
    print('Parola doğru ama e-posta yanliş.')
else:
    print('Hem e-posta hem de parola yanliş.')



 # PYTHONDA FOR DÖNGÜLERİ

names = ['fatih', 'mehmet', 'öztürk']

for name in names:
    print(f'my name is {name}')

name = 'fatih öztürk'

for n in name:
    print(n)

tuple = (1, 2, 3, 4, 5)

for t in tuple:
    print(t)

tuple = [(1, 2), (3, 4), (5, 6)]

for a, b in tuple:
    print(a, b)

f = {'k1': 1, 'k2': 2, 'k3': 3}
for item in f:
    print(item)  # sadece anahtarlar

f = {'k1': 1, 'k2': 2, 'k3': 3}
for item in f.items():
    print(item)  # (anahtar, değer) çiftleri



# ÖRNEKLER
sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1- sayılar listesindeki hangi sayilar 3'ün katıdır ?
for sayi in sayilar:
    if sayi % 3 == 0:
        print(sayi)

# 2- sayılar listesindeki sayıların toplamı kaçtır ?
toplam = 0
for sayi in sayilar:
    toplam += sayi
print('toplam:', toplam)

# 3- sayılar listesindeki tek sayıların karesini alın.
for sayi in sayilar:
    if sayi % 2 == 1:
        print(f'{sayi} karesi: {sayi ** 2}')

sehirler = ['kocaeli', 'istanbul', 'rize', 'ankara', 'izmir']

# 4- şehirlerin hangileri en fazla 5 karakterlidir ?
for sehir in sehirler:
    if len(sehir) <= 5:
        print(sehir)

ürünler = [
    {'name': 'iphone 11', 'price': '4000'},
    {'name': 'iphone 12', 'price': '5000'},
    {'name': 'iphone 13', 'price': '6000'},
    {'name': 'iphone 14', 'price': '7000'},
    {'name': 'iphone 15', 'price': '8000'}
]

# 5- ürün fiyatlarının toplamı nedir ?
toplam_fiyat = 0
for urun in ürünler:
    toplam_fiyat += int(urun['price'])
print('Toplam fiyat:', toplam_fiyat)

# 6- ürünlerden fiyatı en fazla 5000 olan ürünleri göster ?
for urun in ürünler:
    if int(urun['price']) <= 5000:
        print(urun['name'])



# WHILE DÖNGÜSÜ

# 1- 0'dan 99'a kadar sayılar
x = 0
while x < 100:
    print(x)
    x += 1
print('bitti.')

# 2- 0'dan 99'a kadar çift sayılar
x = 0
while x < 100:
    if x % 2 == 0:
        print(x)
    x += 1
print('bitti.')

# 3- 0'dan 99'a kadar tek sayılar (f-string ile)
x = 0
while x < 100:
    if x % 2 == 1:
        print(f'sayi tek: {x}')
    x += 1
print('bitti.')

# 4- Kullanıcıdan isim iste, boş geçerse tekrar sor
name = ''
while not name:  # name boş olduğu sürece
    name = input('ismini gir: ')
    print(f'merhaba, {name}')



# WHILE DÖNGÜSÜ

# 0'dan 99'a kadar sayıları yazdır
x = 0
while x < 100:
    print(x)
    x += 1
print('bitti.')


# 0'dan 99'a kadar çift sayıları yazdır
x = 0
while x < 100:
    if x % 2 == 0:
        print(x)
    x += 1
print('bitti.')


# 0'dan 99'a kadar tek sayıları yazdır
x = 0
while x < 100:
    if x % 2 == 1:
        print(f'sayi tek: {x}')
    x += 1
print('bitti.')


# Kullanıcıdan isim alana kadar devam et
name = ''
while not name:
    name = input('İsmini gir: ')
    print(f'Merhaba, {name}')


# 1- Sayılar listesini while ile ekrana yazdır
sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
i = 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1


# 2- Başlangıç ve bitiş sayılarını kullanıcıdan alıp aradaki tek sayıları yazdır
baslangic = int(input('Başlangıç: '))
bitis = int(input('Bitiş: '))

while baslangic < bitis:
    baslangic += 1
    if baslangic % 2 == 1:
        print(baslangic)


# 3- 1-100 arasındaki sayıları azalan şekilde yazdır
i = 100
while i > 0:
    print(i)
    i -= 1


# 4- Kullanıcıdan alınan 5 sayıyı listeye ekle ve yazdır
numbers = []
i = 0
while i < 5:
    sayi = int(input('Sayi: '))
    numbers.append(sayi)
    i += 1

print(numbers)


# 5- Kullanıcıdan ürün bilgisi al ve dictionary listesi olarak kaydet
urunler = []
adet = int(input('Kaç ürün eklemek istiyorsunuz? '))

i = 0
while i < adet:
    name = input('Ürün ismi: ')
    price = input('Ürün fiyati: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1

# Ürünleri ekranda yazdır
i = 0
while i < len(urunler):
    print(f"Ürünün adi: {urunler[i]['name']}, fiyati: {urunler[i]['price']}")
    i += 1



# BREAK ve CONTINUE İFADELERİ

# Örnek 1: break -> döngüyü tamamen durdurur
name = 'fatih öztürk'

for letter in name:
    if letter == 'h':
        break   # 'h' gördüğünde döngüyü bitirir
    print(letter)


# Örnek 2: continue -> o adımdaki işlemi atlar, döngü devam eder
name = 'fatih öztürk'

for letter in name:
    if letter == 'h':
        continue   # 'h' karakterini atla
    print(letter)


# Örnek 3: while + break
x = 0
while x < 6:
    if x == 3:
        break   # 3 olduğunda döngüyü durdur
    print(x)
    x += 1


# Örnek 4: while + continue
x = 0
while x < 6:
    x += 1   # önce artır ki sonsuz döngü olmasın
    if x == 3:
        continue   # 3'ü atla
    print(x)


# Örnek 5: 1-100 arasındaki tek sayıların toplamı
x = 0
result = 0

while x <= 100:
    x += 1
    if x % 2 == 0:
        continue   # çift sayıları atla
    result += x
print(f'1-100 arasindaki tek sayilarin toplami: {result}')



# ================================
# RANGE
# ================================
# range(start, stop, step) → belli bir aralıkta sayıları üretir.
# start: başlangıç sayısı
# stop: bitiş (dahil değil)
# step: artış miktarı

for item in range(5, 10):
    # 5'ten başlar 10'a kadar (10 hariç) gider
    print(item)

for item in range(40, 90, 5):
    # 40'tan başlar, 90'a kadar 5'er 5'er artar
    print(item)

# range() listesini doğrudan görmek istersek list() içine alırız
print(list(range(40, 90, 5)))


# ================================
# ENUMERATE
# ================================
# enumerate() → hem index (sıra numarası), hem de değeri döndürür

greeting = 'hello there'

for index, letter in enumerate(greeting):
    # her adımda hem harf hem sıra numarası gelir
    print(f'letter:{index} letter:{letter}')


# ================================
# ZIP METODU
# ================================
# zip() → birden fazla listeyi elemanlarına göre eşleştirir

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [111, 222, 333, 444, 555]

# zip'i list() içine alırsak eşleşmeleri görebiliriz
print(list(zip(list1, list2, list3)))

# for döngüsüyle zip kullanırsak, her turda bir tuple döner
for item in zip(list1, list2, list3):
    print(item)

# tuple içini parçalayarak istediğimiz değerleri alabiliriz
for a, b, c in zip(list1, list2, list3):
    print(a)   # burada sadece list1'deki değerleri yazdırıyoruz


# ================================
# LİST COMPREHENSIONS
# ================================
# List Comprehension, bir listeyi kısa ve daha okunabilir şekilde üretmemizi sağlar.


# 0'dan 9'a kadar sayıları listeye ekler
numbers = [x for x in range(10)]
print(numbers)


# Aynı işlemin klasik for döngüsü ile yapılmış hali
numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)


# ================================
# KARE ALMA
# ================================
# Her sayının karesini ekrana yazdırır
for x in range(10):
    print(x**2)

# Aynısını list comprehension ile listeye atarız
numbers = [x**2 for x in range(10)]
print(numbers)


# ================================
# KOŞULLU KULLANIM
# ================================
# Sadece 3'e bölünebilen sayıların karesini alır
numbers = [x*x for x in range(10) if x % 3 == 0]
print(numbers)


# ================================
# STRİNGDEN LİSTE YAPMA
# ================================
mystring = 'Hello'

# klasik yöntem
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# list comprehension ile
mylist = [letter for letter in mystring]
print(mylist)


# ================================
# YILLARDAN YAŞ HESAPLAMA
# ================================
years = [2003, 2000, 1974, 1977]
ages = [2025 - year for year in years]
print(ages)


# ================================
# İF ELSE KULLANIMI
# ================================
# Sayı çiftse kendisini, tekse 'Tek' yaz
Result = [x if x % 2 == 0 else 'Tek' for x in range(1, 10)]
print(Result)


# ================================
# NESTED FOR (İÇ İÇE DÖNGÜ)
# ================================
# Tüm (x, y) ikililerini tuple halinde oluşturur
result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))
print(result)

# aynı işlemi list comprehension ile tek satırda da yazabilirdik:
# result = [(x, y) for x in range(3) for y in range(3)]

result =[(x,y) for x in range (3) for y in range(3)]
print(result)



#  SAYI TAHMİNİ UYGULAMSI

# 1-100 ARASINDA RASTGELE ÜRETİLECEK BİR SAYIYI AŞAĞI YUKARI
# İFADELERİ İLE BULDURMAYA ÇALIŞIN HAK = 5
# RANDOM MODÜLÜ İÇİN PYTHON RANDOM ŞEKLİNDE ARAMA YAP
# 100 ÜZERİNDEN PUANLAMA YAP HER SORU 20 PUAN
# HAK BİLGİSİNİ KULLANICIDAN ALIN VE HER SORU BELİRTİLEN CAN SAYISI ÜZERİNDEN HESAPLANSIN

# SAYI TAHMİNİ UYGULAMASI

import random

# Bilgisayar 1-100 arasinda rastgele bir sayi secer
sayi = random.randint(1, 100)

# Kullanicidan kac hakki olacagini al
can = int(input('Kac hakta bilmek istersiniz: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Tahmininiz: '))

    if sayi == tahmin:
        # Puan hesaplama: 100 uzerinden, her yanlistra dusuyor
        puan = 100 - (100 // can) * (sayac - 1)
        print(f'Tebrikler! {sayac}. denemede bildiniz. Puaniniz: {puan}')
        break
    elif sayi > tahmin:
        print('Daha yukari cikin ⬆️')
    else:
        print('Daha asagi inin ⬇️')

    if hak == 0:
        print(f'Hakkiniz bitti! Tutulan sayi: {sayi}')



#  GİRİLEN SAYININ ASAL OLUP OLMADIĞINI KONTROL EDİNİZ.
#  ASAL SAYI 1 VE KENDİSİNE HARİÇ TAM BÖLENİ OLMAYAN SAYILARA DENİR

girilensayi = int(input('sayi: '))
asalmi=True

if girilensayi == 1:
    print('girilensayi asal değildir')

for i in range(2,girilensayi):
    if (girilensayi%i) ==0 :
        asalmi=False
        break
if asalmi:
    print('girilen sayi asaldir')

else:
    print('girilen sayi asal değildir')





# ---------------- PYTHONDA METODLAR ---------------- #

# Liste metodları
mylist = [1, 2, 3]
mylist.append(4)    # sona 4 ekler
mylist.pop()        # son elemanı siler
print(type(mylist))
print(mylist)

# String metodları
mystring = 'hello'
print(mystring.upper())   # HELLO (orijinali değişmez)
print(type(mystring))


# ---------------- FONKSİYONLAR ---------------- #


# Parametreli ve parametresiz fonksiyon
def sayhello(name='user'):
    print('hello ' + name)

sayhello()
sayhello('fatih')



# Fonksiyon return ile değer döndürür
def sayhello(name='user'):
    return 'hello ' + name

msg = sayhello('batuhan')
print(msg)



# Toplama fonksiyonu
def total(num1, num2):
    return num1 + num2

result = total(10, 20)
print(result)



# Yaş hesaplama fonksiyonu
def yashesapla(dogumyili):
    return 2025 - dogumyili

agebatu = yashesapla(2000)
ageibo = yashesapla(2002)
print(agebatu, ageibo)



# Emeklilik hesaplama (yaşa göre)
def emeklilige_kac_yil(yaş):
    return 65 - yaş

agemustafa = emeklilige_kac_yil(52)
agefatih = emeklilige_kac_yil(21)
print(agemustafa, agefatih)



# Emeklilik hesaplama (doğum yılına göre)
def emeklilige_kac_yil_kaldi(dogumyili, isim):
    yas = yashesapla(dogumyili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'{isim}, emekliliğinize {emeklilik} yil kaldi.')
    elif emeklilik == 0:
        print(f'{isim}, bu yil emekli olabilirsiniz!')
    else:
        print(f'{isim}, zaten emeklisiniz.')

emeklilige_kac_yil_kaldi(1973, 'mustafa')
emeklilige_kac_yil_kaldi(1960, 'ahmet')
emeklilige_kac_yil_kaldi(2004, 'fatih')



# -------------------------------
# Fonksiyon Parametreleri Örnekleri
# -------------------------------

# 1- Immutable (değiştirilemez tipler: str, int, tuple vs.)
def changename(n):
    n = 'emre'   # sadece n değişir, dışarıya etki etmez

name = 'yiğit'
changename(name)
print("Immutable örneği:", name)   # yiğit


# 2- Mutable (değiştirilebilir tipler: list, dict, set vs.)
def change(n):
    n[0] = 'antalya'

sehirler = ['ankara', 'istanbul', 'edirne']
change(sehirler)
print("Mutable örneği:", sehirler)   # ['antalya', 'istanbul', 'edirne']


# 3- Varsayılan parametreler
def add(a, b, c=0, d=0):
    return sum((a, b, c, d))

print("Varsayilan parametre örneği:")
print(add(10, 20))          # 30
print(add(10, 20, 30))      # 60
print(add(10, 20, 30, 40))  # 100


# 4- Sınırsız parametre (*args)
def add_all(*args):
    return sum(args)

print("args örneği:")
print(add_all(10, 20))                  # 30
print(add_all(10, 20, 30, 40, 50))      # 150


# 5- Anahtar=Değer parametreleri (**kwargs)
def displayuser(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")

print("kwargs örneği:")
displayuser(name='ibo', age=7, city='kocaeli')
displayuser(name='samet', age=10, city='malatya', phone='15125145')


# 6- Hem *args hem **kwargs
def func(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

print("Hem args hem kwargs örneği:")
func(10, 20, 30, name="fatih", city="istanbul")



# =====================================================
# 📘 FONKSİYON UYGULAMALARI (AÇIKLAMALI)
# =====================================================

# -----------------------------------------------------
# 1️⃣ Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyon
# -----------------------------------------------------

# Bir kelimeyi ekranda kaç defa yazdırmak istiyorsak, 
# kelime ve adet parametresini fonksiyona gönderiyoruz.

def yazdir(kelime, adet):
    for i in range(adet):      # 0'dan başlayıp 'adet' kadar döner
        print(kelime)          # Her döngüde kelimeyi ekrana yazar

# Fonksiyonu çağırıyoruz:
yazdir('merhaba', 10)          # "merhaba" kelimesi 10 defa ekrana yazılır



# -----------------------------------------------------
# 2️⃣ Kendisine gönderilen sınırsız sayıdaki parametreyi listeye çeviren fonksiyon
# -----------------------------------------------------

# '*' işareti sayesinde fonksiyona sınırsız parametre gönderebiliriz.
# Bu parametreler tuple (demet) olarak gelir, biz de listeye çeviririz.

def listeyecevir(*params):
    return list(params)        # tuple → liste

# Fonksiyonu çağırıyoruz:
result = listeyecevir(10, 20, 30, 'merhaba')
print(result)   # [10, 20, 30, 'merhaba']


# -----------------------------------------------------
# 3️⃣ Gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyon
# -----------------------------------------------------

# Asal sayı: Kendisine ve 1'e bölünebilen, başka böleni olmayan sayıdır.
# Örn: 2, 3, 5, 7, 11, 13 ...

def asalsayilaribul(x, y):
    for sayi in range(x, y+1):                 # x ile y arasındaki sayılar
        if sayi > 1:                           # asal sayılar 1'den büyük
            for i in range(2, int(sayi**0.5)+1):  # sadece kareköküne kadar kontrol et
                if sayi % i == 0:              # bir bölen bulunursa asal değildir
                    break
            else:
                print(sayi)                    # bölen bulunmazsa asal sayıdır

# Fonksiyonu çağırıyoruz:
x = int(input('sayi1: '))
y = int(input('sayi2: '))
asalsayilaribul(x, y)


# -----------------------------------------------------
# 4️⃣ Kendisine gönderilen sayının tam bölenlerini bir liste haline getiren fonksiyon
# -----------------------------------------------------

# Tam bölen: Sayıyı kalansız bölen sayılardır. 
# Örn: 20 → 1, 2, 4, 5, 10, 20

def tambolenleribul(sayi):
    tambolenler = []
    for i in range(1, sayi+1):       # 1'den başlayıp sayının kendisine kadar kontrol et
        if sayi % i == 0:            # eğer kalansız bölünüyorsa
            tambolenler.append(i)    # listeye ekle
    return tambolenler

# Fonksiyonu çağırıyoruz:
print(tambolenleribul(20))    # [1, 2, 4, 5, 10, 20]
 


# ----------------------------
# MAP ile normal fonksiyon
# ----------------------------
def square(num):           # num sayısının karesini hesaplayan fonksiyon
    return num**2

numbers = [1, 9, 7, 3]
result = list(map(square, numbers))  # map ile tüm elemanlara square fonksiyonu uygulanır
print(result)  # [1, 81, 49, 9]



# ----------------------------
# MAP ile lambda fonksiyonu direkt
# ----------------------------
numbers = [1, 4, 5, 3]
result = list(map(lambda num: num**2, numbers))  # lambda ile tek satırda kare alma
print(result)  # [1, 16, 25, 9]



# ----------------------------
# Lambda fonksiyonunu değişkene atayıp map ile kullanma
# ----------------------------
numbers = [1, 9, 0, 5]
square = lambda num: num**2   # lambda fonksiyonunu değişkene atadık
result = list(map(square, numbers))  # map ile uyguladık
print(result)  # [1, 81, 0, 25]



# ----------------------------
# Lambda fonksiyonunu direkt çağırma
# ----------------------------
numbers = [1, 3, 5, 9]
square = lambda num: num**2
result = square(3)  # direkt bir sayı üzerinde çalıştırdık
print(result)  # 9



# ----------------------------
# FILTER ile normal fonksiyon
# ----------------------------
numbers = [1, 3, 5, 9, 10, 4]

def check_even(num):  # sayının çift olup olmadığını kontrol eden fonksiyon
    return num % 2 == 0

result = list(filter(check_even, numbers))  # filter ile çift sayıları seçtik
print(result)  # [10, 4]



# ----------------------------
# FILTER ile lambda fonksiyonu
# ----------------------------
numbers = [1, 3, 5, 9, 10, 4]
result = list(filter(lambda num: num % 2 == 0, numbers))  # lambda ile tek satırda filtreleme
print(result)  # [10, 4]
 
 

# 🌍 Global ve 🔒 Local Değişkenler

# ------------------------------
# 1️⃣ Global ve Local örneği
# ------------------------------


# Global değişken tanımlıyoruz (her yerden erişilebilir)
name = 'fatih'

def changename(new_name):
    # Bu satırda 'name' değişkeni fonksiyon içinde yeniden tanımlanıyor.
    # Yani burada 'name' artık local (yerel) bir değişkendir.
    name = new_name
    print(name)   # Bu, local değişkendeki değeri yazdırır.

# Fonksiyonu çağırıyoruz
changename('emre')  # Fonksiyon içinde 'emre' yazdırılır
print(name)         # Ama global 'name' değişmedi, hâlâ 'fatih' yazdırılır.


# 📘 Çıktı:
# emre
# fatih


# ------------------------------
# 2️⃣ İç içe fonksiyon (LEGB kuralı)
# ------------------------------

name = 'global string'

def greeting():
    # Bu fonksiyon içinde yeni bir local değişken tanımlanıyor
    name = 'mehmet'
    
    def hello():
        # İçteki fonksiyon (nested function) dıştaki local değişkeni kullanabilir
        print('hello ' + name)
    
    hello()  # İçteki fonksiyon çağrılır

# Dış fonksiyon çağrılır
greeting()


# 📘 Çıktı:
# hello mehmet



# ------------------------------
# 3️⃣ Fonksiyon parametresi (local değişken)
# ------------------------------

x = 50

def test(x):
    print(f'x: {x}')  # Parametre olarak gelen değeri (50) yazdırır
    
    x = 100           # Local olarak x'in değeri değiştirilir (global etkilenmez)
    print(f'changed x to {x}')  # 100 yazdırılır

# Fonksiyon çağrılır
test(x)
print(x)  # Global x değişmedi, hâlâ 50


# 📘 Çıktı:
# x: 50
# changed x to 100
# 50



# ------------------------------
# 4️⃣ Global anahtar kelimesi kullanımı
# ------------------------------

x = 50

def test():
    # Bu satır Python’a, bu fonksiyonun global 'x' değişkenini kullanacağını söyler
    global x  
    print(f'x: {x}')  # Global x = 50
    
    # Global değişkenin değerini değiştiriyoruz
    x = 100
    print(f'changed x to {x}')  # Artık x = 100

# Fonksiyon çağrılır
test() 
print(f'Final x: {x}')  # Global x değiştiği için 100 yazdırılır


# 📘 Çıktı:
# x: 50
# changed x to 100
# Final x: 100



# ------------------------------
# 🧠 Özet:
# ------------------------------
# Fonksiyon içinde aynı isimli değişken tanımlanırsa → Local olur, global etkilenmez.
# Fonksiyon parametresi de local kabul edilir.
# "global" anahtar kelimesi kullanılırsa → Global değişken direkt değiştirilir.
# İç içe fonksiyonlarda → Python LEGB (Local, Enclosing, Global, Built-in) sırasına göre arama yapar.



#  BANKAMATİK UYGULAMSI

# Fatih'in hesabını temsil eden sözlük (dictionary)
FatihHesap = {
    'ad': 'Fatih Öztürk',   # Hesap sahibinin adı
    'hesapNo': '12345678',  # Hesap numarası
    'bakiye': 3000,         # Ana hesaptaki para miktarı
    'ekHesap': 2000         # Ek hesap (kredi gibi düşünülebilir)
}

# İbrahim'in hesabını temsil eden sözlük (dictionary)
IbrahimHesap = {
    'ad': 'ibrahim culfa',  # Hesap sahibinin adı
    'hesapNo': '87654321',  # Hesap numarası
    'bakiye': 5000,         # Ana hesaptaki para miktarı
    'ekHesap': 3200         # Ek hesap limiti
}

# Para çekme işlemini gerçekleştiren fonksiyon
def paracek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")  # Kullanıcıya adıyla selamlama
    
    # Eğer hesaptaki para, çekilmek istenen miktardan fazlaysa
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar  # Bakiyeden para düşülür
        print('Paranizi alabilirsiniz.')  # Kullanıcıya bilgi verilir
        
    else:
        # Eğer ana bakiyede para yetmiyorsa, ek hesapla birlikte toplam bakiyeyi hesapla
        toplam = hesap['bakiye'] + hesap['ekHesap']
        
        # Toplam para çekilmek istenen miktardan fazlaysa
        if (toplam >= miktar):
            # Kullanıcıya ek hesabı kullanmak isteyip istemediği sorulur
            ekHesapkullanimi = input('Ek hesap kullanilsin mi (e/h): ')
            
            # Eğer kullanıcı 'e' (evet) derse
            if ekHesapkullanimi == 'e':
                # Ne kadar ek hesaptan kullanılacağı hesaplanır
                ekHesapkullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0  # Ana hesap sıfırlanır
                hesap['ekHesap'] -= ekHesapkullanilacakMiktar  # Ek hesaptan kalan para düşülür
                print('Paranizi alabilirsiniz.')  # İşlem tamam mesajı
            else:
                # Kullanıcı ek hesap kullanmak istemediyse uyarı verilir
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir.")
        else:
            # Ne ana hesap ne de ek hesap yeterliyse
            print('Üzgünüz, bakiye yetersiz.')  # Kullanıcıya bilgi verilir
            

# Hesaptaki mevcut bakiye ve ek hesap limitini gösteren fonksiyon
def bakiyesorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir. "
          f"Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadir.")

# 1. işlem: Fatih hesabından 3000 TL çekiliyor
paracek(FatihHesap, 3000)
# 1. işlem sonrası bakiye kontrolü
bakiyesorgula(FatihHesap)

print('************')  # Görsel ayrım için

# 2. işlem: Fatih hesabından 2000 TL daha çekiliyor
paracek(FatihHesap, 2000)
# 2. işlem sonrası bakiye kontrolü
bakiyesorgula(FatihHesap)




# NESNE TABANLI PROGRAMLAMA (OOP) NEDİR?
# =======================================
# OOP, yazılımı daha düzenli ve yönetilebilir hale getirmek için 
# nesneler (object) ve sınıflar (class) etrafında tasarlanan bir programlama yaklaşımıdır.
# Bu sayede veriler (özellikler) ve işlevler (metotlar) bir arada tutulur.


# Basit bir liste örneği
list1 = [1, 2, 3]
list2 = [1, 2, 3, 4]

# 'type()' fonksiyonu, bir değişkenin veri tipini döndürür.
result = type(list1)
print(result)  # <class 'list'> çıktısını verir, yani bu bir "liste" nesnesidir.


# ================================
# CLASS (Sınıf) Tanımlama Örneği
# ================================
# Sınıf (class): Nesnelerin nasıl oluşturulacağını tanımlar.
# Örnek: "Person" sınıfı, bir insanı temsil eder (adı, doğum yılı, adres gibi özelliklerle).


class Person:

    # --- Sınıf (Class) Özellikleri ---
    # Bunlar tüm nesneler (object) için ortaktır.
    address = 'no information'  # Her kişi için varsayılan adres bilgisi

    # --- Yapıcı Metot (Constructor) ---
    # "__init__" metodu, yeni bir nesne oluşturulurken otomatik olarak çalışır.
    def __init__(self, name, year):
        # "self" => sınıftan oluşturulan nesneyi temsil eder.
        # Bu sayede her nesnenin kendi özellikleri olur.
        self.name = name
        self.year = year
        print(f'init metodu çalıştı -> {self.name} adlı kişi oluşturuldu.')

    # --- Metotlar ---
    # Metotlar, sınıfın davranışlarını (işlevlerini) tanımlar.
    
    # Yaş hesaplayan örnek metot:
    def calculateAge(self, current_year):
        return current_year - self.year


# ====================================
# NESNE (OBJECT) OLUŞTURMA
# ====================================

# Person sınıfından iki farklı kişi oluşturduk.
p1 = Person('Fatih', 2003)
p2 = Person('Yağmur', 2005)

# Nesnelerin (object) özelliklerine erişim:
print(f'name: {p1.name}, year: {p1.year}, address: {p1.address}')
print(f'name: {p2.name}, year: {p2.year}, address: {p2.address}')

# Sınıf türünü öğrenelim
print(type(p1))  # <class '__main__.Person'>
print(type(p2))  # <class '__main__.Person'>

# Metot (fonksiyon) kullanımı
print(f"{p1.name} adlı kişinin yaşı: {p1.calculateAge(2025)}")
print(f"{p2.name} adlı kişinin yaşı: {p2.calculateAge(2025)}")


# ====================================
# CLASS ATTRIBUTES ve OBJECT ATTRIBUTES FARKI
# ====================================
# Class attribute: Tüm nesneler tarafından paylaşılan ortak bilgi (örneğin address)
# Object attribute: Her nesneye özel bilgi (örneğin name, year)

# Class attribute'ü değiştirme (tüm nesneleri etkiler)
Person.address = "Türkiye"

print(f"{p1.name} adresi: {p1.address}")
print(f"{p2.name} adresi: {p2.address}")

# Ancak sadece bir nesneye özel olarak değiştirilirse, sadece o nesne etkilenir:
p1.address = "İstanbul"

print(f"{p1.name} adresi (özel): {p1.address}")
print(f"{p2.name} adresi (hala class değeri): {p2.address}")



# Üst sınıf (Base Class)
class Person():
    def __init__(self, fname, lname):
        self.FirstName = fname
        self.LastName = lname
        print('Person created')
        
    def who_am_i(self):
        print('I am a person')
        
    def eat(self):
        print('I am eating')


# Alt sınıf (Derived Class)
# Student sınıfı Person sınıfından türetiliyor.
class Student(Person):
    def __init__(self, fname, lname):
        # Üst sınıfın yapıcı metodunu çağırıyoruz
        Person.__init__(self, fname, lname)
        print('Student created')


# Nesneleri oluşturalım
p1 = Person('Deniz', 'İbo')
s1 = Student('Fatih', 'Mehmet')

# Her iki sınıfta da ad ve soyad bilgileri geldi.
print(p1.FirstName + ' ' + p1.LastName)
print(s1.FirstName + ' ' + s1.LastName)

# Metotları çağıralım
p1.who_am_i()   # Person sınıfının metodu
s1.who_am_i()   # Student sınıfı miras aldığı için bu metodu da kullanabilir

p1.eat()
s1.eat()


# ========================
# Built-in fonksiyon örnekleri
# ========================

myList = [1, 2, 3]
myString = 'my string'

print(len(myList))      # Listenin eleman sayısını verir → 3
print(len(myString))    # Stringin karakter sayısını verir → 9
print(type(myList))     # Listenin tipi → <class 'list'>
print(type(myString))   # Stringin tipi → <class 'str'>


# ========================
# Nesne Tabanlı Programlama: Special (Magic) Methods
# ========================

class Movie:
    # Constructor → Nesne oluşturulduğunda otomatik çalışır
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie nesnesi oluşturuldu.")

    # __str__ → print() veya str() kullanıldığında dönen metin
    def __str__(self):
        return f"{self.title} by {self.director}"

    # __len__ → len() fonksiyonunun nesne üzerindeki davranışı
    def __len__(self):
        return self.duration

    # __del__ → Nesne silindiğinde çalışan metot
    def __del__(self):
        print("Movie nesnesi silindi.")


# ========================
# Nesne oluşturma ve kullanım
# ========================

m = Movie("Film Adı", "Yönetmen Adı", 120)

print(str(m))     # __str__ çalışır → Film Adı by Yönetmen Adı
print(len(m))     # __len__ çalışır → 120




# ========================
# Question Sınıfı
# ========================

class Question:
    def __init__(self, text, choices, answer):
        self.text = text            # Soru metni
        self.choices = choices      # Şıklar listesi
        self.answer = answer        # Doğru cevap
    
    def checkAnswer(self, answer):
        return self.answer == answer   # Kullanıcının cevabı doğru mu?


# ========================
# Quiz Sınıfı
# ========================

class Quiz:
    def __init__(self, questions):
        self.questions = questions      # Soru listesi
        self.score = 0                  # Başlangıç skoru
        self.questionIndex = 0          # Kaçıncı soruda olduğumuz
    
    def getQuestion(self):
        # Mevcut soruyu döndürür
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        # Ekrena soruyu yazdırır
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")
        
        for choice in question.choices:
            print("- " + choice)
        
        answer = input("Cevap: ")
        self.guess(answer)          # Kullanıcı cevabını kontrol et
        self.loadQuestion()         # Sonraki soruya geç
    
    def guess(self, answer):        # ← quess yerine guess düzeltildi
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 1         # Doğruysa puan artır
        
        self.questionIndex += 1     # Sonraki soruya geç
    
    def loadQuestion(self):
        # Sorular bittiyse sonucu göster, bitmediyse devam et
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()
    
    def showScore(self):
        # Toplam skoru ekrana yaz
        print("Quiz Bitti!")
        print("Toplam Skor:", self.score)


# ========================
# Soru Listesi
# ========================

q1 = Question("En iyi programlama dili hangisidir?", ["python", "javascript", "java"], "python")
q2 = Question("En popüler programlama dili hangisidir?", ["python", "javascript", "java"], "python")
q3 = Question("En çok kazandıran programlama dili hangisidir?", ["python", "javascript", "java"], "python")

questions = [q1, q2, q3]

# ========================
# Quiz Başlatma
# ========================

quiz = Quiz(questions)
quiz.displayQuestion()




# ========================
# HAZIR MODÜL KULLANIMI - MATH
# ========================

import math

print(dir(math))             # math modülündeki fonksiyon ve değişkenleri listeler
# help(math)                # math modülünün dökümantasyonunu gösterir
# help(math.factorial)      # factorial fonksiyonunun açıklaması

print(math.sqrt(36))         # 6.0
print(math.factorial(7))     # 5040
print(math.ceil(13.5))       # 14


# ========================
# AS ile takma isim verme
# ========================

import math as islem
print(islem.factorial(5))     # 120


# ========================
# from math import *
# ========================

from math import *

print(factorial(5))           # 120
print(sqrt(36))               # 6.0


# ========================
# RANDOM MODÜLÜ
# ========================

import random

print(dir(random))            # random modülündeki fonksiyonların listesi
# help(random)               # random modülü dökümantasyonu

print(random.random())        # 0.0–1.0 arası bir sayı
print(random.random() * 100)  # 0–100 arası bir sayı

print(random.uniform(1, 10))  # 1–10 arası float sayı
print(int(random.uniform(1, 10)))  # 1–10 arası tam sayı

print(random.randint(1, 100)) # 1–100 arası integer


names = ['ege', 'mehmet', 'samet', 'fatih']
print(random.choice(names))   # listedeki rastgele bir isim seçer


# Eksik olan 'greeting' listesi burada tanımlandı
greeting = ['selam', 'merhaba', 'naber', 'iyi misin']
print(random.choice(greeting))  # rastgele selamlaşma


# ========================
# LİSTE KARIŞTIRMA (shuffle)
# ========================

liste = list(range(10))       # [0,1,2,3,4,5,6,7,8,9]
random.shuffle(liste)         # listeyi karıştırır

print(liste)                  # karışmış hali




# ======================================
# module.py   (MODÜL DOSYASI)
# ======================================

"""
Bu modül örnek bir Python modülüdür.
İçerisinde değişkenler, fonksiyonlar ve bir sınıf bulunur.
"""

print("Modül eklendi.")     # Modül import edildiğinde 1 kere çalışır.

# --- Değişkenler ---
number = 10
numbers = [1, 2, 3]

person_info = {
    "name": "fatih",
    "age": 21,
    "city": "istanbul"
}

# --- Fonksiyon ---
def func(x):
    """
    Bu fonksiyon kendisine verilen x değerini ekrana yazirir.
    """
    print(f"x: {x}")

# --- Sınıf ---
class Person:
    def speak(self):
        print("I am speaking...")


# ======================================
# main.py   (MODÜLÜ KULLANAN DOSYA)
# ======================================

import module   # module.py dosyasını içeri aktarır

# --- Modül değişkenlerini kullanma ---
print(module.number)
print(module.numbers)
print(module.person_info)

# --- Modül içindeki fonksiyon ---
module.func(50)

# --- Modül içindeki sınıf ---
p = module.Person()
p.speak()




# =====================================================
# PYTHON DOSYA OLUŞTURMA, OKUMA VE GÜNCELLEME
# =====================================================

# open(dosya_adi, dosya_erişme_modu, encoding)
# Dosya erişme modları:
# "w" : write → dosya oluşturur / varsa silip yeniden yazar
# "a" : append → dosya yoksa oluşturur, varsa sona ekler
# "x" : create → dosya varsa hata verir
# "r" : read → okuma modu (varsayılan)
# "r+" : okuma + yazma

# =====================================================
# DOSYA OKUMA (try-except-finally)
# =====================================================

try:
    file = open("newfile2.txt", "r", encoding="utf-8")
    print("Dosya başarıyla açıldı.")
    print(file.read())

except FileNotFoundError:
    print("Dosya bulunamadı!")

finally:
    print("Dosya kapatıldı.")
    if 'file' in locals():
        file.close()


# =====================================================
# DOSYA OKUMA – FOR DÖNGÜSÜ
# =====================================================

file = open("newfile.txt", "r", encoding="utf-8")

# Dosya satır satır okunur
for satir in file:
    print(satir, end="")

file.close()


# =====================================================
# DOSYA OKUMA – read() METODU
# =====================================================

file = open("newfile.txt", "r", encoding="utf-8")

content = file.read()  # Dosyanın tamamını okur
print(content)

file.close()


# =====================================================
# with BLOĞU İLE DOSYA OKUMA
# (Dosya otomatik kapanır)
# =====================================================

with open("newfile.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

    file.seek(10)      # İmleci 10. karaktere götürür
    print(file.tell()) # Mevcut imleç konumu

    content2 = file.read()
    print(content2)


# =====================================================
# DOSYA GÜNCELLEME (ORTADAN YAZMA)
# =====================================================

with open("newfile.txt", "r+", encoding="utf-8") as file:
    file.seek(20)      # 20. karakterden itibaren
    file.write("deneme")


# =====================================================
# DOSYA BAŞINDAN YAZMA
# (Var olan içeriğin üstüne yazar)
# =====================================================

with open("newfile.txt", "r+", encoding="utf-8") as file:
    file.write("deneme")


# =====================================================
# DOSYA SONUNA EKLEME
# =====================================================

with open("newfile.txt", "a", encoding="utf-8") as file:
    file.write("\nFatih Öztürk")


# =====================================================
# DOSYA BAŞINA EKLEME
# (Önce okunur, sonra yeniden yazılır)
# =====================================================

with open("newfile.txt", "r+", encoding="utf-8") as file:
    content = file.read()
    file.seek(0)
    file.write("Batuhan Öztürk\n" + content)


# =====================================================
# DOSYA ORTASINA SATIR EKLEME
# =====================================================

with open("newfile.txt", "r+", encoding="utf-8") as file:
    satirlar = file.readlines()   # Tüm satırlar liste olur
    satirlar.insert(1, "İbrahim Culfa\n")  # 2. satıra ekleme

    file.seek(0)
    for satir in satirlar:
        file.write(satir)




# ===============================
# FONKSİYONLARDA İÇ İÇE KULLANIM
# ===============================

# Basit bir fonksiyon tanımı
def greeting(name):
    # Parametre olarak gelen ismi ekrana yazdırır
    print('hello', name)

# Fonksiyon çağrılır
# return olmadığı için None döner
print(greeting('ali'))  # çıktı: hello ali -> None

# Fonksiyonun kendisi (çalıştırılmaz)
print(greeting)  # <function greeting at ...>


# Fonksiyon başka bir değişkene atanabilir
sayHello = greeting

# sayHello artık greeting fonksiyonunu temsil eder
print(sayHello)  # <function greeting at ...>
print(greeting)  # <function greeting at ...>


# ===============================
# ENCAPSULATION (İÇ İÇE FONKSİYON)
# ===============================

def outer(num1):
    print('outer')  # dış fonksiyonun çalıştığını gösterir
    
    # outer fonksiyonuna özel iç fonksiyon
    def inner_increment(num1):
        # Gelen değeri 1 artırır
        return num1 + 1
    
    # inner fonksiyon outer içinde çağrılır
    num2 = inner_increment(num1)
    
    # İlk ve artırılmış değer yazdırılır
    print(num1, num2)

# outer fonksiyon çağrılır
outer(10)
# çıktı:
# outer
# 10 11


# ===============================
# FACTORIAL (İÇ İÇE + RECURSIVE)
# ===============================

def factorial(number):
    # Parametrenin int olup olmadığı kontrol edilir
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    
    # Sayı negatif mi kontrol edilir
    if number < 0:
        raise ValueError("number must be zero or positive")
    
    # İç içe tanımlanan recursive fonksiyon
    def inner_factorial(number):
        # 0 ve 1 için faktöriyel sonucu 1’dir
        if number <= 1:
            return 1
        
        # Recursive çağrı
        return number * inner_factorial(number - 1)
    
    # Dış fonksiyon inner fonksiyonu çağırır
    return inner_factorial(number)


# ===============================
# HATA YAKALAMA (try - except)
# ===============================

try:
    # Hatalı tip gönderiyoruz (string)
    print(factorial("4"))
except Exception as ex:
    # Oluşan hata mesajı yazdırılır
    print(ex)

# Doğru kullanım örneği
print(factorial(4))  # çıktı: 24




# ===============================
# FONKSİYONDAN FONKSİYONA DÖNDÜRME
# (Closure Kullanımı)
# ===============================

def usalma(number):
    # Dış fonksiyon parametresi: number
    
    def inner(power):
        # İç fonksiyon dış fonksiyondaki number'a erişebilir
        return number ** power
    
    # inner fonksiyonunu geri döndürüyoruz
    return inner


# usalma fonksiyonu çağrılır ve inner fonksiyon elde edilir
two = usalma(2)    # number = 2
three = usalma(3)  # number = 3

# inner fonksiyonlar çalıştırılır
print(two(3))      # 2**3 = 8
print(three(4))    # 3**4 = 81


# ===============================
# YETKİ SORGULAMA (CLOSURE ÖRNEĞİ)
# ===============================

def yetki_sorgula(page):
    # page bilgisi dış fonksiyona aittir
    
    def inner(role):
        # Kullanıcının rolüne göre yetki kontrolü
        if role == 'Admin':
            return "{0} rolü {1} sayfasina ulaşabilir".format(role, page)
        else:
            return "{0} rolü {1} sayfasina ulaşamaz".format(role, page)
    
    # inner fonksiyonu geri döndürülür
    return inner


# yetki_sorgula fonksiyonundan inner fonksiyon elde edilir
user1 = yetki_sorgula("Product Edit")

# inner fonksiyon çağrılır
print(user1("Admin"))
print(user1("User"))





# ===============================
# FUNCTION AS PARAMETERS
# (Fonksiyonları parametre olarak gönderme)
# ===============================

# Toplama fonksiyonu
def toplama(a, b):
    return a + b

# Çıkarma fonksiyonu
def cikarma(a, b):
    return a - b   # HATA DÜZELTİLDİ (çarpma değil çıkarma)

# Bölme fonksiyonu
def bolme(a, b):
    return a / b

# Çarpma fonksiyonu
def carpma(a, b):
    return a * b


# Fonksiyonları parametre olarak alan ana fonksiyon
def islem(f1, f2, f3, f4, islem_adi):
    
    if islem_adi == "toplama":
        print(f1(2, 3))      # toplama(2,3)
    
    elif islem_adi == "cikarma":
        print(f2(5, 3))      # cikarma(5,3)
    
    elif islem_adi == "carpma":
        print(f3(3, 4))      # carpma(3,4)
    
    elif islem_adi == "bolme":
        print(f4(10, 2))     # bolme(10,2)
    
    else:
        print("geçersiz işlem")


# Fonksiyonlar parametre olarak gönderilir
islem(toplama, cikarma, carpma, bolme, "toplama")




# ===============================
# PYTHON'DA DECORATOR FONKSİYON
# ===============================

# Decorator tanımı
def my_decorator(func):
    
    # func fonksiyonunu saran wrapper
    def wrapper():
        print("fonksiyondan önce işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    
    # wrapper fonksiyonu geri döndürülür
    return wrapper


# Normal fonksiyon
def sayHello():
    print("hello")


# Başka bir normal fonksiyon
def sayGreeting():
    print("greeting")


# Decorator manuel olarak uygulanır
sayHello = my_decorator(sayHello)

# ❌ HATA DÜZELTİLDİ
# sayGreeting = my_decorator(sayHello) YANLIŞTI
# Doğrusu kendi fonksiyonunu sarması
sayGreeting = my_decorator(sayGreeting)

# Fonksiyonlar çağrılır
sayHello()
sayGreeting()


# ===============================
# @ DECORATOR SÖZ DİZİMİ (DOĞRU VE TEMİZ KULLANIM)
# ===============================

def my_decorator(func):
    def wrapper():
        print("fonksiyondan önce işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    return wrapper


# @ işareti decorator'ü otomatik uygular
@my_decorator
def sayHello():
    print("hello")

# Decorator'lü fonksiyon çağrılır
sayHello()


# ===============================
# ZAMAN ÖLÇEN DECORATOR (GERÇEK KULLANIM)
# ===============================

import math
import time


# Zaman ölçen decorator
def zaman_hesapla(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        
        # Asıl fonksiyon çalışır
        func(*args, **kwargs)
        
        finish = time.time()
        print("fonksiyon " + str(finish - start) + " saniye sürdü.")
    return wrapper


# Üs alma fonksiyonu
@zaman_hesapla
def usalma(a, b):
    time.sleep(1)  # işlemi yavaşlatmak için
    print(math.pow(a, b))


# Faktöriyel fonksiyonu
@zaman_hesapla
def faktoriyel(num):
    time.sleep(1)
    print(math.factorial(num))


# Fonksiyon çağrıları
usalma(2, 5)
faktoriyel(5)




# ===============================
# PYTHON'DA ITERATOR (İTERATÖRLER)
# ===============================

# -------------------------------
# 1️⃣ Liste üzerinden iterator oluşturma
# -------------------------------

liste = [1, 2, 3, 4, 5]

# iter() ile iterator elde edilir
iterator = iter(liste)

# next() ile sıradaki eleman alınır
print(next(iterator))  # 1


# -------------------------------
# 2️⃣ next() ile adım adım ilerleme
# -------------------------------

liste = [1, 2, 3, 4, 5]
iterator = iter(liste)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3


# -------------------------------
# 3️⃣ for döngüsü aslında iterator kullanır
# -------------------------------

for i in liste:
    print(i)
# for döngüsü arka planda:
# iter(liste) + next() + StopIteration kullanır


# -------------------------------
# 4️⃣ while + try-except ile manuel iterator
# -------------------------------

iterator = iter(liste)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        # Eleman kalmadığında döngü biter
        break


# ===============================
# 5️⃣ KENDİ ITERATOR SINIFIMIZI YAZMA
# ===============================

class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    # Iterator nesnesini döndürür
    def __iter__(self):
        return self

    # next() çağrıldığında çalışır
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            # Eleman kalmadığında hata fırlatılır
            raise StopIteration


# ❌ HATA DÜZELTİLDİ
# list = MyNumbers(10,20)  → list Python’un built-in tipidir
# Üzerine yazmak yanlıştır

my_list = MyNumbers(10, 20)

# for döngüsü iterator mantığıyla çalışır
for x in my_list:
    print(x)





# ==============================
# PYTHON datetime MODÜLÜ
# ==============================

# datetime modülü tarih ve saat işlemleri için kullanılır
import datetime

# datetime modülünün içindeki tüm yapı ve fonksiyonları gösterir
print(dir(datetime))


# ==============================
# datetime MODÜLÜNDEN SINIFLAR
# ==============================

# En sık kullanılan sınıflar:
# datetime -> tarih + saat
# date     -> sadece tarih
# time     -> sadece saat
from datetime import datetime, date, time


# ==============================
# SINIFLARIN İÇİNİ İNCELEME
# ==============================

# datetime sınıfının fonksiyonları
print(dir(datetime))

# date sınıfının fonksiyonları
print(dir(date))

# time sınıfının fonksiyonları
print(dir(time))


# ==============================
# ŞU ANKİ TARİH VE SAAT
# ==============================

# Sistem saatine göre şu anki tarih ve saati alır
simdi = datetime.now()
print(simdi)


# ==============================
# TARİH VE SAAT BİLGİLERİNE ERİŞİM
# ==============================

print(simdi.year)    # Yıl
print(simdi.month)   # Ay
print(simdi.day)     # Gün
print(simdi.hour)    # Saat
print(simdi.minute)  # Dakika


# ==============================
# TARİHİ STRING FORMATINA ÇEVİRME
# ==============================

# ctime -> hazır okunabilir format
print(datetime.ctime(simdi))

# strftime -> özel formatlama
print(datetime.strftime(simdi, '%Y'))          # Yıl
print(datetime.strftime(simdi, '%X'))          # Saat (HH:MM:SS)
print(datetime.strftime(simdi, '%d'))          # Gün
print(datetime.strftime(simdi, '%A'))          # Gün adı
print(datetime.strftime(simdi, '%B'))          # Ay adı
print(datetime.strftime(simdi, '%Y %B %A'))    # Özel format


# ==============================
# STRING → datetime DÖNÜŞÜMÜ
# ==============================

# Metin olarak gelen tarihi datetime nesnesine çevirir
t = "10 January 2004 hour 15:30:45"

tarih = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

print(tarih)
print(tarih.year)


# ==============================
# ÖZEL TARİH OLUŞTURMA
# ==============================

# Doğum günü örneği
birthday = datetime(2004, 1, 10)
print(birthday)


# ==============================
# TIMESTAMP İŞLEMLERİ
# ==============================

# datetime → timestamp (saniye cinsinden)
timestamp = datetime.timestamp(birthday)
print(timestamp)

# timestamp → datetime
print(datetime.fromtimestamp(timestamp))




# ==============================
# PYTHON os MODÜLÜ
# ==============================

# os modülü işletim sistemiyle (dosya, klasör, dizin) etkileşim kurmamızı sağlar
import os
import datetime


# ==============================
# os MODÜLÜNÜ TANIMA
# ==============================

# os modülünün içindeki tüm fonksiyonları gösterir
print(dir(os))

# İşletim sistemi adını verir
# 'nt'  -> Windows
# 'posix' -> Linux / Mac
print(os.name)


# ==============================
# DİZİN (KLASÖR) İŞLEMLERİ
# ==============================

# Aktif dizini C:\ yapar
os.chdir("C:\\")

# Bulunduğun dizinden iki üst dizine çıkar
os.chdir("../..")


# ==============================
# KLASÖR OLUŞTURMA
# ==============================

# Tek bir klasör oluşturur
os.mkdir("newdirectory")

# İç içe klasörler oluşturur
os.makedirs("C:\\newdirectory\\yeniklasor")


# ==============================
# KLASÖR / DOSYA ADI DEĞİŞTİRME
# ==============================

# Bir dosya veya klasörün adını değiştirir
os.rename("C:\\newdirectory\\yeniklasor", "C:\\newdirectory\\yeni_ad")


# ==============================
# DOSYA VE KLASÖR LİSTELEME
# ==============================

# Belirtilen dizindeki tüm dosya ve klasörleri listeler
print(os.listdir("C:\\"))

# Aktif dizindeki sadece .py uzantılı dosyaları yazdırır
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)


# ==============================
# AKTİF DİZİNİ ÖĞRENME
# ==============================

print(os.getcwd())


# ==============================
# DOSYA BİLGİLERİ (stat)
# ==============================

# Dosya hakkında detaylı bilgi alır
dosya_bilgisi = os.stat("_datetime.py")

# Dosya boyutu (KB cinsinden)
print(dosya_bilgisi.st_size / 1024)

# Dosyanın oluşturulma zamanı
print(datetime.datetime.fromtimestamp(dosya_bilgisi.st_ctime))

# Dosyanın son erişim zamanı
print(datetime.datetime.fromtimestamp(dosya_bilgisi.st_atime))

# Dosyanın son değiştirilme zamanı
print(datetime.datetime.fromtimestamp(dosya_bilgisi.st_mtime))


# ==============================
# SİSTEM KOMUTU ÇALIŞTIRMA
# ==============================

# Windows üzerinde Not Defteri açar
os.system("notepad.exe")






# ===============================
# PYTHON re (Regular Expression) MODÜLÜ
# ===============================

import re

# re modülündeki tüm fonksiyonları ve değişkenleri listeler
result = dir(re)
print(result)


# ===============================
# ÜZERİNDE ÇALIŞACAĞIMIZ METİN
# ===============================

text = "python kursu: python programlama rehberiniz | 40 saat"


# ===============================
# re.findall()
# ===============================
# Verilen desene uyan TÜM eşleşmeleri liste olarak döndürür

result = re.findall("python", text)
print(result)          # ['python', 'python']

# Kaç tane eşleşme olduğunu bulmak için
result = len(result)
print(result)          # 2


# ===============================
# re.split()
# ===============================
# Metni belirtilen desene göre böler (liste döndürür)

result = re.split(" ", text)   # boşluklara göre ayırır
print(result)

result = re.split("R", text)   # büyük R olmadığı için bölmez
print(result)


# ===============================
# re.sub()
# ===============================
# Metindeki eşleşen ifadeyi başka bir şeyle değiştirir

result = re.sub(" ", "-", text)
print(result)


# ===============================
# re.search()
# ===============================
# İlk eşleşmeyi bulur, detaylı bilgi döndürür

result = re.search("python", text)

print(result.span())   # (0, 6) → başlangıç ve bitiş index
print(result.start())  # 0
print(result.end())    # 6
print(result.group())  # 'python'
print(result.string)   # aranan tüm string


# ===============================
# KARAKTER SETLERİ []
# ===============================
# Köşeli parantez içindeki karakterlerden BİRİ aranır

result = re.findall("[abc]", text)
print(result)

result = re.findall("[sat]", text)
print(result)

result = re.findall("[a-e]", text)
print(result)

# ^ işareti ile dışındaki karakterler
result = re.findall("[^abc]", text)
print(result)


# ===============================
# . (NOKTA)
# ===============================
# Herhangi BİR karakteri temsil eder

result = re.findall("...", text)
print(result)

result = re.findall("py..on", text)
print(result)


# ===============================
# ^ (BAŞLANGIÇ KONTROLÜ)
# ===============================
# Metin belirtilen karakterle başlıyor mu?

result = re.findall("^a", text)
print(result)

result = re.findall("^p", text)
print(result)


# ===============================
# $ (BİTİŞ KONTROLÜ)
# ===============================
# Metin belirtilen karakterle bitiyor mu?

result = re.findall("t$", text)
print(result)

result = re.findall("saat$", text)
print(result)

result = re.findall("saatt$", text)
print(result)


# ===============================
# * (0 veya daha fazla)
# ===============================
# Önündeki karakter 0 veya daha fazla olabilir

result = re.findall("sa*t", text)
print(result)


# ===============================
# + (1 veya daha fazla)
# ===============================
# Önündeki karakter EN AZ 1 kere olmalı

result = re.findall("sa+t", text)
print(result)


# ===============================
# ? (0 veya 1 kere)
# ===============================
# Önündeki karakter ya vardır ya yoktur

result = re.findall("sa?t", text)
print(result)


# ===============================
# {} (TEKRAR SAYISI)
# ===============================
# Belirli sayıda tekrar kontrolü

result = re.findall("a{2}", text)
print(result)

# 2 basamaklı sayıları bulur
result = re.findall("[0-9]{2}", text)
print(result)


# ===============================
# | (OR - ALTERNATİF)
# ===============================
# a ya da b olsun

result = re.findall("python|kursu", text)
print(result)


# ===============================
# () (GRUPLAMA)
# ===============================
# Alternatifleri gruplayarak kullanırız

result = re.findall("(python|kursu)", text)
print(result)


# ===============================
# \A ve \Z
# ===============================
# \A → string BAŞI
# \Z → string SONU

result = re.findall("\Apython", text)
print(result)

result = re.findall("saat\Z", text)
print(result)


# ===============================
# ÖZEL KARAKTERLER
# ===============================

# \d → rakamlar
result = re.findall("\d", text)
print(result)

# \D → rakam olmayanlar
result = re.findall("\D", text)
print(result)

# \s → boşluklar
result = re.findall("\s", text)
print(result)

# \S → boşluk olmayanlar
result = re.findall("\S", text)
print(result)

# \w → harf, rakam, _
result = re.findall("\w", text)
print(result)

# \W → harf, rakam, _ dışındakiler
result = re.findall("\W", text)
print(result)




#  json modülleme

person = {"name":"ali","languages":["python","C#"]}
# Python sözlüğü (dict) oluşturduk

result = person["name"]
# Sözlük içinden "name" değerini aldık

result = person["languages"]
# "languages" anahtarındaki listeyi aldık

print(result)
# languages listesini yazdırır



import json

person = '{"name":"ali","languages":["python","C#"]}'
# Bu bir JSON string (metin formatında JSON veri)


# JSON string to Dict

# ❌ HATALIYDI:
# result = json.loads(person_string)
# person_string diye bir değişken yoktu

# ✔️ DÜZELTİLDİ:
result = json.loads(person)
# JSON string → Python dict'e dönüştürülür

result = result["name"]
# Dict içinden name bilgisi alınır

result = result["languages"]
# Dict içinden languages bilgisi alınır



# ❗ Not: Dosya okumada dosya uzantısı yazmak gerekir (.json gibi)

with open("person.json") as f:
    # person.json dosyasını açar
    
    data = json.load(f)
    # Dosyadaki JSON veriyi dict'e çevirir
    
    print(data["name"])
    print(data["languages"])



person_dict = {
    "name": "ali",
    "languages": ["python","c#"]
}
# Python dict oluşturduk


result = json.dumps(person_dict)
# Python dict → JSON string'e dönüştürülür

print(result)
# JSON string çıktısı verir

print(type(result))
# Çıktının tipini gösterir (str olacaktır)




# ================================
# NUMPY TEMEL KAVRAMLAR (AÇIKLAMALI)
# ================================

# NumPy kütüphanesini projeye dahil ediyoruz
import numpy as np


# --------------------------------
# 1) PYTHON LIST OLUŞTURMA
# --------------------------------

# Normal Python listesi tanımlıyoruz
py_list = [1,2,3,4,5,6,7,8,9]

# Listenin veri tipini yazdırıyoruz
print(type(py_list))  
# <class 'list'> → Bu standart Python listesi


# --------------------------------
# 2) NUMPY ARRAY OLUŞTURMA
# --------------------------------

# NumPy array oluşturuyoruz
np_array = np.array([1,2,3,4,5,6,7,8,9])

# Veri tipini yazdırıyoruz
print(type(np_array))
# <class 'numpy.ndarray'> → NumPy'nin özel veri yapısı


# --------------------------------
# 3) ÇOK BOYUTLU YAPI (2D ARRAY)
# --------------------------------

# Python'da 2 boyutlu liste (liste içinde liste)
py_multi = [[1,2,3],[4,5,6],[7,8,9]]

# NumPy array'i 3x3 matrix haline getiriyoruz
np_multi = np_array.reshape(3,3)
# reshape() → Diziyi yeniden şekillendirir
# Toplam eleman sayısı değişmez (9 eleman var)


print(py_multi)
print(np_multi)


# --------------------------------
# 4) BOYUT SAYISI (ndim)
# --------------------------------

# ndim → kaç boyutlu olduğunu gösterir

print(np_array.ndim)
# 1 → Tek boyutlu (1D)

print(np_multi.ndim)
# 2 → 2 boyutlu (2D matrix)


# --------------------------------
# 5) SHAPE (ŞEKİL BİLGİSİ)
# --------------------------------

# shape → (satır, sütun) bilgisini verir

print(np_array.shape)
# (9,) → 9 elemanlı tek boyutlu dizi

print(np_multi.shape)
# (3,3) → 3 satır 3 sütun



# NumPy kütüphanesini projeye dahil ediyoruz
import numpy as numpy


# -------------------------------------------------
# ARRAY OLUŞTURMA METOTLARI
# -------------------------------------------------

# Listeyi NumPy array'e çevirme
result = numpy.array([1,3,5,7,9])
# Normal Python listesi yerine NumPy dizisi oluşturur.


# Belirli aralıkta sayılar üretme
result = numpy.arange(10,100,3)
# 10'dan başlar, 100'e kadar gider (100 dahil değil),
# 3'er artarak sayılar üretir.


# Sıfırlardan oluşan dizi
result = numpy.zeros(10)
# 10 elemanlı, tamamı 0 olan bir array oluşturur.


# Birlerden oluşan dizi
result = numpy.ones(10)
# 10 elemanlı, tamamı 1 olan bir array oluşturur.


# Belirli aralıkta eşit bölünmüş sayılar üretme
result = numpy.linspace(0,100,5)
# 0 ile 100 arasını 5 eşit parçaya böler.

result = numpy.linspace(0,5,5)
# 0 ile 5 arasını 5 eşit parçaya böler.


# -------------------------------------------------
# RANDOM (RASTGELE) SAYI ÜRETME
# -------------------------------------------------

result = numpy.random.randint(0,10)
# 0 ile 10 arasında (10 dahil değil) 1 rastgele tam sayı üretir.

result = numpy.random.randint(20)
# 0 ile 20 arasında 1 rastgele tam sayı üretir.

result = numpy.random.randint(1,10,3)
# 1 ile 10 arasında 3 adet rastgele tam sayı üretir.

result = numpy.random.rand(5)
# 0 ile 1 arasında 5 adet ondalıklı (float) rastgele sayı üretir.


# -------------------------------------------------
# RESHAPE (BOYUT DEĞİŞTİRME)
# -------------------------------------------------

numpy_array = numpy.arange(50)
# 0'dan 49'a kadar 50 elemanlı bir array oluşturur.

result = numpy_array.reshape(5,10)
# 50 elemanlı diziyi 5 satır 10 sütun olacak şekilde yeniden şekillendirir.


# -------------------------------------------------
# SUM (TOPLAM) - AXIS KAVRAMI
# -------------------------------------------------

numpy_array = numpy.arange(50)
numpy_multi = numpy_array.reshape(5,10)

print(numpy_multi.sum(axis=1))
# Satırları toplar (her satırın toplamını verir)

print(numpy_multi.sum(axis=0))
# Sütunları toplar (her sütunun toplamını verir)


# -------------------------------------------------
# MAX - MIN - ARGMAX - ARGMIN
# -------------------------------------------------

rnd_numbers = numpy.random.randint(1,100,10)
# 1 ile 100 arasında 10 rastgele sayı üretir.

print(rnd_numbers)

result = rnd_numbers.max()
# Dizideki en büyük değeri verir.

result = rnd_numbers.min()
# Dizideki en küçük değeri verir.

print(result)

result = rnd_numbers.argmax()
# En büyük sayının indeksini verir.

result = rnd_numbers.argmin()
# En küçük sayının indeksini verir.

print(result)





import numpy as np

# -------------------------------------------------
# 1 BOYUTLU ARRAY (TEK BOYUTLU DİZİ)
# -------------------------------------------------

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]
# 5. indeksdeki elemanı verir (indeks 0'dan başlar)
# Çıktı: 25

result = numbers[0:3]
# 0. indeksten 3. indekse kadar (3 dahil değil)
# Çıktı: [0,5,10]

result = numbers[3:]
# 3. indeksten sonuna kadar
# Çıktı: [15,20,25,50,75]

result = numbers[:]
# Baştan sona tüm elemanları verir
# Çıktı: [0,5,10,15,20,25,50,75]

result = numbers[::-1]
# Diziyi ters çevirir
# Çıktı: [75,50,25,20,15,10,5,0]



# -------------------------------------------------
# 2 BOYUTLU ARRAY (MATRİS)
# -------------------------------------------------

numbers2 = np.array([
    [0,5,10],
    [15,20,25],
    [50,75,85]
])

result = numbers2[0]
# 0. satırı verir
# Çıktı: [0,5,10]

result = numbers2[2]
# 2. satırı verir
# Çıktı: [50,75,85]

result = numbers2[0,2]
# 0. satır 2. sütun
# Çıktı: 10

result = numbers2[2,1]
# 2. satır 1. sütun
# Çıktı: 75

result = numbers2[:,2]
# Tüm satırların 2. sütunu
# Çıktı: [10,25,85]

result = numbers2[:,0:2]
# Tüm satırların 0 ve 1. sütunları
# Çıktı:
# [[0,5],
#  [15,20],
#  [50,75]]

result = numbers2[-1,:]
# Son satırın tüm sütunları
# Çıktı: [50,75,85]

result = numbers2[:2,:2]
# İlk 2 satır ve ilk 2 sütun
# Çıktı:
# [[0,5],
#  [15,20]]





# -------------------------------------------------
# NUMPY DİZİ OPERASYONLARI
# -------------------------------------------------

import numpy as np


# Rastgele sayılardan oluşan iki dizi oluşturuyoruz
numbers1 = np.random.randint(10,100,6)
# 10 ile 100 arasında 6 adet rastgele sayı üretir

numbers2 = np.random.randint(10,100,6)
# 10 ile 100 arasında 6 adet rastgele sayı üretir

print(numbers1)
print(numbers2)


# -------------------------------------------------
# ARRAY TOPLAMA
# -------------------------------------------------

result = numbers1 + numbers2
# İki dizinin aynı indekslerindeki elemanları toplar

print(result)


# -------------------------------------------------
# SAYI EKLEME (Broadcasting)
# -------------------------------------------------

result = numbers1 + 10
# Dizideki her elemana 10 ekler


# -------------------------------------------------
# ARRAY ÇARPMA
# -------------------------------------------------

result = numbers1 * numbers2
# Aynı indekslerdeki sayıları çarpar

print(result)


# -------------------------------------------------
# MATEMATİKSEL FONKSİYONLAR
# -------------------------------------------------

result = np.sin(numbers1)
# Dizideki her sayının sinüsünü alır

result = np.cos(numbers1)
# Dizideki her sayının cosinüsünü alır

result = np.sqrt(numbers1)
# Dizideki her sayının karekökünü alır

result = np.log(numbers1)
# Dizideki her sayının doğal logaritmasını alır

print(result)


# -------------------------------------------------
# RESHAPE (DİZİYİ MATRİSE ÇEVİRME)
# -------------------------------------------------

mnumbers1 = numbers1.reshape(2,3)
# 6 elemanlı diziyi 2 satır 3 sütun olacak şekilde değiştirir

mnumbers2 = numbers2.reshape(2,3)
# Aynı şekilde ikinci diziyi de matrise çevirir

print(mnumbers1)
print(mnumbers2)


# -------------------------------------------------
# MATRİS BİRLEŞTİRME
# -------------------------------------------------

result = np.vstack((mnumbers1,mnumbers2))
# Matrisleri dikey olarak birleştirir (alt alta ekler)

result = np.hstack((mnumbers1,mnumbers2))
# Matrisleri yatay olarak birleştirir (yan yana ekler)


# -------------------------------------------------
# KOŞULLU İŞLEMLER (BOOLEAN INDEXING)
# -------------------------------------------------

result = numbers1 >= 5
# Dizideki sayıların 5'ten büyük veya eşit olup olmadığını kontrol eder
# True / False sonucu döndürür

result = numbers1 % 2 == 0
# Dizideki sayıların çift olup olmadığını kontrol eder

print(result)



# Numpy uygulama

import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi
result = np.array([10, 15, 30, 45, 60])

# 2- (5-15) arasındaki sayılarla numpy dizisi
result = np.arange(5, 15)

# 3- (50-100) arasında 5'er 5'er artan dizi
result = np.arange(50, 100, 5)

# 4- 10 elemanlı sıfırlardan oluşan dizi
result = np.zeros(10)

# 5- 10 elemanlı birlerden oluşan dizi
result = np.ones(10)

# 6- (0-100) arasında eşit aralıklı 5 sayı
result = np.linspace(0, 100, 5)

# 7- (10-30) arasında rastgele 5 tane tamsayı
result = np.random.randint(10, 30, 5)

# 8- [-1 ile 1] arasında 10 adet sayı (Doğru aralık için uniform kullanıldı)
result = np.random.uniform(-1, 1, 10)

# 9- (3x5) boyutlarında (10-50) arasında rastgele matris
matris = np.random.randint(10, 50, (3, 5))

# 10- Matrisin satır ve sütun toplamları
result = matris.sum(axis=1) # Satır toplamları
result = matris.sum(axis=0) # Sütun toplamları

# 11- Matrisin en büyük, en küçük ve ortalaması
result = matris.max()
result = matris.min()
result = matris.mean()

# 12- En büyük değerin indeksi
result = matris.argmax()

# 13- (10-20) arasındaki dizinin ilk 3 elemanı
arr = np.arange(10, 20)
result = arr[:3]

# 14- Diziyi tersten yazdırma
result = arr[::-1]

# 15- Matrisin ilk satırı
result = matris[0]

# 16- Matrisin 2. satır 3. sütun elemanı
result = matris[1, 2]

# 17- Tüm satırlardaki ilk elemanlar
result = matris[:, 0]

# 18- Matrisin her bir elemanının karesi
result = matris**2

# 19- (-50, +50) arası matriste pozitif ÇİFT sayıları filtreleme
matris2 = np.random.randint(-50, 50, (3, 5))
result = matris2[(matris2 > 0) & (matris2 % 2 == 0)]

print(result)





# PANDAS KÜTÜPHANESİ - SERİLER (SERIES)

import pandas as pd  # Pandas kütüphanesini 'pd' kısaltmasıyla içe aktarıyoruz.
import numpy as np   # Matematiksel işlemler ve rastgele sayı üretimi için Numpy'ı 'np' olarak aktarıyoruz.

# --- 1. VERİ TANIMLAMALARI ---
numbers = [20, 30, 40, 50]              # Standart bir Python listesi
letters = ['a', 'b', 'c', 'd']          # String (metin) ifadelerden oluşan liste
scalar = [5]                            # Tek elemanlı bir liste (Skaler değer)
dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40} # Bir Python sözlüğü (Dictionary)
random_numbers = np.random.randint(10, 100, 6) # Numpy ile 10-100 arasında 6 tane rastgele sayı üretiyoruz.

# --- 2. PANDAS SERİSİ OLUŞTURMA YÖNTEMLERİ ---
# Not: Aşağıdaki her bir satır 'pandas_series' değişkeninin üzerine yazar,
# yani değişkenin değeri her adımda güncellenir.

pandas_series = pd.Series(numbers)      # Sadece sayılardan oluşan seri (İndeksler otomatik 0,1,2.. olur)
pandas_series = pd.Series(letters)      # Harflerden oluşan seri
pandas_series = pd.Series(scalar)       # Tek elemanlı seri
pandas_series = pd.Series(dict)         # Sözlükten seri oluşturma (Sözlük anahtarları indeks olur)
pandas_series = pd.Series(numbers, ['a', 'b', 'c', 'd']) # Veriyi ve özel indeksleri ayrı ayrı vererek seri oluşturma
pandas_series = pd.Series(random_numbers) # Numpy dizisinden seri oluşturma

# İşlemlerde kullanılacak son ve kalıcı serimiz:
# Veriler: 20, 30, 40, 50 | İndeksler: 'a', 'b', 'c', 'd'
pandas_series = pd.Series([20, 30, 40, 50], ['a', 'b', 'c', 'd'])


# --- 3. ELEMANLARA ERİŞİM (INDEXING) ---
result = pandas_series[0]               # Serinin ilk elemanını (0. indeksli) getirir (20).
result = pandas_series[-1]              # Serinin en son elemanını getirir (50).
result = pandas_series[:2]              # Baştan başlayıp 2. elemana kadar (2 dahil değil) olanları getirir.
result = pandas_series['a']             # İndeksi 'a' olan elemanın değerini getirir (20).
result = pandas_series['d']             # İndeksi 'd' olan elemanın değerini getirir (50).
result = pandas_series[['a', 'c']]      # Birden fazla indekse aynı anda erişmek için liste içinde liste kullanılır ('a' ve 'c').

# --- 4. SERİ ÖZELLİKLERİ (ATTRIBUTES) ---
result = pandas_series.ndim             # Serinin boyutunu verir (Seriler her zaman 1 boyutludur). (Kodunuzdaki 'ndima' düzeltildi)
result = pandas_series.dtype            # Serideki verilerin tipini verir (örn: int64).
result = pandas_series.shape            # Serinin şeklini (eleman sayısını) tuple olarak verir (4,).

# --- 5. MATEMATİKSEL METOTLAR ---
result = pandas_series.sum()            # Serideki tüm elemanların toplamını verir.
result = pandas_series.max()            # Serideki en büyük değeri verir.
result = pandas_series.min()            # Serideki en küçük değeri verir.

# --- 6. VEKTÖREL İŞLEMLER ---
result = pandas_series + pandas_series  # Serinin kendisiyle toplanması (her eleman kendisiyle toplanır).
result = pandas_series + 50             # Serideki her bir elemana 50 ekler.
result = np.sqrt(pandas_series)         # Numpy kullanarak serideki her elemanın karekökünü alır.

# --- 7. KOŞULLU İFADELER VE FİLTRELEME (BOOLEAN INDEXING) ---
result = pandas_series >= 50            # Her elemanın 50'ye büyük eşit olup olmadığını kontrol eder (True/False döndürür).
result = pandas_series % 2 == 0         # Her elemanın çift sayı (2'ye bölümünden kalan 0) olup olmadığını kontrol eder.

print("--- Çift Sayı Olan Elemanlar ---")
print(pandas_series[pandas_series % 2 == 0]) # Seride sadece yukarıdaki koşulu sağlayan (çift olan) elemanları ekrana yazdırır.

print("\n--- Serinin Son Hali ---")
print(pandas_series)

print("\n--- Son 'result' Değişkeni ---")
print(result)                           # Result değişkeni en son çift sayı kontrolüne (True/False dizisine) eşitlenmişti.


# --- 8. İKİ FARKLI SERİYİ BİRLEŞTİRME VE İNDEKS HİZALAMA (INDEX ALIGNMENT) ---
opel2018 = pd.Series([20, 30, 40, 10], ["astra", "corsa", "mokka", "insignia"])
opel2019 = pd.Series([40, 30, 20, 10], ["astra", "corsa", "Grandland", "insignia"])

# Pandas, iki seriyi toplarken indeksleri eşleştirir. 
# Ortak indeksler (astra, corsa, insignia) toplanır. 
# Ortak olmayanlar (mokka ve Grandland) için diğer seride karşılık olmadığı için sonuç 'NaN' (Not a Number - Sayı Değil) döner.
total = opel2018 + opel2019

print("\n--- İki Serinin Toplamı (Astra) ---")
print(total["astra"])                   # Sadece 'astra' indeksinin toplamını yazdırır (20 + 40 = 60).

print("\n--- İki Serinin Tüm Toplam Sonuçları ---")
print(total)






# PANDAS KÜTÜPHANESİ - DATAFRAME OLUŞTURMA YÖNTEMLERİ

import pandas as pd

# --- 1. SERİLERDEN (SERIES) SÖZLÜK YARDIMIYLA DATAFRAME OLUŞTURMA ---
s1 = pd.Series([3, 2, 0, 1])
s2 = pd.Series([0, 3, 7, 2])

# İki farklı seriyi bir sözlükte (dictionary) birleştiriyoruz. 
# Sözlüğün anahtarları ('apples', 'oranges') DataFrame'in sütun isimleri olacak.
data_series = dict(apples=s1, oranges=s2) 
df_from_series = pd.DataFrame(data_series)

print("--- Serilerden Oluşan DataFrame ---")
print(df_from_series)
print("\n")


# --- 2. LİSTELERDEN DATAFRAME OLUŞTURMA ---
# Tek boyutlu bir listeden DataFrame oluşturma (Tek sütunlu bir tablo olur)
df1 = pd.DataFrame([1, 2, 3, 4]) 

# Liste içinde listelerden (İki boyutlu) DataFrame oluşturma
# Sütun veya satır ismi belirtilmediği için Pandas bunları 0, 1, 2.. olarak otomatik atar.
df2 = pd.DataFrame([["ahmet", 50], ["fatih", 60], ["ibo", 70], ["batu", 80]])

# Verileri, sütun isimlerini (columns) ve satır indekslerini (index) özel olarak belirleme
data_list = [["ahmet", 50], ["fatih", 60], ["ibo", 70], ["batu", 80]]
df3 = pd.DataFrame(data_list, columns=['Name', 'Grade'], index=[1, 2, 3, 4])

print("--- Liste ve Özel İndekslerden Oluşan DataFrame ---")
print(df3)
print("\n")


# --- 3. FARKLI VERİ YAPILARIYLA DATAFRAME OLUŞTURMA ---
# Not: Python'da 'list' ve 'dict' gömülü (built-in) fonksiyon isimleri olduğu için, 
# değişken ismi olarak kullanılmaları tavsiye edilmez. Bu yüzden sonlarına '_' ekledik.

# A) Liste içinde listeler (Satır bazlı veri)
my_list = [["ahmet", 50], ["fatih", 60], ["ibo", 70], ["batu", 80]]

# B) Sözlük içinde listeler (Sütun bazlı veri - En sık kullanılan yöntemlerden biri)
# Anahtarlar ('Name', 'Grade') sütun başlığı, karşılarındaki listeler ise o sütunun verileri olur.
my_dict = {"Name": ["ahmet", "fatih", "ibo", "batu"], "Grade": [50, 60, 70, 80]}

# C) Sözlüklerden oluşan liste (JSON formatına çok benzer, API'lerden veri çekerken sık karşılaşılır)
dict_list = [
    {"Name": "ahmet", "Grade": 50},
    {"Name": "fatih", "Grade": 60},
    {"Name": "ibo",   "Grade": 70},
    {"Name": "batu",  "Grade": 80}
]

# Sözlük tabanlı verimizden (my_dict), indeksleri kendimiz belirleyerek ('212', '232' vb.) DataFrame oluşturuyoruz.
df_final = pd.DataFrame(my_dict, index=["212", "232", "236", "456"])

print("--- Sözlükten ve Özel İndekslerden Oluşan Final DataFrame ---")
print(df_final)





# PANDAS İLE FARKLI DOSYA TİPLERİNDEN VERİ OKUMA

import pandas as pd
import sqlite3

# Not: Aşağıdaki her bir satır 'df' (DataFrame) değişkeninin üzerine yazar.
# Gerçek bir projede her birini farklı değişkenlere (örn: df_csv, df_excel) atamak daha mantıklıdır.

# --- 1. CSV (Comma Separated Values) Dosyası Okuma ---
# Veri biliminde en sık kullanılan, virgülle ayrılmış metin dosyalarıdır.
df = pd.read_csv('sample.csv')


# --- 2. JSON (JavaScript Object Notation) Dosyası Okuma ---
# Genellikle web API'lerinden gelen, sözlük (dictionary) yapısına benzeyen dosyalardır.
# Türkçe karakter (ş, ç, ö vb.) sorunu yaşamamak için encoding="UTF-8" kullanmanız çok doğru bir hamle.
df = pd.read_json('sample.json', encoding="UTF-8")


# --- 3. EXCEL Dosyası Okuma ---
# Klasik Microsoft Excel (.xlsx veya .xls) dosyalarındaki sayfaları okur.
# (Not: Çalışması için bilgisayarınızda 'openpyxl' kütüphanesinin yüklü olması gerekebilir).
df = pd.read_excel('sample.xlsx')


# --- 4. SQL VERİTABANINDAN Veri Okuma ---
# Önce veritabanına bağlanıyoruz. SQLite, dosya tabanlı hafif bir veritabanıdır.
connection = sqlite3.connect("sample.db")

# Veritabanına SQL sorgusu göndererek dönen sonucu doğrudan DataFrame'e çeviriyoruz.
# DÜZELTME: Hangi bağlantıyı kullanacağını bilmesi için 'connection' parametresini ekledik.
df = pd.read_sql_query("SELECT * FROM students", connection)

# Bağlantıyı kullandıktan sonra kapatmak iyi bir alışkanlıktır (kaynak tüketimini engeller).
connection.close()


# En son okunan veriyi (bu durumda SQL'den gelen students tablosunu) ekrana yazdırır.
print("--- SQL Veritabanından Gelen Veri ---")
print(df)





import pandas as pd
from numpy.random import randn

# DataFrame oluşturma (Parantez hatası düzeltildi)
df = pd.DataFrame(randn(3,3), index=["A","B","C"], columns = ["column1","column2","column3"])

# 1. Temel Seçimler
res1 = df["column1"]                # Series döndürür
res2 = type(df["column1"])          # <class 'pandas.core.series.Series'>
res3 = df[["column1","column2"]]    # Birden fazla kolon: DataFrame döndürür

# 2. .loc ile Satır/Sütun Seçimi
res4 = df.loc["A"]                  # "A" satırını seçer
res5 = type(df.loc["A"])            # Series döndürür (Hata düzeltildi: dp -> df)

# 3. İleri Seviye Dilimleme (Slicing)
res6 = df.loc[:,"column1"]                  # Tüm satırlar, sadece column1
res7 = df.loc[:,["column1","column2"]]      # Tüm satırlar, belirli kolonlar
res8 = df.loc["A":"B", :"column2"]          # A'dan B'ye satırlar, baştan column2'ye kadar sütunlar
res9 = df.loc["A","column2"]                # Tek bir hücre (Skaler değer)

# 4. Yeni Kolon Ekleme
df["column4"] = pd.Series(randn(3), index=["A","B","C"])

print(df) # DataFrame'in son halini görelim
print("\nSon Seçim İşlemi (result):")
print(res8)




#  DATAFRAME  FİLTRELEME

import pandas as pd
import numpy as np

# 10 ile 100 arasında rastgele tam sayılardan oluşan, 15 satır ve 5 sütunluk (15x5) bir NumPy dizisi oluşturur.
data = np.random.randint(10,100,75).reshape(15,5)

# Bu diziyi, sütun isimleri "column1"den "column5"e kadar olan bir Pandas DataFrame'ine dönüştürür.
df = pd.DataFrame(data,columns= ["column1","column2","column3","column4","column5"])

# --- TEMEL SEÇME VE GÖZLEM FONKSİYONLARI ---

result = df             # DataFrame'in tamamını 'result' değişkenine atar.
result = df.columns     # DataFrame'in sütun isimlerini (Index nesnesi olarak) döndürür.
result = df.head()      # DataFrame'in ilk 5 satırını getirir (varsayılan değer 5'tir).
result = df.head(10)    # DataFrame'in ilk 10 satırını getirir.
result = df.tail()      # DataFrame'in son 5 satırını getirir (varsayılan değer 5'tir).
result = df.tail(10)    # DataFrame'in son 10 satırını getirir.

# --- SÜTUN VE SATIR DİLİMLEME (SLICING) ---

result = df["column1"].head()       # Sadece "column1" sütununu seçer ve ilk 5 satırını getirir (Series döndürür).
result = df.column1.head()          # Üstteki kod ile tamamen aynıdır, sütuna nokta (.) ile erişim sağlar.
result = df[["column1","column2"]].head()  # "column1" ve "column2" sütunlarını birlikte seçer ve ilk 5 satırını getirir.
result = df[["column1","column2"]].tail()  # "column1" ve "column2" sütunlarının son 5 satırını getirir.

# Önce 5. indeksten 14. indekse kadar olan satırları alır (15 dahil değil), sonra bu satırların ilk 5'ini getirir.
result = df[5:15][["column1","column2"]].head()

# Önce 5. indeksten 14. indekse kadar olan satırları alır, sonra bu satırların son 5'ini getirir.
result = df[5:15][["column1","column2"]].tail()


# --- KOŞULLU FİLTRELEME (BOOLEAN INDEXING) ---

result = df > 50        # Tüm hücreleri kontrol eder. 50'den büyükse True, değilse False içeren bir maske (DataFrame) döner.
result = df [df > 50]   # 50'den büyük olan değerleri aynen gösterir, 50 ve daha küçük olan yerlere ise NaN (boş değer) yazar.
result = df[df % 2 ==0] # Çift olan sayıları aynen gösterir, tek olan sayıların yerine NaN yazar.

# "column1" sütunundaki değeri 50'den büyük olan SATIRLARIN tamamını filtreler.
result = df[df["column1"]>50]

# "column1" değeri 50'den büyük olan satırları filtreler ama ekrana sadece bu satırların "column1" ve "column2" sütunlarını getirir.
result = df[df["column1"]>50][["column1","column2"]]

# ÇOKLU KOŞUL (VE - &): "column1" değeri 50'den büyük VE 70'ten küçük veya eşit olan satırları getirir.
result = df[(df["column1"]>50) & (df["column1"] <=70)]

# ÇOKLU KOŞUL (VE - &): "column1" değeri 50'den büyük VE "column2" değeri 70'ten küçük veya eşit olan satırları getirir.
result = df[(df["column1"]>50) & (df["column2"] <=70)]

# ÇOKLU KOŞUL (VEYA - |): "column1" 50'den büyük VEYA "column2" 50'den büyük olan satırların sadece ilk iki sütununu getirir.
result = df[(df["column1"]>50) | (df["column2"] > 50)][["column1","column2"]]

# QUERY METODU: SQL benzeri bir metinle filtreleme yapar. "column1" değeri 50'ye eşit/büyük VE çift sayı olan satırların ilk iki sütununu getirir.
result = df.query("column1 >=50 & column1 %2 ==0") [["column1","column2"]]

# En son hangi 'result' ataması yapıldıysa onun çıktısını ekrana yazdırır (Şu an en alttaki query sonucunu basar).
print(result)




# UYGULAMA IMDB VERİ ANALİZİ
import pandas as pd

df = pd.read_csv("imdb.csv")

# 1- dosya hakkındaki bilgiler
result= df
# 2- ilk 5 kaydı gösterin
result= df.head()
# 3- ilk 10 kaydı gösterin
result = df.head(10)
# 4- son 5 kaydı gösterin
result = df.tail()
# 5- son 10 kaydı gösterin
result = df.tail(10)
# 6- sadece Movie_title kolonunu alın
result = df["Movie_Title"]
# 7- sadece Movie_title kolonunu içeren ilk 5 kaydı alın
result= df["Movie_Title"].head(5)
# 8- sadece Movie_title ve Rating kolonunu içeren ilk 5 kaydı alın
result = df[["Movie_Title","Rating"]].head(5)
# 9- sadece Movie_title ve Rating kolonunu içeren son 7 kaydı alın
result = df[["Movie_Title","Rating"]].tail(7)
# 10- sadece Movie_title ve Rating kolonunu içeren ikinci 5 kaydı kaydı alın
result = df[5:][["Movie_Title","Rating"]].head(5)
# 11- sadece Movie_title ve Rating kolonunu içeren ve imdb puanı 8.0 üstü
#     olan kayıtlardan ilk 50 tanesini alınız.
result = df[df["Rating"] >=8.0] [["Movie_Title","Rating"]].head(50)
# 12- yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz
result = df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <=2015)] [["Movie_Title","YR_Released"]]
# 13- değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı
#     8 ile 9 arasında olan filmleri listeleyiniz
result = df[(df["Num_Reviews"] >100000) | (df["Rating"]>=8) & (df["Rating"]<=9)]
print(result)





import pandas as pd
import numpy as np

# Personel bilgilerini içeren bir sözlük (dictionary) veri yapısı
personeller = {
    'çalışan' : ["ahmet yılmaz","can ertürk","hasan korkmaz","cenk saymaz","ali turan","rıza ertürk","mustafa can"],
    'departman' : ["insan kaynakları","bilgi işlem","muhasebe","insankaynakları","bilgi işlem","muhasebe","bilgi işlem"], # Not: 'insankaynakları' bitişik yazılmış, ayrı bir grup olarak algılanır.
    'yaş':[30,25,45,50,23,34,42],
    'semt': ["kadıköy","tuzla","maltepe","tuzla","maltepe","tuzla","kadıköy"],
    'maaş': [5000,3000,4000,3500,2750,6500,4500]    
}

# Sözlüğü Pandas DataFrame'ine dönüştürüyoruz
df = pd.DataFrame(personeller)

result = df                     # DataFrame'in tamamını result değişkenine atar.
result = df["maaş"].sum()       # Şirketteki tüm çalışanların maaşlarının toplamını verir.


# --- GRUPLARI İNCELEME (GROUPS & LOOPS) ---

# Departmanlara göre gruplar oluşturur ve hangi grupta hangi satır indekslerinin (0, 1, 2..) olduğunu gösteren bir sözlük döner.
result = df.groupby("departman").groups

# Çoklu gruplama: Hem departman hem de semt kombinasyonlarına göre gruplar oluşturur (Örn: bilgi işlem-tuzla grubu).
result = df.groupby(["departman","semt"]).groups

# Semtlere göre gruplar oluşturur ve her semti (name) ve o semtteki kişilerin listesini (group) döngüyle ekrana yazdırır.
for name, group in df.groupby("semt"):
    print(name)
    print(group)

# Departmanlara göre gruplar oluşturur ve her departmanı ve o departmandaki kişilerin listesini döngüyle ekrana yazdırır.
for name, group in df.groupby("departman"):
    print(name)
    print(group)


# --- ÖZEL BİR GRUBU SEÇME (GET_GROUP) ---

result = df.groupby("semt").get_group("kadıköy")       # Sadece "kadıköy" semtinde oturanların verilerini getirir.
result = df.groupby("departman").get_group("muhasebe") # Sadece "muhasebe" departmanında çalışanların verilerini getirir.


# --- GRUP BAZLI AGGREGATION (TOPLAMSAL FONKSİYONLAR) ---

result = df.groupby("departman").sum()   # Her departmanın sayısal sütunlarının (yaş ve maaş) toplamını verir.
result = df.groupby("departman").mean()  # Her departmanın yaş ve maaş ortalamasını verir.

result = df.groupby("departman")["maaş"].mean() # Departman bazında SADECE maaş ortalamalarını getirir.
result = df.groupby("departman")                 # Sadece gruplama nesnesini oluşturur, ekrana anlamlı bir veri basmaz (Lazy evaluation).

result = df.groupby("semt")["yaş"].mean()        # Semtlere göre yaş ortalamasını verir.
result = df.groupby("semt")["maaş"].mean()       # Semtlere göre maaş ortalamasını verir.
result = df.groupby("semt")["çalışan"].count()   # Hangi semtte kaç adet çalışan olduğunu sayar.

result = df.groupby("departman")["yaş"].max()    # Departmanlardaki en büyük yaş değerini bulur.
result = df.groupby("departman")["maaş"].min()   # Departmanlardaki en düşük maaşı bulur.
result = df.groupby("departman")["maaş"].max()   # Departmanlardaki en yüksek maaşı bulur.

# Departmanlardaki en yüksek maaşları bulur ve içinden SADECE "bilgi işlem" departmanının değerini (örn: 4500) çeker.
result = df.groupby("departman")["maaş"].max()["bilgi işlem"]


# --- AGG METODU KULLANIMI ---

# NumPy kütüphanesini kullanarak departman bazlı sayısal sütunların ortalamasını (np.mean) hesaplar.
result = df.groupby("departman").agg(np.mean)

# Departman bazında SADECE maaş sütununun toplamını (np.sum) hesaplar.
result = df.groupby("departman")["maaş"].agg(np.sum)

# En son hangi 'result' atandıysa onun çıktısı ekrana yazdırılır.
print(result)




# pandas ile kayıp ve bozuk veri analizi

import pandas as pd
import numpy as np

# 10 ile 100 arasında rastgele 15 tam sayıdan oluşan 5 satır, 3 sütunluk bir matris oluşturur.
data = np.random.randint(10,100,15).reshape(5,3)

# 'b', 'd', 'g' indeksleri eksik olacak şekilde 5 satırlık bir DataFrame oluşturur.
df = pd.DataFrame(data, index= ['a','c','e','f','h'], columns=['column1','column2','column3'])

# DataFrame'i yeni indekslerle genişletir. Orijinalde olmayan 'b', 'd', 'g' satırları NaN (boş veri) ile dolar.
df = df.reindex(['a','b','c','d','e','f','g','h'])

result = df


# --- VERİ SİLME (DROP) İŞLEMLERİ ---

result = df.drop("column1", axis = 1)               # "column1" sütununu siler (axis=1 sütun demektir).
result = df.drop(["column1","column2"], axis = 1)   # Belirtilen iki sütunu birden siler.
result = df.drop('a', axis = 0)                     # 'a' satırını siler (axis=0 satır demektir, varsayılardır).
result = df.drop(['a','b','h'], axis = 0)           # Belirtilen 'a', 'b' ve 'h' satırlarını siler.


# --- KAYIP VERİ SORGULAMA (ISNULL / NOTNULL) ---

result = df.isnull()                    # Tüm hücreleri kontrol eder; boş (NaN) ise True, doluysa False döner.
result = df.notnull()                   # isnull'ın tam tersidir; dolu olan hücreler için True döner.
result = df.isnull().sum()              # Her sütunda kaçar tane boş (NaN) veri olduğunu hesaplar.
result = df["column1"].isnull().sum()   # Sadece "column1" sütunundaki boş veri sayısını döndürür.

result = df[df['column1'].isnull()]     # "column1" sütunu boş olan SATIRLARIN tamamını filtreler.
result = df[df['column1'].isnull()]["column1"]   # "column1" sütunu boş olan satırları bulur ve sadece "column1" sütununu getirir.
result = df[df['column1'].notnull()]["column1"]  # "column1" sütunu DOLU olan satırları bulur ve sadece "column1" sütununu getirir.


# --- EKSİK VERİLERİ SİLME (DROPNA) ---

result = df.dropna()         # İçinde EN AZ BİR TANE NaN olan tüm satırları siler (axis=0 varsayılan).
result = df.dropna(axis=1)   # İçinde EN AZ BİR TANE NaN olan tüm sütunları siler.
result = df.dropna(how='any') # Satırda en az bir NaN varsa o satırı siler (df.dropna() ile aynıdır).
result = df.dropna(how="all") # Sadece TÜM elemanları NaN olan satırları siler.

# Sadece "column1" ve "column2" sütunlarına bakar; ikisi birden NaN ise o satırı siler.
result = df.dropna(subset= ["column1","column2"], how='all')

# Sadece "column1" ve "column2" sütunlarına bakar; herhangi biri NaN ise o satırı siler.
result = df.dropna(subset= ["column1","column2"], how='any')

# Thresh (Eşik değeri): Bir satırda en az 2 tane normal (NaN olmayan) veri varsa o satırı silmez, tutar.
result = df.dropna(thresh= 2)


# --- EKSİK VERİLERİ DOLDURMA (FILLNA) ---

result = df.fillna(value = 'no input')  # DataFrame içindeki tüm NaN alanları 'no input' metniyle doldurur.
result = df.fillna(value = 1)           # Tüm NaN alanları 1 sayısı ile doldurur.


# --- İSTATİSTİKSEL ÖZETLER VE ÖZEL FONKSİYON İLE DOLDURMA ---

result = df.sum()                       # Her sütunun kendi içindeki toplamını verir (NaN'lar hesaba katılmaz).
result = df.sum().sum()                 # Tüm DataFrame'deki sayıların genel toplamını verir.
result = df.size                        # DataFrame'deki toplam hücre sayısını verir (Boşlar dahil: Satır x Sütun).
result = df.isnull().sum()              # Sütun bazlı boş veri sayılarını verir.
result = df.isnull().sum().sum()        # Tüm DataFrame içindeki toplam boş (NaN) hücre sayısını verir.

# DataFrame'deki mevcut (dolu) sayıların genel ortalamasını hesaplayan fonksiyon
def ortalama(df):
    toplam = df.sum().sum()             # Not: Orijinal kodundaki eksik parantez () eklendi.
    adet = df.size - df.isnull().sum().sum() # Toplam hücre sayısından boş hücre sayısı çıkarılarak dolu hücre sayısı bulunur.
    return toplam / adet

# Tablodaki tüm boş hücreleri (NaN), tablonun genel sayısal ortalaması ile doldurur.
result = df.fillna(value = ortalama(df))


# En son hangi 'result' atandıysa ekrana onun çıktısı basılır.
print(result)






#  pandas ile string fonksiyonları

import pandas as pd

# 1. Veriyi okuyoruz ve eksik değerleri (NaN) temizliyoruz
data = pd.read_csv("nba.csv")
data.dropna(inplace=True)

# 2. İsimleri önce tamamen büyük harfe, sonra tamamen küçük harfe çeviriyoruz
data["Name"] = data["Name"].str.upper()
data["Name"] = data["Name"].str.lower()

# 3. İsimlerin içinde 'a' harfinin geçtiği ilk indeks numarasını buluyoruz (Yoksa -1 döner)
data["index"] = data["Name"].str.find('a')

# 4. HATA DÜZELTME 1: İsimleri tamamen küçük harfe (lower) çevirdiğimiz için 
# 'Jordan' (büyük J ile) ararsak hiçbir şey bulamaz. Bu yüzden 'jordan' olarak aratıyoruz.
data = data[data["Name"].str.contains('jordan')]

# 5. HATA DÜZELTME 2: 'data.Name.Team' adında zincirleme bir kullanım hata verir. 
# Muhtemelen "Team" sütunundaki boşlukları '-' ile değiştirmek istedin. Doğrusu:
data["Team"] = data["Team"].str.replace(' ', '-')

# 6. HATA DÜZELTME 3: Sadece 2 kelimeden oluşan isimleri 'FirstName' ve 'LastName' olarak ayırırken
# veri çerçevesinin (DataFrame) orijinal boyutunu korumak ve hata almamak için işlemleri ayırıyoruz.
# 'expand=True' kullanarak sütunları bölüyoruz.
split_names = data['Name'].str.split(expand=True)
data['FirstName'] = split_names[0]
data['LastName'] = split_names[1]

# Sonucu ekrana yazdırıyoruz
print(data.head(10))







# pandas ile join ve merge

import pandas as pd

# --- VERİ SETLERİNİN OLUŞTURULMASI ---

customer = {
    'CustomerId':[1,2,3,4],
    'FirstName' :["fatih","batuhan","çağatay","yiğit"],
    'LastName'  :["öztürk","hanoğlu","kalem","kahraman"]
}

orders = {
    'OrderId': [10,11,12,13],
    'CustomerId': [1,2,5,7], # Not: 5 ve 7 id'li müşteriler 'customer' tablosunda yok. 3 ve 4 id'li müşterilerin ise siparişi yok.
    'OrderDate': ['2025-07-04','2025-08-04','2025-07-07','2025-07-04']
}

df_customers= pd.DataFrame(customer,columns=["CustomerId","FirstName","LastName"])
df_orders= pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

print(df_customers)
print(df_orders)


# --- PD.MERGE() İŞLEMLERİ (SQL JOIN MANTIĞI) ---

# INNER JOIN: Sadece her iki tabloda da ortak olan 'CustomerId' değerlerini birleştirir.
# Çıktıda sadece 1 ve 2 id'li müşteriler (fatih ve batuhan) yer alır.
result = pd.merge(df_customers,df_orders,how="inner")

# LEFT JOIN: Soldaki (ilk yazılan) tablonun tamamını getirir. Sağdaki tabloda eşleşen sipariş varsa yazar, yoksa NaN koyar.
# fatih ve batuhan'ın sipariş bilgileri gelir; çağatay ve yiğit'in sipariş bilgileri NaN olur.
result = pd.merge(df_customers,df_orders,how="left")

# RIGHT JOIN: Sağdaki (ikinci yazılan) tablonun tamamını getirir. Soldaki tabloda eşleşen müşteri varsa yazar, yoksa NaN koyar.
# 1 ve 2 id'li siparişlerin müşteri isimleri gelir; 5 ve 7 id'li siparişlerin isim kısımları NaN olur.
result = pd.merge(df_customers,df_orders,how="right")

# OUTER JOIN: Her iki tablodaki tüm satırları birleştirir. Eşleşmeyen tüm alanlara NaN yazar (Hiçbir veri kaybolmaz).
result = pd.merge(df_customers,df_orders,how="outer")

print(result) 


# --- YENİ VERİ SETLERİ (MÜŞTERİ GRUPLARI) ---

customersA = {
    'CustomerId':[1,2,3,4],
    'FirstName' :["fatih","batuhan","çağatay","yiğit"],
    'LastName'  :["öztürk","hanoğlu","kalem","kahraman"]
}

customersB = {
    'CustomerId':[4,5,6,7],
    'FirstName' :["akın","mutlu","deniz","eray"],
    'LastName'  :["yakın","bulut","erden","yalın"]
}

df_customersA = pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])


# --- PD.CONCAT() İŞLEMLERİ (UCA EKLEME / CONCATENATION) ---

# Dikey Birleştirme (axis=0 varsayılan): df_customersB tablosunu, df_customersA tablosunun ALTINA ekler. 
# Satırlar arka arkaya dizilir. Toplam 8 satırlık bir DataFrame oluşur. İndeksler orijinal kalır (0,1,2,3,0,1,2,3).
result=pd.concat([df_customersA,df_customersB])

# Yatay Birleştirme (axis=1): Tabloları YAN YANA birleştirir. 
# Aynı satır indeksine sahip veriler yan yana gelir. Toplam 6 sütunlu bir yapı oluşur.
result=pd.concat([df_customersA,df_customersB],axis=1)

print(result)







#  Pandas ile dataframe metotları

import pandas as pd
import numpy as np

data = {
    "Column1":[1,2,3,4,5],
    "Column2":[10,20,13,45,25],
    "Column3":["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

# --- FONKSİYON TANIMLAMALARI ---
# Gelen sayının karesini alan klasik bir fonksiyon
def kareal(x):
    return x*x

# Yukarıdaki fonksiyonun tek satırlık (anonim) lambda hali
kareal2 = lambda x: x * x


# --- VERİ ANALİZİ VE BENZERSİZ DEĞER METOTLARI ---

result = df                             # DataFrame'in tamamını atar.
result = df["Column2"].unique()         # "Column2" içindeki benzersiz (tekrarlanmayan) değerleri bir dizi (array) olarak döner.
result = df["Column2"].nunique()        # Benzersiz değerlerin KAÇ ADET olduğunu (sayısını) döndürür.
result = df["Column2"].value_counts()   # Hangi değerden kaçar tane olduğunu sayar (Frekans tablosu oluşturur).
result = df["Column1"] * 2              # "Column1"deki tüm elemanları matematiksel olarak 2 ile çarpar.


# --- APPLY METODU (FONKSİYON UYGULAMA) ---

result = df["Column1"].apply(kareal)    # "Column1"deki her elemanı tek tek 'kareal' fonksiyonuna gönderir ve sonuçları döner.
result = df["Column1"].apply(kareal2)   # Üstteki işlemin aynısını lambda fonksiyonu kullanarak yapar.
result = df["Column3"].apply(len)       # "Column3"deki her metnin karakter uzunluğunu (harf sayısını) hesaplar.

# "Column3"teki metin uzunluklarını hesaplar ve bunu "Column4" adında YENİ BİR SÜTUN olarak DataFrame'e ekler.
df["Column4"] = df["Column3"].apply(len)


# --- METADATA VE TABLO BİLGİLERİ ---

result = df.columns                     # Tablonun sütun isimlerini getirir.
result = len(df.columns)                # Tabloda kaç adet sütun olduğunu sayar.
result = df.index                       # Tablonun satır indeks bilgilerini (başlangıç, bitiş, adım) getirir.
result = len(df.index)                  # Tabloda kaç adet satır (indeks) olduğunu sayar.

# Tablonun yapısı, sütunların veri tipleri, bellek kullanımı ve boş olmayan (non-null) değer sayıları hakkında özet bilgi verir.
# Not: Genelde metot olarak parantezle çağrılır -> df.info()
result = df.info 


# --- SIRALAMA (SORTING) METOTLARI ---

result = df.sort_values("Column2")      # Tabloyu "Column2"deki sayılara göre KÜÇÜKTEN BÜYÜĞE sıralar.
result = df.sort_values("Column3")      # Tabloyu "Column3"teki metinlere göre ALFABETİK (A'dan Z'ye) sıralar.

# Tabloyu "Column3"e göre Z'den A'ya (Ters alfabetik) sıralar. (ascending=False büyükten küçüğe demektir)
result = df.sort_values("Column3", ascending=False)


# --- YENİ VERİ SETİ OLUŞTURMA ---

data = {
    "ay": ["mayıs","haziran","nisan","mayıs","haziran","nisan","mayıs","haziran","nisan"],
    "kategori": ["elektronik","elektronik","elektronik","kitap","kitap","kitap","sanat","sanat","sanat"],
    "gelir": [20,30,15,14,32,42,12,36,52] 
}

df = pd.DataFrame(data)

# En son oluşturulan 'ay, kategori, gelir' içerikli yeni DataFrame'i ekrana yazdırır.

print(df.pivot_table(index="ay",columns="kategori",values="gelir"))
 
 
 
 
 
#   NBA.CSV ALIŞTIRMA

import pandas as pd

# NBA veri setini CSV dosyasından okuyup bir DataFrame'e yüklüyoruz
df = pd.read_csv("nba.csv")


# 1. İlk 10 kaydı getiriniz
result = df.head(10)


# 2. Toplam kaç kayıt vardır?
result = len(df.index)


# 3. Tüm oyuncuların toplam maaş ortalaması nedir?
result = df["Salary"].mean()


# 4. En yüksek maaş ne kadardır?
result = df["Salary"].max()


# 5. En yüksek maaş alan oyuncu kimdir?
# Maaşı maksimum değere eşit olan satırı bulur, sadece "Name" sütununu seçer ve iloc[0] ile ilk değeri alır.
result = df[df["Salary"] == df["Salary"].max()]["Name"].iloc[0]


# 6. Yaşı 20 ile 25 (25 hariç) arasında olan oyuncuların isim, takım ve yaş bilgilerini yaşa göre azalan (büyükten küçüğe) şekilde getirir.
result = df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name","Team","Age"]].sort_values("Age", ascending=False)


# 7. "John Holland" isimli oyuncunun oynadığı takımı getirir.
result = df[df["Name"] == "John Holland"]["Team"].iloc[0]


# 8. Takımlara göre oyuncuların ortalama maaş bilgisi nedir?
# Performans ve modern Pandas standartları için önce ["Salary"] sütununu seçip sonra mean() almak daha iyidir:
result = df.groupby("Team")["Salary"].mean()


# 9. Kaç farklı takım mevcut?
result = len(df.groupby("Team")) # Gruplama üzerinden toplam grup sayısını alır.
result = df["Team"].nunique()    # Doğrudan sütundaki benzersiz değer sayısını döndürür (Alternatif).


# 10. Her takımda kaç oyuncu oynamaktadır?
# Takımların frekansını (oyuncu sayılarını) büyükten küçüğe sıralı getirir.
result = df["Team"].value_counts()

 
# 11. İsmi içinde "and" geçen kayıtları bulunuz.
# .str.contains() metodu dize içinde arama yapar (Örn: "Orlando", "Anderson" vb. eşleşir).
result = df[df["Name"].str.contains("and", na=False)] # na=False eklemek boş (NaN) isimlerde hata almanı önler.


# En son atanan sonucun çıktısını yazar
print(result)



import pandas as pd

df = pd.read_csv("nba.csv")


# ilk 10 kaydı getiriniz
result = df.head(10)

# toplam kaç kayıt vardır ?
result = len(df.index)

# tüm oyuncuların toplam maaş ortalaması nedir ?
result = df["Salary"].mean()

# en yüksek maaş ne kadardır ?
result = df["Salary"].max()

# en yüksek maaş alan oyuncu kimdir ?
result = df[df["Salary"] ==df["Salary"].max()]["Name"].iloc[0]

# yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
result = df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name","Team","Age"]].sort_values("Age",ascending=False)

# "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
result = df[df["Name"] =="John Holland"]["Team"].iloc[0]

# takımlara göre oyuncuların ortalama maaş bilgisi nedir ?,
result = df.groupby("Team").mean()["Salary"]

# kaç farklı takım mevcut ?
result = len(df.groupby("Team"))
result = df["Team"].nunique()

# her takımda kaç oyuncu oynamaktadır ?
result = df["Team"].value_counts()
 

print(result)




import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# ÖRNEK 1: TEMEL GRAFİK VE EKSEN BİÇİMLENDİRME
# =============================================================================

x1 = [1,2,3,4]
y1 = [1,4,9,16]

# "o--r" parametresi: 'o' (yuvarlak işaretçi), '--' (kesikli çizgi), 'r' (kırmızı renk)
plt.plot(x1, y1, "o--r")

# Eksen sınırlarını belirler: [x_min, x_max, y_min, y_max] -> x(0-6), y(0-20)
plt.axis([0, 6, 0, 20])

plt.title("Grafik Başlığı")
plt.xlabel("X Ekseni Etiketi")
plt.ylabel("Y Ekseni Etiketi")
plt.show()  # Grafiği ekrana basar


# =============================================================================
# ÖRNEK 2: TEK GRAFİKTE ÇOKLU ÇİZGİ VE LEJAND (KUTUCUK)
# =============================================================================

# 0 ile 2 arasında eşit aralıklı 100 sayı üretir
x2 = np.linspace(0, 2, 100)

plt.plot(x2, x2, label="Linear (Doğrusal)", color="red")
plt.plot(x2, x2**2, label="Quadratic (Karesel)", color="yellow")
plt.plot(x2, x2**3, label="Cubic (Küp)", color="green")

plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.title("Matematiksel Fonksiyonlar")
plt.legend()  # Çizgilerin etiketlerini (label) gösteren kutucuğu ekler

plt.show()


# =============================================================================
# MATPLOTLIB İLE FIGURE VE AXES (NESNE YÖNELİMLİ YAKLAŞIM)
# =============================================================================

# -10 ile 9 arasında 20 nokta üretelim
x = np.linspace(-10, 9, 20)
y = x**3  # Küp
z = x**2  # Kare


# --- ÖRNEK 3: İÇ İÇE GRAFİKLER (İÇ GRAFİK / NESTED AXES) ---

figure = plt.figure() # Boş bir tuval (Figure) oluşturur

# add_axes([sol, alt, genişlik, yükseklik]) -> Tuvale göre % oranlar (0 ile 1 arası)
# Büyük Grafik (Dış)
axes_cube = figure.add_axes([0.1, 0.1, 0.8, 0.8])
axes_cube.plot(x, y, "b")  # 'b' = blue (mavi)
axes_cube.set_xlabel("X Ekseni")
axes_cube.set_ylabel("Y Ekseni")
axes_cube.set_title("Küp Grafiği (Dış)")

# Küçük Grafik (Sol üst köşeye yerleştirilmiş iç grafik)
axes_square = figure.add_axes([0.15, 0.6, 0.25, 0.25])
axes_square.plot(x, z, "r")  # 'r' = red (kırmızı)
axes_square.set_xlabel("X Ekseni")
axes_square.set_ylabel("Y Ekseni")
axes_square.set_title("Kare Grafiği (İç)")

plt.show()


# --- ÖRNEK 4: TEK EKSENDE İKİ AYRI ÇİZGİ VE LEJAND KONUMU ---

figure = plt.figure()

# Tuvalin tamamını kaplayan bir eksen alanı oluşturur
axes = figure.add_axes([0, 0, 1, 1])

axes.plot(x, z, label="Kare (x^2)")
axes.plot(x, y, label="Küp (x^3)")

# loc=1 -> Lejand kutusunu sağ üst köşeye yerleştirir (1: sağ üst, 2: sol üst, 3: sol alt, 4: sağ alt)
axes.legend(loc=1)

plt.show()


# --- ÖRNEK 5: SUBPLOTS (ÇOKLU GRAFİK PANELLERİ) ---

# 2 satır, 1 sütun olacak şekilde 2 adet grafik paneli (axes dizisi) oluşturur
fig, axes = plt.subplots(nrows=2, ncols=1)

# Üstteki grafik (0. indeks)
axes[0].plot(x, y)
axes[0].set_title("Küp Grafiği (Üst)")

# Alttaki grafik (1. indeks) - Not: Orijinal kodundaki başlık isim karmaşası düzeltildi
axes[1].plot(x, z)
axes[1].set_title("Kare Grafiği (Alt)")

# Grafiklerin başlıkları ve eksen yazıları birbiri üzerine binmesin diye mesafeleri otomatik ayarlar
plt.tight_layout()

plt.show()




import matplotlib.pyplot as plt

# =============================================================================
# ÖRNEK 1: STACK PLOT (YIĞILI ALAN GRAFİĞİ)
# =============================================================================

yıl = [2011, 2012, 2013, 2014, 2015]

oyuncu1 = [8, 10, 12, 7, 9]
oyuncu2 = [7, 12, 5, 15, 21]
oyuncu3 = [18, 20, 22, 25, 19]

# Boş çizimlerle lejand (etiket) tanımları yapıyoruz
plt.plot([], [], color="y", label="oyuncu1")
plt.plot([], [], color="r", label="oyuncu2")
plt.plot([], [], color="b", label="oyuncu3")

# Verileri üst üste yığarak alan grafiği çizer
plt.stackplot(yıl, oyuncu1, oyuncu2, oyuncu3, colors=["y", "r", "b"])

plt.title("Yıllara göre atılan goller")
plt.xlabel("Yıl")
plt.ylabel("Gol sayısı")
plt.legend()
plt.show()


# =============================================================================
# ÖRNEK 2: PIE CHART (PASTA GRAFİĞİ)
# =============================================================================

goal_types = "penaltı", "akan oyunda", "serbest vuruş"
goals = [12, 35, 7]
colors = ["y", "r", "b"]

# shadow=True (gölge efekti)
# explode=(...) (dilimlerin merkezden dışarı ayrılma payı)
# autopct='%1.1f%%' (yüzdelik dilimleri virgülden sonra 1 basamakla yazdırma)
plt.pie(
    goals,
    labels=goal_types,
    colors=colors,
    shadow=True,
    explode=(0.05, 0.05, 0.05),
    autopct="%1.1f%%"
)
plt.title("Gol Tiplerinin Dağılımı")
plt.show()


# =============================================================================
# ÖRNEK 3: BAR CHART (SÜTUN GRAFİĞİ - KARŞILAŞTIRMALI)
# =============================================================================

# X eksenindeki konumları hafif kaydırarak iki sütunun yan yana durmasını sağlıyoruz
plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50, 40, 70, 80, 20], label="BMW", width=0.5)
plt.bar([0.75, 1.75, 2.75, 3.75, 4.75], [80, 20, 20, 50, 60], label="AUDİ", width=0.5)

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Alınan mesafe (km)")
plt.title("Araç Bilgileri")
plt.show()


# =============================================================================
# ÖRNEK 4: HISTOGRAM GRAFİĞİ (FREKANS DAĞILIMI)
# =============================================================================

# Veri seti (Yaşlar)
yaslar = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 2, 102, 95, 85, 55, 110, 120, 70, 65, 55, 111, 115]

# Yaş aralıkları (0-10, 10-20, 20-30... şeklinde kutular/bins oluşturur)
yas_grupları = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# rwidth=0.8 sütunlar arasında ufak bir boşluk bırakarak görünürlüğü artırır
plt.hist(yaslar, yas_grupları, histtype="bar", rwidth=0.8)

plt.xlabel("Yaş grupları")
plt.ylabel("Kişi sayısı")
plt.title("Histogram Grafiği")

plt.show()
