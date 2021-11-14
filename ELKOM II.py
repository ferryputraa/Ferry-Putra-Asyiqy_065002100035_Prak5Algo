print("-------HITUNG GAJI Harian-------")

jam1=float(input("Jam Masuk Kerja  : "))
gaji1= 175000
if jam1 >=6.00: 
    print("Selamat Pagi")
elif jam1 >=12.00:
    print("Selamat Siang") 

jam2=float(input("Jam Keluar Kerja : "))
if jam2 >=14.00: 
    print("Selamat Siang") 
elif jam2 >=16.00: 
    print("Selamat Sore")
elif jam2-jam1 == 8.00:
    gaji1=gaji1
elif jam2-jam1 >=8.59:
    x = int((jam2 -jam1)-8)
    gaji2=((x)*15000)
    y=int((jam2 - jam1) - 8.00)
x = int((jam2 -jam1)-8)
gaji2=((x)*15000)

print("----------RINCIAN GAJI----------")
print(f"Waktu Kerja   : {int(jam2-jam1)} Jam")
print(f"Gaji Per Hari : Rp.{gaji1}")
print(f"Lembur        : Rp.{gaji2}")
print(f"Total Gaji    : Rp.{(gaji1)+gaji2}")
print("----------TERIMA KASIH----------")
