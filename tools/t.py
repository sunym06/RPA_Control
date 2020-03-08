class A(object):
    a = '123'
    def get(self):
        return self.a

class B(A):

    def g(self):
        n = self.__class__.__name__
        return n


class C(B):
    c = self.__class__.__name__
s = C()
print(s.gg())