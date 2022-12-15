
def modInverse(e, phi_n):

    for X in range(1, phi_n):
        if (((e % phi_n) * (X % phi_n)) % phi_n == 1):
            return X
    return -1


n = int(
    input("Masukkan nilai N yang didapatkan pada program sebelumnya : "))
phi_n = int(
    input("Masukkan nilai PHI_N yang didapatkan pada program sebelumnya : "))

# Public Key

e = int(input(f"Pilih bilangan prima dalam range {phi_n} : "))
pesan = int(input("Masukkan angka yang ingin di ENKRIPSI : "))

encry = pow(pesan, e) % n
print(f"Pesan anda telah terenkripsi sebagai : {encry}")

public_key = (e, n)
print(f"public key anda : {public_key}")

# Private Key

d = modInverse(e, phi_n)
private_key = (d, n)
print(f"private key anda : {private_key}")
