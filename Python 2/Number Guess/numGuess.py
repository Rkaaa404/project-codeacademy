import random

print("Selamat datang di permaianan tebak angka")
print("Disini kamu akan menebak total angka dari lemparan dua buah dadu")
guess = int(input("Masukkan angka tebakanmu: "))

dadu1 = random.randint(1,6)
dadu2 = random.randint(1,6)

if guess == dadu1 + dadu2 :
    print("Selamat tebakanmu benar!!")
    print(f"Nilai dadu pertama: {dadu1}, nilai dadu kedua: {dadu2}\nMaka nilai totalnya adalah {dadu1+dadu2}")
else :
    print("Yahhh... kamu salah tebak")
    print(f"Nilai dadu pertama: {dadu1}, nilai dadu kedua: {dadu2}\nMaka nilai totalnya adalah {dadu1+dadu2}")