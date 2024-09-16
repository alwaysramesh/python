# packing and unpacking tuple
# =========================================
# a=(1,3,54,65,100)
# b=list(a)
# b.append(101)
# a= tuple(b)
# print(a)

a = (12,23,3,1.2, 45,67,78,4,100,[112,63,34])

a[9].append(35)
a[9].sort()
print(a)

print(a[::-1])