'''Print Right Angled Triangle
Print the following pattern (check the sample output):
Sample 1:
Input
Output
 
*
**
***
****
*****    '''
# cook your dish here
n=6
for i in range(1,n+1):
    print()
    for j in range(1,i):
        print("*",end="")
    