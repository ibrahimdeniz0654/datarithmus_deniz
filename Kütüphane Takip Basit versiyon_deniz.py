#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[ ]:


import os

# ---------------------------
# 1. Başlangıç Kitap Veritabanı
# ---------------------------
varsayilan_kitaplar = {
    "Python 101": "uygun",
    "Clean Code": "oduncte",
    "Algorithms": "uygun"
}

dosya_adi = "kutuphane.txt"


# ---------------------------
# 2. Dosya İşlemleri
# ---------------------------
def kutuphane_yukle():
    """kutuphane.txt varsa kitap bilgilerini yükler, yoksa varsayılanlarla başlar."""
    if not os.path.exists(dosya_adi):
        return varsayilan_kitaplar.copy()

    kitaplar = {}
    with open(dosya_adi, "r", encoding="utf-8") as f:
        for satir in f:
            try:
                kitap, durum = satir.strip().split(" - ")
                kitaplar[kitap] = durum
            except ValueError:
                continue  # hatalı satır varsa atla
    return kitaplar


def kutuphane_kaydet(kitaplar):
    """Kitap durumlarını dosyaya yazar."""
    with open(dosya_adi, "w", encoding="utf-8") as f:
        for kitap, durum in kitaplar.items():
            f.write(f"{kitap} - {durum}\n")


# ---------------------------
# 3. Fonksiyonlar
# ---------------------------
def kitap_liste(kitaplar):
    for kitap, durum in kitaplar.items():
        print(f"{kitap} - {durum}")


def kitap_al(kitaplar, kitap_ismi):
    if kitap_ismi not in kitaplar:
        print("Bu kitap mevcut değil.")
    elif kitaplar[kitap_ismi] == "oduncte":
        print("Kitap zaten ödünçte.")
    else:
        kitaplar[kitap_ismi] = "oduncte"
        print("Kitap ödünç verildi.")


def kitap_teslim(kitaplar, kitap_ismi):
    if kitap_ismi not in kitaplar:
        print("Bu kitap mevcut değil.")
    elif kitaplar[kitap_ismi] == "uygun":
        print("Bu kitap zaten kütüphanede.")
    else:
        kitaplar[kitap_ismi] = "uygun"
        print("Kitap teslim alındı.")


# ---------------------------
# 4. Ana Program Döngüsü
# ---------------------------
def main():
    kitaplar = kutuphane_yukle()
    print("📚 Kütüphane Uygulaması Başladı. Komutlar için 'yardim' yazabilirsiniz.")

    while True:
        komut = input("\n> ").strip()

        if komut == "cikis":
            kutuphane_kaydet(kitaplar)
            print("Değişiklikler kaydedildi. Program kapandı.")
            break

        elif komut == "yardim":
            print("""
Komutlar:
  kitap liste                → Tüm kitapları listele
  kitap al <kitap ismi>      → Belirtilen kitabı ödünç al
  kitap teslim <kitap ismi>  → Belirtilen kitabı teslim et
  cikis                      → Programı kapat
            """)

        elif komut == "kitap liste":
            kitap_liste(kitaplar)

        elif komut.startswith("kitap al "):
            kitap_ismi = komut[len("kitap al "):].strip()
            kitap_al(kitaplar, kitap_ismi)

        elif komut.startswith("kitap teslim "):
            kitap_ismi = komut[len("kitap teslim "):].strip()
            kitap_teslim(kitaplar, kitap_ismi)

        else:
            print("Bilinmeyen komut. 'yardim' yazarak komut listesini görebilirsiniz.")


# ---------------------------
# 5. Programı Başlat
# ---------------------------
if __name__ == "__main__":
    main()


# In[ ]:




