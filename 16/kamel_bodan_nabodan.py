n=int(input())
m=0
for i in range(1,n):
    if n%i==0:
        m=i+m
if m == n:
    print("Yes!")
else:
    print("No!")