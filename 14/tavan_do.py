n=int(input())
tavan=1
while True:
    if n<2**tavan:
        print(2**tavan)
        break
    else:
        tavan=tavan+1