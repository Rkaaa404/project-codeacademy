#import library
import math

print("Selamat datang di kalkulator tip, silahkan isi data data ini:")
# Meminta input user
meal = int(input("Harga Makanan: Rp."))
tip = int(input("Tip yang diberikan (dalam %): "))
# Proses perhitungan
mealTax = math.ceil(meal * 0.11)
mealTaxed = meal + (mealTax)
mealTip = math.ceil(mealTaxed * tip / 100)
mealTotal = mealTaxed + mealTip
mealTotalRounded = math.ceil(mealTotal / 100) * 100
mealRounding= mealTotalRounded - mealTotal
# Print hasil 
print("*******************************")
print(f"Harga Makanan : Rp.{meal} \nPajak(PPN 11%) : Rp. {mealTax} \nTip({tip}%) : Rp.{mealTip}")
#Kondisi bila perlu pembulatan
print(f"Total Sebelum Pembulatan: Rp.{mealTotal}")
if mealRounding != 0:
    print(f"Pembulatan : Rp.{mealRounding} \nTotal Setelah Pembulatan: Rp.{mealTotalRounded}")
print("*******************************")