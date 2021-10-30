#pangkat
def pangkat(a,b):
    if b == 0:
        return 1
    else:
        return a*pangkat(a,b-1)

print(pangkat(2,3))

#faktorial
def faktorial(n):
    if n == 1:
        return 1
    else:
        return n*faktorial(n-1)

input_user = 4

for i in range(input_user,0,-1):
    print(i,"!",end = " x ")
print("=",faktorial(input_user))

#fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

input_user = 7

for i in range(input_user+1):
    print(fibonacci(i),end = " ")
