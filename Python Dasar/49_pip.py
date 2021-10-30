##melihat list package yang sudah di install
# $pip list --format=column

#download package di https://pypi.org/
# $pip install numpy

#pycharm harus diinstall sendiri di Project:pythonProject/Python Interpreter, karena memiliki environment yg berbeda (IDE)

import numpy as np

a = [1,2,3,4]
b = [5,6,7,8]

print(a+b,"\n")

c = np.array([1,2,3,4])
d = np.array([5,6,7,8])

print(c+b)