class Vector():
    def __init__(self, lst):
        # _values 属性私有
        self._values = lst
    def __len__(self):
        # 返回向量的长度
        return len(self._values)
    def __repr__(self):
        return "Vector({})".format(self._values)
    def __str__(self):
        return "({})".format(", ".join([str(e) for e in self._values]))

