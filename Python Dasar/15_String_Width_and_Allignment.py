#width dan multiline
#data

data_nama = "rapli maulana aji"
data_umur = 23
data_tinggi = 170.4
data_nomor_sepatu = 44

#string standard
data_string = f"nama : {data_nama}, umur : {data_umur},tinggi : {data_tinggi} ,nomor sepatu : {data_nomor_sepatu}"

print(5*"=" + " DATA STRING "+ 5*"=")
print(data_string)

#string multiline (menggunakan newline \n)
data_string = f"nama : {data_nama}, \numur : {data_umur}, \ntinggi : {data_tinggi} , \nnomor sepatu : {data_nomor_sepatu}"
print(data_string)

#string multiline dengan triplet
data_string = f"""
nama         = {data_nama}
umur         = {data_umur:>10}
tinggi       = {data_tinggi}
nomor sepatu = {(data_nomor_sepatu)}
"""

print(5*"=" + " DATA STRING "+ 5*"=")
print(data_string)