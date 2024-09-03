#1 program to print half pyramid pattern of number

try:
    n= int(input("Enter no. of rows:"))
    def pattern1(n):
        for i in range (1,n+1):
            for j in range (1,i+1):
                print(i, end=" ")
            print()
    pattern1(n)

except Exception:
        print("invalid input. please enter integers only.")

#2 Program To print Inverted Half Pyramid of Numbers.
try:
    n= int(input("Enter no. of rows:"))
    def pattern2(n):
        for i in range (n,0,-1):
            for j in range (i,0,-1):
                 print(i, end=" ")
            print()
    pattern2(n)
except ValueError:
    print("Invalid input. Please enter integers only.")

#3 Program To print Full Pyramid Pattern of Numbers

try:
    n= int(input("Enter no. of rows:"))
    def pattern3(n):
        for i in range(1, n + 1):
            for j in range(1,2*n):
               if j>(n-i) and j<(n+i):
                print(i, end=" ")
               else:
                print(" ", end=" ")
            print()
    pattern3(n)
except ValueError:
    print("invalid input. please enter integers only.")

#4.Program To Pyramid of Numbers  in 180 Degree

try:
    n= int(input("Enter no. of rows:"))
    def program4(n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(i, end=" ")
            print()
        for i in range(n-1,0,-1):
            for j in range(i,0,-1):
                print(i, end=" ")
            print()
    program4(n)
except ValueError:
    print("invalid input. please enter integers only.")

#5.Program to print a triangle 

try:
    n = int(input("Enter number of rows:"))
    def pattern5(n):
        for i in range (1,n+1):
            for j in range(i):
               print("*", end=" ")
            print()
    pattern5(n)
except ValueError:
    print("invalid input. please enter integers only.")

#6.Program To Print Character Pyramid Pattern

try:
    n= int(input("Enter no. of rows:"))
    def pattern6(n):
        k= ord("A")
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(chr(k), end="" )
            print()
            k = k+1
    pattern6(n)
except ValueError:
    print("invalid input. please enter integers only.")

#7.Print continuous character patterns

try:
    n = int(input("Enter number of rows:"))
    def pattern7(n):
       k= ord("A")
       for i in range(n):
           for j in range(i+1):
                print(chr(k), end=" ")
                k += 1
           print()
    pattern7(n)
except ValueError:
    print("invalid input. please enter integers only.")

#8. Print the hollow star pyramid pattern

try:
    n = int(input("Enter no. of rows:"))
    def pattern8(n):
        for i in range(1,n+1):
            for j in range(1,2*n):
                if i==n or i+j==n+1 or j-i==n-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    pattern8(n)
except ValueError:
    print("invalid input. please enter integers only.")

