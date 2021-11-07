class Mahasiswa:
    def __init__(self,nama,nim,jurusan,ip):
        self.__nama = nama
        self.__nim = nim
        self.__jurusan = jurusan
        self.__ip = ip
        self.__sksTotal = 0
        self.__matkul = []

    def inputSks(self,nama,sks):
        self.__matkul.append(nama)
        self.__sksTotal += sks

    @property
    def mataKuliah(self):
        pass

    @mataKuliah.setter
    def mataKuliah(self,input):
        kode,__namaMK,__sks = input

        if (self.__ip >= 3) and (self.__ip <= 4):
            if self.__sksTotal <= 24:
                self.inputSks(__namaMK,__sks)
                print("Data Berhasil Disimpan!")
            else:
                print("SKS TIDAK MENCUKUPI")
        elif self.__ip >= 1 and self.__ip < 3:
            self.inputSks(__namaMK, __sks)
            if self.__sksTotal > 16:
                print("SKS TIDAK MENCUKUPI")
                self.__matkul.pop()
            else:
                print("Data Berhasil Disimpan!")
        elif self.__ip < 1:
            print("Nilai IP anda terlalu rendah, tidak dapat mengambil matkul semester ini")
        else:
            print("jumlah maksimul sks yg diambil adalah 24")

    @property
    def info(self):
        return "Nama\t\t: {} \nNIM\t\t\t: {} \nJurusan\t\t: {} \nip\t\t\t: {} \nmata kuliah\t: {}".format(self.__nama, self.__nim,
                                                                                          self.__jurusan, self.__ip,
                                                                                          self.__matkul)

