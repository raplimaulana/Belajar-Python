#queue = first in, first out
from collections import deque

antrian = deque([1,2,3,4,5])
print("Data Sekarang : ",antrian)

antrian.append(6)
print("Data Masuk : ",6)
antrian.append(7)
print("Data Masuk : ",7)
print("Data Sekarang : ",antrian)

antrian.popleft()
print(Queue)
print("Data Sekarang : ",antrian)

