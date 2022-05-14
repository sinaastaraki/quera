# How generate a dict from a list in python?
#there is three ways 1-dict.fromkeys 2-zip() 3-comperhension list
# def fruits():
#     pass

# a='hello'
# b=list(a)
# print(b)
# c=tuple(b)
# print(c)

from re import A
from unicodedata import name


# fruits=((
#     {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
#     {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
#     {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
#     {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}))

# def fruit(fruits):
#     b=[]
#     c={}
#     counter=0
#     A=list(fruits)
    
#     print(A[1]['name'])


    #===========================
    # for i in A:
    #     if 300<=i['mass']<=600 and 100<=i['volume']<=500:
    #         c.update(i)
    #     else:
    #         continue
        
        

# fruit(fruits)



A=['apple','apple','mango']
# def f():
#     A=['apple','apple','mango']
#     b=[]
#     for i in A:
#         x=i.count(i)
#         b.append(x)
#     return b
# print(f())
# print(set(A))
# print(A.count('apple'))
print(dict.fromkeys(A))