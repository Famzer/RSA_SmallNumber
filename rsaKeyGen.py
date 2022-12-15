import rsa


# RSA Key Generation

p = int(input("Masukkan bilangan prima : "))
q = int(input("Masukkan bilangan prima : "))


n = p * q
phi_n = (p-1)*(q-1)

print(f"Nilai N anda adalah : {n}")
print(f"Nilai PHI_N anda adalah : {phi_n}")
