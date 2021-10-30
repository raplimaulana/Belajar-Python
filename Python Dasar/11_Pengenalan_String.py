#cara membuat string

#1 menggunakan single quotes (')
data1 = 'menggunakan single quotes'

#2 menggunakan double quotes
data2 = "menggunakan double quotes"

print(data1)
print(data2)

#membuat tanda ' menjadi string
print("ini adalah hari jum'at")
print('ini adalah hari jum\'at')

#backslash
print("C:\\user\\rapli")

#tab
print("rapli\tmaulana")

#backspace
print("rapli \bmaulana")

#newline
print("ini baris petama.\nini baris kedua")     #LF   -> Line Feed                  (UNIX,LINUX,MAC OS)
print("ini baris petama.\rini baris kedua")     #CR   -> Carriage Return            (Commodore,Acorn,Lisp)
print("ini baris petama.\r\nini baris kedua")   #CRLF -> Line Feed Carriage Return  (Windows)

#raw string
print("C:\\user\\rapli")
print(r"C:\user\rapli")

#multiline literal string
print("""
nama  : rapli
kelas : b
""")

#multiline literal string dan raw
print(r"""
nama  : rapli
kelas : b\new class
web   : www.raplimaulana/newid
""")
