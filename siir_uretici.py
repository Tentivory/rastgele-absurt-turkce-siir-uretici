#!/usr/bin/env python3
# Evrenin en absürt Türkçe şiir üreticisi
# Çalıştır: python siir_uretici.py
import random
import time

def siir_uret():
    kelimeler = [
        "gökyüzü", "çay", "kedi", "uzaylı", "filozof", "tencere", "bulut", "bilgisayar",
        "rüya", "kahve", "yıldız", "ördek", "felsefe", "sandalye", "gizem", "şarkı"
    ]
    fiiller = ["uçuyor", "düşünüyor", "demleniyor", "kayboluyor", "gülüyor", "bekliyor", "dans ediyor"]
    
    print("\n=== ABSÜRT ŞİİR ÜRETİCİSİ BAŞLADI ===\n")
    for i in range(4):
        satir = f"{random.choice(kelimeler)} {random.choice(fiiller)}, "
        satir += f"{random.choice(kelimeler)} ise {random.choice(fiiller)}."
        print(satir)
        time.sleep(0.8)  # Şiirsel tempo için yavaşlama
    print("\n=== ŞİİR BİTTİ, ANLAM ARAMA ===")
    print("Not: Anlam yok. Sadece güzel.")

if __name__ == "__main__":
    siir_uret()
