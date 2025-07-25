# factorial using for loop
n=int(input("Enter n: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)


# using while loop
n=int(input("Enter n: "))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)