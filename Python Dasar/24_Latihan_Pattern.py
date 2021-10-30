n = int(input("Masukan nilai n : "))

for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print("")

for i in range(n+1,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
print("")

for i in range(n+1):
    for j in range(i):
        print(j+1,end="")
    print("")

