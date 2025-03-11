nama = input("Masukan Nama: ")
nik = int(input("Masukan NIK: "))
status = input("Masukan Status Pegawai Tetap/Honorer: ").strip().lower()
gol = input("Masukan Golongan A/B/C: ").strip().upper()

gaji_pokok = 0
bonus = 0

if status == "pegawai tetap":
    gaji_pokok = 1000000
    if gol == "A":
        bonus = 200000
    elif gol == "B":
        bonus = 400000
    elif gol == "C":
        bonus = 550000
    else:
        print("golongan tidak valid!")
        exit()

elif status == "honorer":
    gaji_pokok = 750000
    if gol == "A":
        bonus = 150000
    elif gol == "B":
        bonus = 275000
    elif gol == "C":
        bonus = 480000
    else:
        print("golongan tidak valid!")
        exit()
else:
    print("status tidak valid!")

gaji_total = gaji_pokok + bonus

print("\n Slip Gaji")
print("Nama: ",nama)
print("NIK: ",nik)
print("Status: ",status.capitalize())
print("Golongan: ",gol)
print("Gaji Pokok: Rp.",gaji_pokok)
print("Bonus: Rp.",bonus)
print("Gaji Totall: Rp.",gaji_total)
