import json
import os

DOSYA_ADI = "kullanicilar.json"


def kullanici_ekle():
    kullanicilar = dosya_yukle()  # Önce mevcut verileri yükle
    while True:
        ad = input("Adınızı girin ('listele' = kullanıcıları göster, 'bitti' = çıkış): ").strip()

        if ad.lower() == "bitti":
            break
        elif ad.lower() == "listele":
            kullanicilari_listele()
            continue

        soyad = input("Soyadınızı girin: ").strip()
        yas = input("Yaşınızı girin: ").strip()

        if not yas.isdigit():
            print("Lütfen geçerli bir yaş girin.")
            continue

        kullanicilar.append({"ad": ad, "soyad": soyad, "yas": int(yas)})

        dosya_kaydet(kullanicilar)
        print("Kullanıcı başarıyla eklendi!\n")


def kullanicilari_listele():
    kullanicilar = dosya_yukle()

    if kullanicilar:
        print("\n--- Kayıtlı Kullanıcılar ---")
        for i, kullanici in enumerate(kullanicilar, 1):
            print(f"{i}. {kullanici['ad']} {kullanici['soyad']}, Yaş: {kullanici['yas']}")
    else:
        print("Henüz kayıtlı kullanıcı bulunmamaktadır.")


def dosya_yukle():
    """Dosyayı açar ve JSON verisini yükler, yoksa boş liste döndürür."""
    if os.path.exists(DOSYA_ADI):
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            try:
                return json.load(dosya)
            except json.JSONDecodeError:
                return []
    return []


def dosya_kaydet(kullanicilar):
    """JSON verisini dosyaya yazar."""
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(kullanicilar, dosya, indent=4, ensure_ascii=False)


kullanici_ekle()