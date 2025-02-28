ogrenciler = []

def ogrenci_ekle():
    ad = input(" Öğrenci adını girin: ")
    soyad = input("Öğrenci soyadını girin: ")
    idno = int(input(" Yalnizca rakamlardan olusan ogrenci numarasini girin: "))
    yas = int(input("Öğrenci yaşını girin: "))
    dersler = input("Öğrencinin aldığı dersleri aralarına virgül koyarak yazınız: ").split(",")

    ogrenci = {
        "Ad": ad,
        "Soyad": soyad,
        "Ogrenci_No": idno,
        "Yas": yas,
        "Dersler": [ders.strip() for ders in dersler]
    }

    ogrenciler.append(ogrenci)
    print(f" {ad} {soyad} isimli ogrenci basariyla eklendi! ")

def ogrenci_sil():
    istek = int(input(" -- Silmek istediginiz ogrencinin numarasini giriniz: -- "))
    for ogrenci in ogrenciler:
        if ogrenci["Ogrenci_No"] == istek:
            ogrenciler.remove(ogrenci)
            print(f" {ogrenci["Ad"]} {ogrenci["Soyad"]} isimli ogrenci sistemden basariyla silindi. ")
            return
        print("Ogrenci bulunamadi. ")
def ogrenci_guncelle():
    istek = int(input(" -- Hangi ogrencinin bilgilerini guncellemek istiyorsunuz, numarasini giriniz: -- "))
    for ogrenci in ogrenciler:
        if ogrenci["Ogrenci_No"] == istek:
            print(" Degistirmek istediginiz bilgi nedir? ")
            print(" ---        1- Ad             ---")
            print(" ---        2- Soyad          ---")
            print(" ---        3- Ogrenci No     ---")
            print(" ---        4- Yas            ---")
            print(" ---        5- Aldigi dersler ---")
            istek_degisim = int(input("\n - Degistirmek istediginiz bilgi nedir?  - "))
            if istek_degisim == 1:
                ogrenci["Ad"] = input(" Yeni ogrenci adini girin: ")
            elif istek_degisim == 2:
                ogrenci["Soyad"] = input(" Yeni ogrenci soyadini girin: ")
            elif istek_degisim == 3:
                ogrenci["Ogrenci_No"] = int(input(" Yeni ogrenci numarasini girin: "))
            elif istek_degisim == 4:
                ogrenci["Yas"] = input(" Yeni ogrenci yasini girin")
            elif istek_degisim == 5:
                ogrenci["Dersler"] = input(" Ogrencinin aldigi yeni dersleri arasina virgul koyarak yaziniz: ").split(",")
def ogrenci_listele():
    istek = int(input(" Belirli bir ogrenciyi mi listelemek istiyorsunuz? \n Bir ogrenci icin 1, tum ogrencileri listelemek icin 2 giriniz: "))
    if istek == 1:
        tek_goster = int(input(" Bilgilerini gormek istediginiz ogrencinin numarasini giriniz: "))
        for ogrenci in ogrenciler:
            if ogrenci["Ogrenci_No"] == tek_goster:
                print(f" {ogrenci["Ogrenci_No"]} numarali ogrencinin bilgileri: ")
                print(f" Ogrenci Adi-Soyadi : {ogrenci["Ad"]} {ogrenci["Soyad"] }")
                print(f" Ogrenci Yasi : {ogrenci["Yas"]} ")
                print(f" Ogrencinin aldigi dersler: {ogrenci["Dersler"]} ")
    elif istek == 2:
        for ogrenci in ogrenciler:
            print(f" {ogrenci['Ogrenci_No']} numarali ogrencinin bilgileri: ")
            print(f" Ogrenci Adi-Soyadi : {ogrenci['Ad']} {ogrenci['Soyad']}")
            print(f" Ogrenci Yasi : {ogrenci['Yas']}")
            print(f" Ogrencinin aldigi dersler: {ogrenci['Dersler']}")
            print(" ----------------------------- ")


    def menu():
        while True:
            print(" --------  Ogrenci Yonetim Sistemi  --------")
            print(" --------      1- Ogrenci Ekle      --------")
            print(" --------      2- Ogrenci Sil       --------")
            print(" --------      3- Ogrenci Guncelle  --------")
            print(" --------      4- Ogrenci Listele   --------")
            print(" --------      5-     Cikis         --------")


