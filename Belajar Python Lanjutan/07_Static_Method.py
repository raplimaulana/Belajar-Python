class Mahasiswa:
    def __init__(self,nama):
        self.__nama = nama

    def getNama(self):
        return self.__nama

    @staticmethod
    def hurufBesar(nama):
        return nama.upper()

x1 = Mahasiswa("Rapli")

print(x1.getNama())

print(x1.hurufBesar(x1.getNama()))
print(Mahasiswa.hurufBesar("maualana"))
