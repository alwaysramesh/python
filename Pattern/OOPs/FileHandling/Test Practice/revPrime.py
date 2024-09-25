for num in range(10, 101):
    reversed_num = int(str(num)[::-1])
    if reversed_num > 1:
        prime = True
        for i in range(2, reversed_num):
            if reversed_num % i == 0:
                prime = False
                break
        if prime:
            print(num, reversed_num)
            
