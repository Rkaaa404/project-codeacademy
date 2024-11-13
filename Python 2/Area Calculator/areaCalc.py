# list bangun datar yang tersedia
print('Selamat datang di kalkulator luas')
def hitungLingkaran():
    radius = input('Masukkan jari jari lingkaran (dalam cm): ')
    while radius.isdigit() == False:
        print('Tolong masukkan angka yang valid')
        radius = input('Masukkan jari jari lingkaran (dalam cm): ')
    radius = float(radius)
    if radius % 7 == 0:
        luasLingkaran = 22/7*radius**2
    else :
        luasLingkaran = 3.14*radius**2
    print(f'Luas lingkaran: {luasLingkaran}cm')

def hitungPersegi():
    sisi = input('Masukkan panjang sisi persegi (dalam cm): ')
    while sisi.isdigit() == False:
        print('Tolong masukkan angka yang valid')
        sisi = input('Masukkan panjang sisi persegi (dalam cm): ')
    sisi = float(sisi)
    luasPersegi = sisi**2
    print(f'Luas persegi: {luasPersegi}cm')

def hitungSegitiga():
    alas = input('Masukkan panjang alas segitiga (dalam cm): ')
    while alas.isdigit() == False:
        print('Tolong masukkan angka yang valid')
        alas = input('Masukkan panjang alas segitiga (dalam cm): ')
    tinggi = input('Masukkan panjang tinggi segitiga (dalam cm): ')
    while tinggi.isdigit() == False:
        print('Tolong masukkan angka yang valid')
        tinggi = input('Masukkan panjang tinggi segitiga (dalam cm): ')
    alas = float(alas)
    tinggi = float(tinggi)
    luasSegitiga = 1/2*alas*tinggi
    print(f'Luas segitiga: {luasSegitiga}cm')
    
def hitungPersegiPanjang():
    panjang = input('Masukkan panjang persegi panjang (dalam cm): ')
    while panjang.isdigit() == False:
        print('Tolong masukkan angka yang valid')
        panjang = input('Masukkan panjang persegi panjang (dalam cm): ')
    lebar = input('Masukkan lebar persegi panjang (dalam cm): ')
    while lebar.isdigit() == False:
        print('Tolong masukkan angka yang valid')
        lebar = input('Masukkan lebar persegi panjang (dalam cm): ')
    panjang = float(panjang)
    lebar = float(lebar)
    luasPersegiPanjang = panjang*lebar
    print(f'Luas persegi panjang: {luasPersegiPanjang}cm')

while True : #melakukan do-while loop memastikan bangun datar tersedia dalam daftar bangun datar
    # Input oleh user
    bangunDatar = input('Masukkan bangun datar yang ingin dihitung (contoh: lingkaran): ').lower()
    if bangunDatar == 'lingkaran':
        hitungLingkaran()
    elif bangunDatar == 'persegi':
        hitungPersegi()
    elif bangunDatar == 'persegi panjang':
        hitungPersegiPanjang()
    elif bangunDatar == 'segitiga' :
        hitungSegitiga()

    else :
        print('Bangun datar yang anda masukkan tidak tersedia.')
        print('Apakah anda ingin mengganti input? (Y/N)')
        pilihan = input('').upper()
        if pilihan == 'N':
            print('Terima kasih telah menggunakan program kalkulator luas ini ^_^')
            break
        else:
            continue
    print('Apakah anda mau keluar dari program (Y/N)?')
    pilihan = input('').upper()
    if pilihan == 'Y':
        print('Terima kasih telah menggunakan program kalkulator luas ini ^_^')
        break
    else : 
        continue
