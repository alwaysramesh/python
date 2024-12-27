'''Loop and Print Sequence - MCQ
What does the following code snippet do?

count = 0
while count < 5:
    print(count, end=" ")
    count += 1

    Select one of the following options:
01) Prints numbers 0 to 4 with spaces
02) Prints numbers 1 to 5 with spaces
03) Prints numbers 0 to 4 without spaces
04) Prints numbers 1 to 5 without spaces'''
#Correct:- Prints numbers 0 to 4 with spaces

#Que.00
'''While Loop Increment - MCQ
What is the output of the following code snippet?

x = 0
while x < 5:
    print(x, end=" ")
    x += 2
    
    Select one of the following options:
01) 0 2 4 6
02) 0 2 4
03) 2 4 6
04) 0 2 4 6 8'''
#correct= 0 2 4

#Que. 03
'''Evaluation in while
In a while loop, when does the condition get evaluated?

Select one of the following options:

01) Before each iteration
02) After each iteration
03) Only at the start of the loop
04) Only at the end of the loop'''
#Correct:-Before each iteration

#Que.04 MCQ
'''While Loop Initial Condition - MCQ
What happens if the initial condition of a while loop is false?

Select one of the following options:

01) The loop executes once.
02) The loop runs indefinitely
03) The loop is skipped, and the code inside is not executed
04) The loop throws an error'''
#Correct= The loop is skipped, and the code inside is not executed

#Que.05 MCQ
'''Suspicious Loop - MCQ
What does the following code snippet do?

x = 1
while x > 0:
    print(x, end="")
    x += 1
Select one of the following options:

01) Syntax error
02) Infinite loop
03) Compilation error
04) None of the above '''
#Corrct= Infinite loop

#Que.06
'''Number of evaluation
How many times will the following while loop execute?

x = 5
while x > 0:
    print(x, end=" ")
    x -= 1
    
    Select one of the following options:
01) 4
02) 5
03)6
04) Infinite loop'''
#Correct=5

#Que.07
'''Printing using While
number = 10
while number > 0:
    print(number)
    number -= 2
    
    Select one of the following options:

01) Prints numbers from 10 to 1 in steps of 2
02) Prints even numbers from 10 to 2
03) Prints odd numbers from 9 to 1
04) Enters an infinite loop'''
#Correct=Prints even numbers from 10 to 2
#Que.08 MCQ
'''Print Squares
Write a program that utilizes a while loop to print the squares of numbers from 1 to 
N
N.

Check the sample input / output below further clarity

Sample 1:
Input
Output
5
1 4 9 16 25'''
#Code:- 
num = int(input())
# Update your code below this line
for i in range(1,num+1):
    print(i*i,end=" ")
    num+=1

#Que.09 MCQ
'''String repetition
In Python, you can multiply strings to create a new string that repeats the original string a certain number of times. This technique is known as string repetition or string replication.

The multiplication operator (*) is used to repeat a string a specified number of times.

string = "hello "
result = string * 3
print(result) # output: hello hello hello

# string is assigned the value `hello`.
# string * 3 creates a new string by repeating `hello` three times.
# The result, `hello hello hello`, is stored in the variable result and printed.
Task
Write a program to print the word tenet 100 times'''
# Update your code below this line
string="tenet"
result=string*100
print(result)
#next day.
