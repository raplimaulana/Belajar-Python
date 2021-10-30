
while True :
    try:
        penyebut = int(input("Masukan angka penyebut : "))
        pembilang = int(input("Masukan angka pembilang : "))
        hasil = penyebut/pembilang
        break

#    except ValueError:
#        print("yang anda masukan bukan angka")
#    except ZeroDivisionError:
#        print("pembilang tidak boleh nol")

    except Exception as error:
        print(error)
print("Berhasil, hasil pembagian adalah",hasil)