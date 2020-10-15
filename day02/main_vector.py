from playLA.Vector import Vector
# 初始化向量值
lst = [120, 3, 2, 2]
vec1 = Vector(lst)
lst2 = [2, 3, 2, 2, 3]
vec2 = Vector(lst2)
print(vec1)
print(vec2)
# unsupported operand type(s) for +: 'Vector' and 'Vector'
# res = vec1 + vec2
# res2 = vec1 - vec2
# print(res)
# print(res2)
# # TypeError: object of type 'Vector' has no len()
# print(len(vec))
# print(vec[0]) # 'Vector' object is not subscriptable
# print(vec[1]) # 'Vector' object is not subscriptable
# <playLA.Vector.Vector object at 0x00000232D7EFE688>
# print(5*vec1)
print(vec1*5)
print(5*vec1)
print(+vec1)
print(-vec1)

zero2 = Vector.zero(len(vec2))
print(zero2)
print(zero2 +vec2)