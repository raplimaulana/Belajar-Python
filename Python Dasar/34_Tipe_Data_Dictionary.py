#dictionary
member_1 = {"ID":101,
          "Nama":"Rapli Maulana",
          "Pekerjaan":"Mahasiswa",
          "Status Member":"Gold"}

member_2 = {"ID":102,
          "Nama":"Ricardo Kaka",
          "Pekerjaan":"Atlet",
          "Status Member":"Silver"}

memberlist = {101:member_1,102:member_2}

print(member_1)
print(member_1["Pekerjaan"])
print(member_1.keys())
print(member_1.values())
print(member_1.items())

print(memberlist[101])
