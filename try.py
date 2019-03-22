import random
from Element import ElementClass
c=[ElementClass('O').__str__(),ElementClass('*').__str__()]
#print(c)

d=random.sample(c,1)
#print(d)

x=random.randint(0,4)
y=random.randint(0,4)
print(x)
print(y)
