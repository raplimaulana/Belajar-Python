#list
kumpulan_club = ["Livepool","Chelsea","Arsenal","Tottentham","Milan"]
kumpulan_pemain = ["Mane","Lukaku","Ozil","Kane"]

for i in range(len(kumpulan_club)):
    print(kumpulan_club[i])
print("\n")


#enumerate
for index,club in enumerate(kumpulan_club):
    print("[",index,"]"," ",club)
print("\n")

#zip
for club,pemain in zip(kumpulan_club,kumpulan_pemain):
    print(club,"memiliki pemain bernama",pemain)
print("\n")

#set
sepatu = {"nike","adidas","puma","new balane","carvil"}

for jenis in sorted(sepatu):
    print(jenis)

