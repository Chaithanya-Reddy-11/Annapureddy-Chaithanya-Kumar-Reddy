n=int(input())
c=0
c1=0
sum1=0
sumA=0
l=[]
l1=[]
for i in range(1,n+1):
    power = len(str(i))
    n1=i
    sum = 0
    while n1!=0:
        d=n1%10
        sum+=d**power
        n1=n1//10
    if sum==i:
        c=c+1
        l.append(i)
        sum1+=i
        if c%2==0:
            c1+=1
            l1.append(i)
            sumA=sumA+i
print()
print(l)
print(l1)
print("Continuos Armstrong Numbers")
print("Average = " ,sum1/c)
print("Sum = " ,sum1)
print("Alternative Armstrong Numbers")
print("Average = " ,sumA/c1)
print("Sum = " ,sumA)