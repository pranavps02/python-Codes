class A:
    classvar1 = "I am Varialble on A"
    def __init__(self):
        self.var1 = "I am Inside Class A's Constructor"
        self.classvar1 = "Instance var in Class A"
        self.speciala = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):

        super().__init__()
        self.var1 = "I am Inside Class B's Constructor"
        self.classvar1 = "Instance var in Class B"

a=A()
b=B()
print(b.special)
print(b.var1)
print(b.classvar1)