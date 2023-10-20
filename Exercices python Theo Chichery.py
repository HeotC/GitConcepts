import numpy as np
a=np.arange(0,21,1)
for i in range(9,16):
    a[i]=a[i]*-1
print (a)

import numpy as np
a=np.arange(15,56,1)
print(a[1:-1])

import numpy as np
a=np.arange(1,13).reshape(3,4)
for i in range(a.shape[0]):
    for g in range(a.shape[1]):
         print(a[i,g], end=" ")
         
import numpy as np
a=np.linspace(5, 50,10)
print(a)

import numpy as np
a=np.random.randint(0,11,5)
print(a)

import numpy as np
a=np.linspace(1,11,1) 
b=np.linspace(2,12,2)   
c=a*b
print(c)
    
import numpy as np
a=np.arange(10,22).reshape(3,4)
print(a)

import numpy as np
a=np.arange(1,30).reshape(4,3)
print("Number of row {} and number of columns {}".format(a.shape[0],a.shape[1]))

import numpy as np
a=np.zeros((4,4))
a[::2,1::2]=1
a[1::2,::2]=1
print(a)

import numpy as np
a=[0,10,20,40,60]
b=[10,30,40]
r=[]
for i in range (len(a)):
    for y in range(len(b)):
        if(b[y]==a[i]):
            r.append(b[y])
print(r) 

import numpy as np
a=[10,10,20,20,30,30]
b=[[1,1],[2,3]]
b=np.unique(b)
print(b)

import numpy as np
x=np.random.randint(10,size=(3,2))
y = np.random.randint(10,size=3)
print(np.cross(x, y))

import numpy as np
z= np.random.random((10,2))
r=np.sqrt(z[:,0]**2+z[:,1]**2)
t=np.arctan(z[:,1]/z[:,0])
print("Polar coordonate {}{}".format(r,t))

import numpy as np
test=np.arange(0,101)
a=float(input("nombre a chercher "))
test2=abs(test-a)
print(test2.argmin())
