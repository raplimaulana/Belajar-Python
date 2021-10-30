from PIL import Image

x1 = Image.open("49_fix_edit.png")

print("Format file : ",x1.format)
print("Ukuran file : ",x1.size)
print("Mode file : ",x1.mode)


x1.show()