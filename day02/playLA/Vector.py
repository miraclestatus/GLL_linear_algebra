class Vector():
    def __init__(self, lst):
        # _values 属性私有
        self._values = lst
    @classmethod
    def zero(cls, dim):
        """返回一个dim维度的向量"""
        return cls([0]*dim)
    def __add__(self, another):
        assert len(self) == len(another), "Error in  adding . length of vectors must be same"
        # return Vector([a + b for a, b in zip(self._values, another._values)])
        return Vector([a + b for a, b in zip(self, another)])
    def __sub__(self, another):
        assert len(self) == len(another), "Error in  subtracting . length of vectors must be same"
        return self, another
    def __mul__(self, k):
        """返回向量数量乘法的结果向量  self * k"""
        return Vector([k*e for e in self])
    def __rmul__(self, k):
        """ k * self"""
        return self*k
        # return Vector([k*e for e in self])
    def __pos__(self):
        """返回向量取正的结果"""
        return 1*self
    def __neg__(self):
        """返回向量取负的结果"""
        return -1*self
    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()
    def __len__(self):
        # 返回向量的长度
        return len(self._values)
    def __getitem__(self, index):
        """取出向量的第index个元素"""
        # return "haha"
        return self._values[index]
    def __repr__(self):
        return "Vector({})".format(self._values)
    def __str__(self):
        return "({})".format(", ".join([str(e) for e in self._values]))

