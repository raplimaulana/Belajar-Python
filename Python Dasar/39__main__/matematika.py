#print(__name__)                 #kalo program ini dijalankan muncul "__main__"
                                 #tapi kalo dijalankan di file lain sebagai import muncul sebagai "__matematika__"
def Utama():
    print("Ini Adalah FIle Rumus Matematika")

def Tambah(a,b):
    return  a + b

def Kurang(a,b):
    return a - b

if __name__ == "__main__":
    print("Ini adalah program utama")
else:
    print("file import")