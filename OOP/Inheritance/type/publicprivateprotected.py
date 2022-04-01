# in function overiding,which class method will be called depends on object

# we can not perform function overiding for static method,cause overriding need an object
# static-class, overriding-object
# destructor used to uninitialize object or release a object __del__

# public=global(visible to everwhere), = a
# private(high secure,avl in only main class), =_b
# protected(avl in class and child class) = __c(not implemented in python,shows like public)


class Base:
    def __init__(self,a,b,c):
        self.__a = a #private
        self._b = b  #protected
        self.c = c   #public

    def display(self):
        print("a={0},b={1},c={2}".format(self.__a,self._b,self.c))

class Derived(Base):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    def demo(self):
        print("a={0},b={1},c={2}".format(self.__a,self._b,self.c))

b1 = Base(10,20,30)
b1.display()
print(b1.c)

# d1 = Derived(11,22,33)
# d1.demo() private variable not accesible in base derived class