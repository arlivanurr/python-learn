# mendefinisikan penambahan
def penambahan(x, y):
    return x + y

# mendefinisikan pengurangan
def pengurangan(x, y):
    return x - y

# mendefinisikan perkalian
def perkalian(x, y):
    return x * y

# mendefinisikan pembagian
def pembagian(x, y):
    return x / y

print("Pilih operasi :")
print("1. penambahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")

pilihan = input("Memilih opsi operasi (masukkan 1/2/3/4) : ")
angka1 = int(input("Masukkan angka pertama : "))
angka2 = int(input("Masukkan angka kedua : "))

if pilihan == '1':
    print(angka1, "+", angka2, "=", penambahan(angka1, angka2))
elif pilihan == '2':
    print(angka1, "-", angka2, "=", pengurangan(angka1, angka2))
elif pilihan == '3':
    print(angka1, "*", angka2, "=", perkalian(angka1, angka2))
elif pilihan == '4':
    print(angka1, "/", angka2, "=", pembagian(angka1, angka2))
else:
    print("Opsi yang dipilih tidak valid !")