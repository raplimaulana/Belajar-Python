a = 9
b = 5

#or
c = a|b

print("######## OR ########")
print("nilai : ",a,", binary : ",format(a,"08b"))
print("nilai : ",b,", binary : ",format(b,"08b"))
print("---------------------------------- (|)")
print("hasil : ",c,", binary : ",format(c,"08b\n"))

#and
d = a&b

print("######## and ########")
print("nilai : ",a,", binary : ",format(a,"08b"))
print("nilai : ",b,", binary : ",format(b,"08b"))
print("---------------------------------- (&)")
print("hasil : ",d,", binary : ",format(d,"08b\n"))

#xor
e = a^b

print("######## XOR ########")
print("nilai : ",a,", binary : ",format(a,"08b"))
print("nilai : ",b,", binary : ",format(b,"08b"))
print("---------------------------------- (^)")
print("hasil : ",e,", binary : ",format(e,"08b\n"))

#not        *not 1 = -2
f = ~a

print("######## not ########")
print("nilai : ",a,", binary : ",format(a,"08b"))
print("---------------------------------- (~)")
print("hasil : ",e,", binary : ",format(e,"08b\n"))

#shift right
g = a >> 1

print("######## SHIFT RIGHT ########")
print("nilai : ",a,", binary : ",format(a,"08b"))
print("---------------------------------- (>>)")
print("hasil : ",g,", binary : ",format(g,"08b\n"))

#shift left
h = a << 1

print("######## SHIFT LEFT ########")
print("nilai : ",a,", binary : ",format(a,"08b"))
print("---------------------------------- (<<)")
print("hasil : ",g,", binary : ",format(g,"08b\n"))