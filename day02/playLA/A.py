class A():
    def __init__(self):
        pass
    def __getitem__(self, item):
        return item
# a = A([2232, 333])
a = A()
print(a[3])
print(a[43])