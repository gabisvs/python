"""

"""

#shallow copy(jeito ruim)
a = [1, 2, 3, 4, 5]
b = a

print(a)
print(b)

b.append(6)

print(a)
print(b)

print(id(a))
print(id(b))

#deep copy

a = [1, 2, 3, 4, 5]
b = a.copy()

print(a)
print(b)

b.append(6)

print(a)
print(b)

print(id(a))
print(id(b))



