# li =[1,2,3,4,5,6,7,8]

# for i in li:
#     print(i**2)

# li =[1,2,3,4,5,6,7,8]
# def sqr(n):
#     return n**2
# res =map(sqr,li)
# print(list(res))

# li =[1,2,3,4,5,6,7,8]
# def odd(n):
#     if(n%2==1):
    
#       return n
# res = filter(odd,li)

 
# print(list(res))
# print(li)

li =[1,2,3,4,5,6,7,8]
def odd(n):
    if n%2==1:
        
        return n**2
    else:
        return n
res = map(odd(li))

print(map(res))
print(list(res))

# Que.01  WAP to appy prime function on the data source tuple or list. (map and reduce)