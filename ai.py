isim = input("İsmini yaz:!")

print(f"Merhaba, {isim}!")

import json
import os

# Bilgileri kaydedeceğimiz dosya
BILGI_DOSYASI = "bilgiler.json"

# Önceden öğrendiği bilgileri yükle
if os.path.exists(BILGI_DOSYASI):
    with open(BILGI_DOSYASI, "r", encoding="utf-8") as f:
        bilgiler = json.load(f)
else:
    bilgiler = {}

def cevap_ver(soru):
    # Eğer soru daha önce öğrenilmişse cevapla
    if soru in bilgiler:
        return bilgiler[soru]
    else:
        return None

def ogret(soru, cevap):
    bilgiler[soru] = cevap
    with open(BILGI_DOSYASI, "w", encoding="utf-8") as f:
        json.dump(bilgiler, f, ensure_ascii=False, indent=2)

# Ana döngü
print("Merhaba! Bana bir şeyler sorabilir veya yeni şeyler öğretebilirsin.")
print("Yeni bir şey öğretmek için: öğret: [soru] = [cevap] şeklinde yaz.")
print("Çıkmak için 'çık' yaz.\n")

while True:
    giris = input("Sen: ")

    if giris.lower() == "çık":
        print("Görüşürüz!")
        break

    elif giris.startswith("öğret:"):
        try:
            parca = giris[7:].split("=")
            soru = parca[0].strip()
            cevap = parca[1].strip()
            ogret(soru, cevap)
            print("🧠 Öğrendim!")
        except:
            print("Hatalı format. Şöyle yaz: öğret: Kedim ne renk? = Sarı")
    else:
        cevap = cevap_ver(giris)
        if cevap:
            print("AI:", cevap)
        else:
            print("🤔 Bunu bilmiyorum. Bana öğretebilirsin.")
