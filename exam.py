# class A:
#     def display(self):
#         print("Class A")
# class B(A):
#     def display(self):
#         super().display()
#         print("Class B")
# class C(B):
#     def display(self):
#         super().display()
#         print("Class C")
# c = C()
# c.display()
#
#
#
#
# class FoodOrder:
#     def __init__(self, restaurant_name, item, price, quantity):
#         self.restaurant_name = restaurant_name
#         self.item = item
#         self.price = price
#         self.quantity = quantity
#     def add_order(self, quantity):
#         self.quantity += quantity
#     def remove_order(self, quantity):
#         if quantity <= self.quantity:
#             self.quantity -= quantity
#         else:
#             print("Cannot remove")
#     def generate_bill(self):
#         total = self.price * self.quantity
#         return f"Total Bill: {total}"
#
# order1 = FoodOrder("Dominos", "Pizza", 250, 2)
# order2 = FoodOrder("KFC", "Burger", 150, 3)
# order1.add_order(1)
# order2.add_order(2)
# order1.remove_order(2)
# order2.remove_order(1)
# print("Bill 1 : ",order1.generate_bill())
# print("Bill 2 : ",order2.generate_bill())
#
#
#
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def grade(self):
#         if self.marks>90:
#             return "A"
#         elif self.marks>80:
#             return "B"
#         elif self.marks>70:
#             return "C"
#         elif self.marks>60:
#             return "D"
#         else:
#             return "Fail"
#     def __add__(self,other):
#         return self.marks+other.marks
#     def __str__(self):
#         return f"{self.name}"
#     def __ge__(self,other):
#         return  self.marks>=other.marks
#     def __lt__(self,other):
#         return self.marks<other.marks
#     def __getattribute__(self, name):
#         print("Accesing Values")
#         return super().__getattribute__(name)
# s2=Student("Chaithanya",90)
# s1=Student("Lalith",70)
# print(s2+s1)
# print(s1>=s2)
# print(s1<s2)

# print("---------NON PRIMES---------")
# n = 5
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# primes = []
# num = 2
# while len(primes) < n * n:
#     if not is_prime(num):
#         primes.append(num)
#     num += 1
#
# for r in range(0,n):
#     a=r
#     for c in range(0,n):
#         print(f"{primes[a]:<3}",end=" ")
#         a+=n
#     print()
#
# print("---------PRIMES---------")
# n = 5
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# primes = []
# num = 2
# while len(primes) < n * n:
#     if  is_prime(num):
#         primes.append(num)
#     num += 1
# for r in range(0, n):
#     a = r
#     for c in range(0, n):
#         print(f"{primes[a]:<3}",end=" ")
#         a += n
#     print()
#
# n=5
# fib = []
# a, b = 0, 1
# for i in range(n * n):
#     fib.append(a)
#     a, b = b, a + b
# for i in range(n):
#     for j in range(n):
#         print(f"{fib[j * n + i]:>4}", end="  ")
#     print()


# # n number of primes
# num = 2
# l=[]
# while len(l)<=100:   # print primes up to 20
#     is_prime = True
#     i = 2
#     while i <= num // 2:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1
#     if is_prime:
#         l.append(num)
#     num += 1
# print(l)

# # in between range
# start, end = 1, 50   # range
# num = start
# while num <= end:
#     is_prime = True
#     i = 2
#     if num==1:
#         is_prime=False
#     while i <= num // 2:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1
#     if is_prime:
#         print(num, end=" ")
#     num += 1
# print("---------------------------Armstrongs---------------------------")
# a=100
# b=2000
# num=a
# while num<=b:
#     temp=num
#     s=0
#     digits=len(str(temp))
#
#     while temp>0:
#         r=temp%10
#         s=s+r**digits
#         temp=temp//10
#     if s==num:
#         print(num,end=" ")
#     num+=1
# print()
# print("---------------------------Palindromes---------------------------")
# a=100
# b=2000
# num=a
# while num<=b:
#     temp=num
#     rev=0
#     while temp > 0:
#         digit = temp % 10
#         rev = rev * 10 + digit
#         temp //= 10
#     if rev==num:
#         print(num,end=" ")
#     num+=1


# n=5
# b=[]
# for i in range(n):
#     b.append(int(input()))
# for i in range(0,n):
#     for j in range(i,n):
#         if b[i]+b[j]==20:
#             print(f"[{b[i],b[j]}]")

a=[1,6,8,9,13,54,67,12,32,45]
# max1=a[0]
# max2=a[0]
# max3=a[0]
# for i in a:
#     if i>max1:
#         max3=max2
#         max2=max1
#         max1=i
#     if i>max2 and i<max1:
#         max3=max2
#         max2=i
#     if i>max3 and i<max2:
#         max3=i
# print(max3)
# b=sorted(a)
# print(f"3rd Maximum number is {b[len(b)-3]}")
for i in range(0,len(a)-1):
    for j in range(0,len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
a.reverse()
print(a[2])