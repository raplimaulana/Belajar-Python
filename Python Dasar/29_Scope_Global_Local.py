#variabel local
namakucing = "cassandra"

def rubahnama(namabaru):
    namakucing = namabaru
    return namakucing

print(namakucing)
print(rubahnama("kettie"))

print(namakucing,"\n")

#variabel gblobal
namaanjing = "kaori"

def rubahnama2(namabaru):
    global namaanjing
    namaanjing = namabaru
    return namaanjing

print(namaanjing)
print(rubahnama2("kettie"))
print(namaanjing)

