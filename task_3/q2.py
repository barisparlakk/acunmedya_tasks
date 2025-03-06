import os
def gunluk_yaz():
    with open("gunluk.txt", "a", encoding="utf-8") as dosya:
        while True:
            not_girisi = input(
                "Günlük notunuzu girin ('goruntule' = notları göster, 'sil' = dosyayı sil, 'bitti' = çıkış): ")

            if not_girisi.lower() == "bitti":
                break
            elif not_girisi.lower() == "goruntule":
                gunluk_goruntule()
            elif not_girisi.lower() == "sil":
                gunluk_sil()
            else:
                dosya.write(not_girisi + "\n")
def gunluk_goruntule():
    try:
        with open("gunluk.txt", "r", encoding="utf-8") as dosya:
            notlar = dosya.readlines()
            if notlar:
                print("\n--- Günlük Notları ---")
                for not_ in notlar:
                    print(not_.strip())
            else:
                print("Günlük boş.")
    except FileNotFoundError:
        print("Henüz bir günlük kaydı bulunmuyor.")
def gunluk_sil():
    try:
        os.remove("gunluk.txt")
        print("Günlük başarıyla silindi.")
    except FileNotFoundError:
        print("Silinecek günlük bulunamadı.")

gunluk_yaz()