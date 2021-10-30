#input list integer
data = input("Masukan nilai (pisahkan dengan spasi) :")
list  = data.split()

print(list)

for i in range(len(list)):
    list[i] = int(list[i])

print(list)

#menambahkan list
number_list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)