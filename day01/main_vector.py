from playLA.Vector import Vector
# 初始化向量值
lst = [120, 3, 2, 2, 666]
vec = Vector(lst)
print(vec)
# TypeError: object of type 'Vector' has no len()
# print(len(vec))

print(vec[1]) # 'Vector' object is not subscriptable
# <playLA.Vector.Vector object at 0x00000232D7EFE688>