# n=input()
# m=map(int,list(n))
# # for i in m:
# #     print(int(m[int(i)]),end="")
# #     for j in range(int(i)):
# #         print(int(i),':')
# print()

n=input()
m=list(n)
for i in range(len(m)):
    print(f"{m[i]}: {m[i]*int(m[i])}")

