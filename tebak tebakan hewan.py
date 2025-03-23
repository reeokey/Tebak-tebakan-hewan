import random

#daftar dan informasi hewan
daftar_hewan = [
    {"nama": "Burung Hantu", "kelompok": "Burung",
    "habitat": "Hutan Berkeliaran Di Malam Hari", "ukuran": "Sedang"},
    {"nama": "Singa", "kelompok": "Mamalia", 
    "habitat": "Sabana", "ukuran": "Besar Dan Punya Rambut"},
    {"nama": "Ikan Hiu", "kelompok": "Ikan",
    "habitat": "Laut", "ukuran": "Besar Dan Mempunyai Gigi Tajam"},
    {"nama": "Gajah", "kelompok": "Mamalia",
    "habitat": "Hutan", "ukuran": "Sangat Besar Serta Punya Belalai"},
] 

def tebak_hewan():
    #untuk mengacak petunjuk
    hewan_acak = random.choice(daftar_hewan)
    skor = 0
    
    print("|=================================|")
    print("|      Selamat Datang Di Game     |")
    print("|       Tebak-Tebakan Hewan       |")
    print("|=================================|")
    print("|      !Tebak Hewan Apa Ini!      |")
    print("|=================================|")
    print("Petunjuk")
    print(f"Kelompok : {hewan_acak['kelompok']}")
    print(f"Habitat  : {hewan_acak['habitat']}")
    print(f"Ukuran   : {hewan_acak['ukuran']}")
    jawaban = input("Tebakan Anda: ")
    
    while jawaban.lower() != hewan_acak['nama'].lower():
        print("Tebakan Anda Salah! Coba Lagi.")
        jawaban = input("Tebakan Kamu: ")
    else:
        skor = skor + 1
        print("Benar! Skor Kamu Sekarang:",skor)
        return skor

# lanjut permainan
skor_total = 0
while True:
    skor_total = skor_total + tebak_hewan()
    print("Ingin Bermain Lagi? (ya / tidak)")
    lanjut = input()
    if lanjut.lower() != "ya":
        break

    print("Terimakasih Telah Bermain! Skor Akhir Anda: ",skor_total)