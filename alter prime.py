# a=int(input())
# b=int(input())
# c=0
# p=0
# for i in range(a,b+1):
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc+=1
#     if fc==2:
#         c+=1
#         if c%2==1:
#             p=p+1
#             if p==1:
#                 print(i,end="")
#             else:
#                 print(",",i,end=" ")


# a=int(input("enter the number = "))
# b=int(input("enter the number = "))
# c=0
# d=0
# for i in range(a,b+1):
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc+=1
#     if(fc==2):
#         c=i
#         break
# for i in range(b-1,1,-1):
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc+=1
#     if(fc==2):
#         d=i
#         break
# print("c = ",c)
# print("d = ",d)
# print(f"difference b/w {c} and {d} = ",d-c)

# n=int(input("enter the number = "))
# f=0
# b=0
# if n==1:
#     print("Nearest Prime is ",2)
# else:
#     f = n + 1
#     while True:
#         fc=0
#         for i in range(1,f+1):
#             if f%i==0:
#                 fc+=1
#         if fc==2:
#             break
#         f=f+1
#         #print(f)
#     for i in range(n-1,1,-1):
#         fc=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 fc+=1
#         if fc==2:
#             b=i
#             #print(b)
#             break
#     a=f-n
#     a1=n-b
#     if a>a1:
#         print("Nearest Prime is ",b)
#     elif a<a1:
#         print("Nearest Prime is ",f)
#     else:
#         print("Nearest Primes are ",b,f)

#Factorial
# n = int(input())
# fact = 1
# fact1 = 1
# c = 0
# if n >= 0:
#     #print("1", end="")
#     for i in range(1,n + 1):
#         fact *= i
#         fact1 += fact
#         if c == 1:
#             print(f"{fact}", end="")
#         else:
#             print(f"+{fact}", end="")
#
#     print(f"={fact1}")
# else:
#     print("INvalid INput")

#no of digits in a number
# n=int(input("enter the number"))
# c=0
# while True:
#     n=n//10
#     c += 1
#     if n==0:
#         break
# print(c)

#Prime digit in a number
# n = int(input("Enter the number: "))
# while n!=0:
#     n1 = n % 10
#     fc=0
#     for i in range(1,n1+1):
#             if n1%i==0:
#                 fc+=1
#     if fc==2:
#         print(n1,end=" ")
#     n = n // 10

#Highest digit in a number
# n = int(input("Enter the number: "))
# b=0
# while n!=0:
#     r = n % 10
#     fc=0
#     if r>b:
#         b=r
#     n = n // 10
# print(f"Greatest number is {b}.")

#Lowest digit in a number
# n = int(input("Enter the number: "))
# b=10
# while n!=0:
#     r = n % 10
#     fc=0
#     if r<b:
#         b=r
#     n = n // 10
# print(f"Lowest number is {b}.")

#Diff b/w Greatest and Smallest digit in a number
# n = int(input("Enter the number: "))
# b=10
# a=0
# while n!=0:
#     r = n % 10
#     if r<b:
#         b=r
#     if r>a:
#         a=r
#     n = n // 10
# print(a-b)

#Palindrome
# n = int(input("Enter the number: "))
# m=n
# rev = 0
# while n!=0:
#     n1 = n % 10
#     rev = rev * 10 + n1
#     n = n // 10
# print("Reversed number:", rev)
# n=m
# if rev==n:
#     print("Palindrome")

#All palindromes in a given range
# a=int(input("enter number"))
# b=int(input("enter number"))
# for i in range(a,b+1):
#     rev=0
#     t=i
#     while t!=0:
#         r=t%10
#         rev=rev*10+r
#         t=t//10
#     if rev==i:
#         print(i,end=" ")



#
# n=int(input())
# n1=int(input())
# if n<0 or n1<0:
#     print("Invalid Inputs")
# else:
#     if n>n1:
#         n,n1=n1,n
#     palindromes=[]
#     for i in range(n,n1+1):
#         m=i
#         rev=0
#         while m!=0:
#             r=m%10
#             rev=rev*10+r
#             m//=10
#         if rev==i:
#             palindromes.append(i)
#     if palindromes:
#         print(*palindromes)  # prints in one line, space-separated
#     else:
#         print("No Palindrome Values")

# n = int(input())
# n1 = int(input())
# if n < 0 or n1 < 0:
#     print("Invalid Inputs")
# else:
#     if n > n1:
#         n, n1 = n1, n
#     a, b = 0, 1
#     found = False
#     while a <= n1:
#         if a >= n:
#             print(a, end=" ")
#             found = True
#         a, b = b, a + b
#     if not found:
#         print("No Fibonacci Series Values")
#
#

# n = int(input())
# n1 = int(input())
# if n < 0 or n1 < 0:
#     print("Invalid Inputs")
# else:
#     if n > n1:
#         n, n1 = n1, n
#     a, b = 0, 1
#     count = 0
#     total = 0
#     index = 0
#     while a <= n1:
#         if a >= n:
#             index += 1
#             if index % 2 == 1:   # take alternative terms
#                 total += a
#                 count += 1
#         a, b = b, a + b
#     if count == 0:
#         print("No Fibonacci Series Values")
#     else:
#         print(f"{total/count:.2f}")

