#membuat fungsi
def suara_ayam():
    print("kukuruyuk\n")

def luas():
    panjang = int(input("Panjang : "))
    lebar = int(input("lebar : "))
    luas = panjang*lebar
    print("luasnya adalah : ", luas,"\n")

#memanggil fungsi
"""suara_ayam()
luas()"""

#fungsi dengan argument
def harga_ayam(kg):
    harga = 20000*kg
    print("Harga",kg,"kg ayam adalah",harga,"\n")

harga_ayam(2)

def siswa(nama):
    print("Siswa ini bernama : ",nama)

siswa("rapli")

def guru(nama,pelajaran):
    print("Guru ini bernama : ",nama)
    print("Mengajar :",pelajaran,"\n")

guru("maulana","biologi")
guru(nama = "aji",pelajaran = "fisika")
guru(pelajaran = "matematika",nama = "rama")

def harga_makanan(nama,jumlah):
    print("Nama makanan : ",nama)
    harga_makanan = jumlah*20000
    print("Harga : ",harga_makanan,"\n")

harga_makanan("Kue",5)

#fungsi dengan default argument
def data_diri(nama,saudara = 0, kota = "subang"):
    print("Nama : ",nama)
    print("Jumlah Saudara : ",saudara)
    print("Tinggal : ",kota)

data_diri("rapli")




