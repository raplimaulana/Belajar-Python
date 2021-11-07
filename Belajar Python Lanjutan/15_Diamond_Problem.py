class A:
    def show(self):
        print("Ini adalah show A")

class B(A):
    def show(self):
        print("ini adalah show B")

class C(A):
    def show(self):
        print("ini adalah show C")

class D(B,C):
    pass

x = D()

#yang di pangil urutannya method di kelas D,B,C,A
#help(x)
x.show()