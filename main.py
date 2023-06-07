# #9.82
# x = input()
# z2 = 0
# cnt = 0
# lenX = len(x)
# c = 0
# while True:
#     z1 = (x.index(' ', cnt, lenX))
#     if z1 == 0:
#         cnt += 1
#     elif z1 != 0:
#         c = x.count('o', 0, z1)
#         if c == 0:
#             print('error')
#             break
#     if c != 0:
#         break
# print(c)

# #9.141 a,b

# x = input()
# lenX = len(x)
# c1 = 0
# x1 = 0
# c = 0
# z = 0
# while True:
#     z1 = x[c1]
#     c1 += 1
#     lenX -= 1
#     if z1.isdigit():
#         x1 = int(z1)
#         z += x1
#         if x1 > c:
#             c = int(z1)
#     else:
#         continue
#     if lenX == 0:
#         break
# print(c)
# print(z)

# #9.161
# x = input()
# lenX = len(x)
# lenX1 = len(x)
# cnt = 0
# while True:
#     cnt -= 1
#     c = x[lenX - 1]
#     if (c not in x[0:lenX - 1]) and (c not in x[cnt+1:lenX1]):
#         print(c)
#     lenX -= 1
#     if lenX == 0:
#         break

# #9.166
# x = input()
# lenX = len(x)
# z2 = lenX + 1
# z = x.find(' ', 0, lenX)
# z1 = x.rfind(' ')
# print(f'{x[z1:]} {x[z:z1]} {x[0:z]}')

#9.178 a,b,v,g не осилил надо просить разбор на уроке