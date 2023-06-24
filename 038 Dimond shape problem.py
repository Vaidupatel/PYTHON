# Remove one by one method of each class, start from class D to A and see the result
class A:
    def met(self):
        print("This is a method from class A")


class B(A):
    def met(self):
        print("This is a method from class B")


class C(A):
    def met(self):
        print("This is a method from class C")


# class D(B, C):
class D(C, B):
    def met(self):
        print("This is a method from class D")


a = A()
b = B()
c = C()
d = D()

d.met()
