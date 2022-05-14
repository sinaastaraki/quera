from numpy import absolute


nomre=int(input())
rooz=int(input())
if rooz==0:
    print(20)
elif rooz==7:
    print(nomre)
else:
    if rooz>nomre:
        print(0)
    else:
        print(nomre-rooz)