a,b,c=input().split()
if (int(a)+int(b)+int(c) == 180) and (int(a)*int(b)*int(c) != 0):
    print("Yes")
else:
    print("No")