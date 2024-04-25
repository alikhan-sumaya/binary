'''class a:
    def _init_(self) ->None:
        print("1")
    def _init_(self) ->None:
        print("2")
    def fun1(self):
        print("fun1")
    def fun2(self):
        print("fun2")
class b(a):
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun4")
class c(b):
    def fun5(self):
        print("fun5")
    def fun6(self):
        print("fun6")
o=a()
p=b()
p=c()
p.fun1(
p.fun2()
p.fun3()
p.fun4()
p.fun5()
p.fun6()'''
 
'''class a:
    def _init_(self,a)->None:
        self.a=a
    def fun(self,x):
        self.x=x
        print("fun1")
o=a(3)
o.p=10
print(o.a,o.p)'''

class ab:
    branch="cse"
    def _init_(self,a):
        ab.x=10
        self.a=a
    def fun(self):
        print("fun1",self.branch,self.x)
        print("fun1",ab.branch,ab.x)
o=ab(3)
o.fun()
print(o.a,ab.x)