class Mangga:

    #otomatis akan dieksekusi saat pembuatan class
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah

    #otomatis akan mengeluarkan output saat class dipanggil,jika tidak ada __str__ (digunakan pada proses debuging)
    def __repr__(self):
        return "Debuging \nMangga : {} \njumlah : {}".format(self.nama,self.jumlah)

    #otomatis akan mengeluarkan output saat class dipanggil (program sudah jadi)
    def __str__(self):
        return "Mangga : {} \njumlah : {}".format(self.nama,self.jumlah)

    #menambahkan 2 variabel pada 2 object
    def __add__(self, other):
        return self.jumlah + other.jumlah

belanja1 = Mangga("Arumanis",10)
belanja2 = Mangga("Arumanis",5)

print(belanja1)
print()

print(repr(belanja1))
print()

print(belanja1+belanja2)

