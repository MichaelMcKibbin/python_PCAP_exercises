print("\n#============================")


def myfun():
    for num in range(3):
        yield num

for i in myfun():
    print(i)


print("\n#============================")



b=bytearray(3)
print(b)

print("\n#===========================")

def I():
    s='abcdef'
    for c in s[::2]:
        yield c

for x in I():
    print(x,  end='')



print("\n#===========================")

# import os
# os.mkdir('testdir')
# os.chdir('testdir')
# sizes=['small','medium','large']
# for size in sizes:
#     os.mkdir(size)
# print(os.listdir())


print("\n#===========================")

from datetime import date
d1=date(1992,1,16)
d2=date(1991,2,5)
print(d1-d2)


print("\n#===========================")

from datetime import datetime
dt=datetime(2020,11,17,12,30,45)
print(dt.strftime("%y-%B-%d %H:%M:%S"))

print("\n#===========================")

def fun_cross(n):
    s='+'
    for i in range(n):
        s+=s
        yield s

for x in fun_cross(2):
    print(x, end='')

print("\n#===========================")

#
# import os
# os.mkdir('pictures')
# os.chdir('pictures')
# os.mkdir('thumbnails')
# os.chdir('thumbnails')
# os.mkdir('tmp')
# os.chdir('../')
#
# print(os.getcwd())

print("\n#===========================")

my_tuple=(0,1,2,3,4,5,6)

foo= tuple(filter(lambda x: x > 1, my_tuple))
print(foo)

foo2= list(filter(lambda x: x ==0 and x== 1, my_tuple))
print(foo2)

foo3= list(filter(lambda x: x - 0 and x - 1, my_tuple))
print(foo3)

foo4= tuple(filter(lambda x: x - 0 and x - 1, my_tuple))
print(foo4)

print("\n#===========================")


import math
print(dir(math))



print("\n#===========================")
print(__name__)





print("\n#===========================")

numbers2=[0,2,7,9,10]
foo5 = lambda x: x*2, numbers2
foo6 = map(lambda x:x**2, numbers2)
foo7 = lambda x:x**2,numbers2
foo8 = filter(lambda x:x**2, numbers2)
print(list(foo5))
print(list(foo6))
print(list(foo7))
print(list(foo8))



print("\n#===========================")


numbers3 = [i*i for i in range(5)]
foo9=list(filter(lambda x: x % 2, numbers3))
print(foo9)



print("\n#===========================")

import random
a=random.randint(0,100)
b=random.randrange(10,100,3)
c=random.choice((0,100,3))
print(a,b,c)











print("\n#===========================")

class A:
    def __init__(self):
        pass

a=A()
print(hasattr(a,"A"))

class B:
    def __init__(self,v):
        self.__a=v+1
a=B(0)
print(a._B__a)


print("\n#===========================")

#
# for x in open('jekyll-notes.txt', 'rt'):
#     print(x)
#


print("\n#===========================")

var=1
assert var !=0




print("\n#===========================")

datetime5=datetime(2019,11,27,11,27,22)
datetime6=datetime(2019,11,26,0,0,0)
print(datetime5 - datetime6)




print("\n#===========================")

class C:
    C=1
    def __init__(self):
        self.c=1
print(hasattr(C,"C"))
print(hasattr(C,"c"))




print("\n#===========================")

class D:
    def __init__(self,v):
        self.__d=v+1
d=D(0)
print(d._D__d)


print("\n#===========================")

numbers17=[i*i for i in range(5)]
foo7=list(filter(lambda x: x % 2, numbers17))
print(foo7)

print("\n#===========================")