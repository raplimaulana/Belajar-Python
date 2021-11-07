class A:
    def show(self):
        print("Ini adalah show A")

class B:
    def show(self):
        print("ini adalah show B")


class C(A,B):
    def show(self):
        print("Ini adalah show C")

x = C()

#yang di pangil urutannya method di kelas C,A,B
#help(x)
x.show()