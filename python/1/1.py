def game1(number):
    A=[int(i) for i in str(number)]
    return max(A)-min(A)
print(game1(18))
