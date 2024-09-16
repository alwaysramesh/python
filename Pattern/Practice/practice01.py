for _ in range(int(input("number"))):

    def reverse(n):
        sum=0
        while(n!=0):
            b=n%10
            sum=sum*10+b
            n=n//10
        return sum
    print( sum)
    
    # def sumOfDigits(n):
    #     sum=0
    #     while(n!=0):
    #         b=n%10
    #         sum=sum+b
    #         n=n//10
    #     return sum
    
    # def productOfDigits(n):
    #     product=1
    #     while(n!=0):
    #         b=n%10
    #         product=product*b
    #         n=n//10
    #     return product
    
    # def isPalindrome(n):
    #     a=n
    #     sum=0
    #     while(n!=0):
    #         b=n%10
    #         sum=sum*10+b
    #         n=n//10
    #     if sum==a:
    #         return True
    #     return False

    # n=int(input())
    # if(n%2==0):
    #     x=sumOfDigits(n)
    #     y=isPalindrome(x)
    #     if(isPalindrome(y)==True):
    #         m=sumOfDigits(y)
    #         k=isPalindrome(m)
    #         print(k)
    #     else:
    #         l=reverse(y)
    #         print(l)
    # else:
    #     x=productOfDigits(n)
    #     y=sumOfDigits(x)
    #     print(y)