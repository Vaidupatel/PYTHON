class A:
    classvar1 = "I am a clasvar in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        # If there is instance variable in constructor than at call time it will be called
        self.classvar1 = "I am instance variable in class A"
        self.special = "Special"


class B(A):
    classvar1 = "I am class variable in class B"
    classvar2 = "I am class variable in class B"

    def __init__(self):
        # super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "I am instance variable in class B"
        super().__init__()
        print(super().classvar1)


a = A()
b = B()

# It will fist check for instance variable in class B,
# if there is not than it will be goes for instance variable of inherited class,
# If there is not than it will check for class variable of class B,
# if there is not than it will go for the inherited class variable
# It is called Overriding

print(b.classvar1)
# If there is no supper() in child class method than this will be not executed
print(b.special, b.var1, b.classvar1)
