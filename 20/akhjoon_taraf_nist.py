a=int(input())
I=input().split()
b=int(input())
II=input().split()
c=int(input())
III=input().split()

A=I+II+III
TA=set(A)
B=7-len(list(TA))
print(B)