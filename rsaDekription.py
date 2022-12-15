

d = int(input("Masukkan angka PERTAMA yang ada pada PRIVATE KEY anda : "))
n = int(input("Masukkan angka KEDUA yang ada pada PRIVATE KEY anda: "))

pesan = int(input("Masukkan PESAN YANG TELAH TERENKRIPSI : "))

decr = pow(pesan, d) % n

print(f"Pesan anda adalah : {decr}")
