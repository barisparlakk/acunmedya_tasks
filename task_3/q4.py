import os

DOSYA_ADI = "rehber.txt"


def kisi_ekle():
    #Ad ve telefon numarasını alıp rehber.txt dosyasına ekler.
    ad = input("Adınızı girin: ").strip()
    telefon = input("Telefon numaranızı girin: ").strip()

    with open(DOSYA_ADI, "a", encoding="utf-8") as dosya:
        dosya.write(f"{ad}: {telefon}\n")

    print(f"{ad} başarıyla rehbere eklendi!")


def kisi_ara():
    #Girilen adı dosyada arar ve telefon numarasını gösterir.
    if not os.path.exists(DOSYA_ADI):
        print("Rehberde kayıtlı hiçbir kişi bulunmuyor.")
        return

    ad = input("Aramak istediğiniz kişinin adını girin: ").strip()
    with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            if satir.lower().startswith(ad.lower() + ":"):
                print(f"Bulundu: {satir.strip()}")
                return

    print(f"{ad} adlı kişi rehberde bulunamadı.")


def rehberi_listele():
    #Rehberdeki tüm kişileri ekrana yazdırır.
    if not os.path.exists(DOSYA_ADI):
        print("Rehberde henüz kayıtlı kişi yok.")
        return

    with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
        rehber = dosya.readlines()

        if rehber:
            print("\n--- Rehber ---")
            for kisi in rehber:
                print(kisi.strip())
        else:
            print("Rehberde kişi bulunmamaktadır.")


def menu():
    """Ana menü ve kullanıcı komutlarını yönetir."""
    while True:
        komut = input(
            "\nKomut girin ('ekle' = kişi ekle, 'ara' = kişi ara, 'listele' = rehberi göster, 'çık' = çıkış): ").strip().lower()

        if komut == "ekle":
            kisi_ekle()
        elif komut == "ara":
            kisi_ara()
        elif komut == "listele":
            rehberi_listele()
        elif komut == "çık":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz komut! Lütfen 'ekle', 'ara', 'listele' veya 'çık' komutlarını kullanın.")


# Programı başlat
menu()
