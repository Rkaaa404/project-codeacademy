print("Selamat datang di kalkulator tip, silahkan isi data data ini:")
# Meminta input user
meal = int(input("Harga Makanan: Rp."))
tip = int(input("Tip yang diberikan (dalam %): "))
# Proses perhitungan
mealTax = meal * 0.11
mealTaxed = meal + (mealTax)
mealTip = mealTaxed * tip / 100
mealTotal = mealTaxed + mealTip
# Print hasil 
print("*******************************")
print(f"Harga Makanan : Rp.{meal} \nPajak(PPN 11%) : Rp. {mealTax} \nTip({tip}%) : Rp.{mealTip} \nTotal : Rp.{mealTotal}")
print("*******************************")