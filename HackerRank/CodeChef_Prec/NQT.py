#Write the sum_of_occurrences function here
def sum_of_occurrences(s1,s2):
    s2=set(s2)
    d={}
    for i in s1:
        d[i]=0
    for i in s1:
        d[i]+1
    count=0
    for i in s2:
        if i in d:
            count=count+d[i]
    return count
t=int(input())
for _ in range(t):
    str1=input().strip()
    str2=input().strip()
    print(sum_of_occurrences(str1,str2))