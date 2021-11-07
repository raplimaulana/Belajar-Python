class Manusia:
    __jumlah_tangan = 2
    def __init__(self,nama):
        self.nama = nama

    @classmethod
    def pengertian(cls):
        print("manusia memiliki",cls.__jumlah_tangan,"tangan")

x1 = Manusia("Rapli")

x1.pengertian()
Manusia.pengertian()
