class A:

    def demo_a(self):
        return "I\m just a class A mathod !"

    def hello(self):
        return "HEllo from A class"

class B:

    def demo_b(self):
        return "I\m just a class B mathod !"

    def hello(self):
        return "HEllo from B class"

class C(A, B):
    pass

a1= A()
b1= B()
c1= C()
print(a1.demo_a())
print(b1.demo_b())

print(c1.hello())
print(C.mro())