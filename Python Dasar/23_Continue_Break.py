for i in range(10):
    if i == 5:
        print("data ke 5 ditemukan")
    print("data ke : ", i)
print("SELESAI\n")

#break
for i in range(10):
    if i == 5:
        print("data ke 5 ditemukan")
        break
    print("data ke : ", i)
print("SELESAI\n")

#continue (langsung dilanjutkan kembali proses looping)
for i in range (10):
    if i == 5:
        print("data ke 5 ditemukan")
        continue
    print("data ke : ",i)
print("SELESAI\n")

#pass (buat dummy if,for)
for i in range(10):
    pass
