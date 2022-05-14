
#Variation 1
# def game(number):
#     a=int(number/10)
#     b=number %10
#     if number<100:
#         if a>b:
#             return a-b
#         else:
#             return b-a
#     else:
#         return "Enter a number less than 100!"
# print(game(18))
# def game1(number):
#     return max([int(i) for i in str(number)])-min([int(i) for i in str(number)])
# game1(22)
#================================================
#Varation 2
# def game1(number):
#     A=[int(i) for i in str(number)]
#     return max(A)-min(A)
# print(game1(18))
#==============================================
#Variation 3
def game1(number):
    return max(A=[int(i) for i in str(number)])-min(A=[int(i) for i in str(number)])
print(game1(18))
