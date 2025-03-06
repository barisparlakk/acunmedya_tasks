def ogrenci_ekle():
    with open("ogrenciler.txt", "a", encoding="utf-8") as dosya:
        while True:
            isim = input("Öğrenci ismi girin (Çıkmak için 'bitti' yazın): ") #bitti input'u girilene dek kullanicidan girdi almaya devam eder
            if isim.lower() == "bitti":
                break
            dosya.write(isim + "\n")

def ogrencileri_goster():
    try:
        with open("ogrenciler.txt", "r", encoding="utf-8") as dosya:
            ogrenciler = dosya.readlines()
            if ogrenciler:
                print("\n--- Öğrenci Listesi ---")
                for ogrenci in ogrenciler:
                    print(ogrenci.strip())
            else:
                print("Dosyada öğrenci kaydı bulunmamaktadır.")
    except FileNotFoundError:
        print("Dosya bulunamadı. Önce öğrenci ekleyin.")

ogrenci_ekle()