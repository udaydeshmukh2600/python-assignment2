value=int(input("Enter a number:"))
print(type(value))             # Data Type
print(id(value))               # Memory Address

from sys import getsizeof
print (getsizeof(value))   # Size of Variable