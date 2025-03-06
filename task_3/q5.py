import time
import datetime
import threading

DOSYA_ADI = "log.txt"


def log_yaz():
    """Her 10 saniyede bir log.txt dosyasına zaman damgalı kayıt ekler."""
    while True:
        zaman_damgasi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_mesaji = f"{zaman_damgasi} - Sistem çalışıyor\n"

        with open(DOSYA_ADI, "a", encoding="utf-8") as dosya:
            dosya.write(log_mesaji)

        print(f"Log eklendi: {log_mesaji.strip()}")
        time.sleep(10)


def loglari_goruntule():
    """log.txt dosyasındaki tüm kayıtları ekrana yazdırır."""
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            loglar = dosya.readlines()
            if loglar:
                print("\n--- Log Kayıtları ---")
                for log in loglar:
                    print(log.strip())
            else:
                print("Henüz log kaydı bulunmamaktadır.")
    except FileNotFoundError:
        print("Log dosyası bulunamadı. Henüz kayıt yapılmamış olabilir.")


def menu():
    """Log işlemini başlatır ve kullanıcı komutlarını yönetir."""
    # Log işlemini ayrı bir thread içinde başlat
    log_thread = threading.Thread(target=log_yaz, daemon=True)
    log_thread.start()

    while True:
        komut = input("\nKomut girin ('loglari_goruntule' = logları göster, 'çık' = çıkış): ").strip().lower()

        if komut == "loglari_goruntule":
            loglari_goruntule()
        elif komut == "çık":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz komut! Lütfen 'loglari_goruntule' veya 'çık' komutlarını kullanın.")


# Programı başlat
menu()
