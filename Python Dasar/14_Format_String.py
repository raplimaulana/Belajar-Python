##format string
#string
nama = "rapli"

format_str1 = f"hello{nama}"

print(format_str1)

#boolean
boolean = True

format_str3 = f"boolean : {boolean}"
print(format_str3)

#angka
angka1 = 2005.5

tanpa_format = "angka : " + str(angka1)
print(tanpa_format)

format_str2 = f"angka : {angka1}"
print(format_str2)

#bilangan bulat
angka2 = 15
format_str4 = f"bilangan bulat : {angka2:d}"

#bilangan dengan ordo ribuan
angka3 = 2000
angka4 = 2000000

format_str5 = f"ribuan : {angka3:,}"
format_str6 = f"jutaan : {angka4:,}"

print(format_str5 + "\n" + format_str6 + "\n")

#bilangan desimal
angka1 = 2005.5432

format_str2 = f"desimal : {angka1:.2f}"
print(format_str2)

#menampilkan leading zero
angka5 = 2005.5432
format_str7 = f"desimal : {angka5:9.2f}"
format_str8 = f"desimal : {angka5:09.2f}"
format_str9 = f"desimal : {angka5:010.2f}"

print(format_str7 + "\n" + format_str8 + "\n" + format_str9 + "\n")

#menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.5432

format_minus = f"minus : {angka_minus:+d}"
format_plus = f"plus : {angka_plus:+.2f}"

print(format_minus + "\n" + format_plus + "\n")

#memformat persen
persentase = 0.045

format_persen1 = f"persen : {persentase:%}"
format_persen2 = f"persen : {persentase:.2%}"

print(format_persen1 + "\n" + format_persen2 + "\n")

#melakukan operasi aritmatika di dalam placeholder
harga = 5000
jumlah = 5

format_str10 = f"harga total : Rp.{harga*jumlah}"
print(format_str10)

#format angka lain (binary,octal,hexadecimal)
angka = 255

format_binary = f"binary : {bin(angka)}"
format_octal = f"octal : {oct(angka)}"
format_hex = f"hex : {hex(angka)}"

print(format_binary + "\n" + format_octal + "\n" + format_hex + "\n")