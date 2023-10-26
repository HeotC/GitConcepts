import math as m

v=float(input("enter Volume"))
n=float(input("enter mol"))
R=0.082
t=float(input("enter Temperature"))
P=n*R*t/v

print("volume ={},température= {} pression= {}".format(v,t,P))
r=float(input("rayon"))
h=float(input("hauteur"))
V=(1/3)*m.pi*r**2*h
print(V)

ang=float(input("angle"))
ang_rad=ang*m.pi/180
si=m.sin(ang_rad)

nb1=int(input("nombre 1"))
nb2=int(input("nombre 2"))
som=nb1+nb2
prod=nb1*nb2
print("som =",som)
print("product =",prod)

Temp=float(input("température"))
print("Temperature en kelvin ",Temp+273.15)

edge=float(input("coté"))
area=6*edge**2
vol=edge**3
print("Area= {} and Volume= {}".format(area,vol))

euro10=int(input("nombre billts 10"))
euro20=int(input("nombre billts 20"))
euro50=int(input("nombre billts 50"))
tot=euro10*10+euro20*20+euro50*50
print("totale=",tot)

import math as m
rad=float(input("rayon?"))
long=2*m.pi*rad
air=m.pi*rad**2
print("longueur {} et aire {}".format(long,air))

import math as m
TEMP=float(input("temperature"))
A=3.718*10**13
E=float(input("E"))+273.15
RESUL=A*m.exp(-E/(8.31*TEMP))
print (RESUL)

import math as m
Cotea=float(input("cote1 "))
Coteb=float(input("cote2 "))
Angle=float(input("angle "))
c=Cotea**2+Coteb**2-(2*Cotea*Coteb*m.cos(m.radians(Angle)))
c=m.sqrt(c)
print(c)

message='good morning'
print(message[:-1])
print(message.lower())
print(message.count('g'))

num=5
if num>=5 :
    print("the nuber is {num}")

weight=float(input("weight"))
height=float(input("height"))
BMI=weight/height**2
unite=input("CM or M")
if BMI<18.5:
    print("underweight")
elif 18.5<BMI<25:
    print("normal")
elif 25<BMI<30:
    print("overweight")
else:
    print("obesity")
    
n1=int(input("nombre 1 "))
n2=int(input("nombre 2 "))
q=n1/n2
r=n1%n2
if n1%n2==0 :
    
    print("{} is divisible by {} and the quotient is {}".format(n1,n2,q))
else :
   q=round(q)
   print("{} is not divisible by {} and the quotient is {} and the rest is {}".format(n1,n2,q,r))
   
n1=int(input("nombre 1 "))
n2=int(input("nombre 2 "))
n3=int(input("nombre 3 "))
if n1<n2 and n1<n3 :
    print("{} is the lower".format(n1))
elif n3<n2 and n3<n1 :
    print("{} is the lower".format(n3))
else  :
    print("{} is the lower".format(n2))
    
number=int(input("number of units "))
Price=0.
if 100<number<=200:
    Price =(number-100)*5
elif number>200 :
    Price =100*5+(number-200)*10
print (Price)

num =int(input("nombre"))
while num>0:
    res=num//3
    print("The division of {} by 3 gives {}".format(num,res))
    num=int(input("enter an integer value "))
print("where done")

num = int(input("Enter"))
ndiv = 1
while ndiv<num:
    res = num// ndiv
    print("The integer division of {} by {} gives {}".format(num,ndiv,res))
    ndiv = ndiv+1
print("We're done")
print ("Total number of divisions: {}".format(ndiv))

num = int(input("Enter"))
ndiv = 0
while num>0:
    res = num// 3
    print("The integer division of {} by 3 gives {}".format(num,res))
    ndiv = ndiv+1
    print("number of divisions so far : {}".format(ndiv))
    num=int(input("enter an integer value:"))
print("We're done")
print ("Total number of divisions: {}".format(ndiv))

num = 1
ndiv = 0
while num>0 and num<211:
    if num%3==0:
        print(f"the number is {num}")
        ndiv = ndiv+1
    num=num+1
print("We're done")
print ("Total number of divisions: {}".format(ndiv))

num=1
som=0
while num<11:
    som=som+num
    num=num+1
print(som)

num=1
som=0
while num<11:
    nombr =int(input("nombre"))
    som=som+nombr
    num=num+1
print(som/10)

i=1
while i<=4:
    print ("*"*i)
    i=i+1
    
fact=int(input("nombre"))
res=1
while fact>1:
    res=fact*res
    fact=fact-1
print(res)
    
n= int(input("enter "))
for i in range (1,n+1,2):
    q_i=i**2
    print(q_i)
    
n= int(input("enter "))
som=0
for i in range (1,n+1):
    som=som+i
print(som)

n= int(input("enter"))
som=0.0
for j in range (1,n+1):
    q=((j+1)/j**2)
    som=som+q
print("the som is {: .2f}".format(som))

for i in range(1,10):
    for j in range(1,10):
        print("{}{}".format(i,j))

num = int(input("Entrer"))
for i in range (2,n):
    if num%i==0:
        print("non")
        break
print("yes")

num = int(input("Entrer"))
a=0
b=1
c=0
for i in range (1,num+1):
    c=b
    b=b+a
    a=c
    print(b)
    
list = ['test1','test2','test3','test4','test5','test6']
print(list[2])
list.append('test7')
print(list)
list.remove(list[6])
print(list)

integer = [1,2,3,4]
print(integer)
smooth=[3.14,7,-2+3j,'water',False,[1,2]]
print(smooth)
print(smooth[1:])
print(smooth [3][4])

smooth2=["hello","Hi",'7',"e"]
print(smooth2[::2])

n = int(input("Entrez "))
list1=[]
for i in range (1,n+1):
    list1.append(1/i)
print(sum(list1))

a=[1,3,5,7,11]
be=[13,17]
c=a+be
print(c)
be[0]=-1
d=[]
for e in a:
    d.append(e+1)
print (d)
d.append(b[0]+1)
d.append(b[-1]+1)
print(d)
print(d[-2:])
print(d[:-1])
print(d[1:4])

n=int(input("entrer "))
list_num=[]
for i in range (1,n+1):
    list_num.append(i**2)
print(list_num)

name=[]
note=[]
n='a'
som=0
while n!="":
    n=input("Name ")
    if n=="":
        break
    no=int(input("Note "))
    name.append(n)
    note.append(no)
for i in range (len(note)):
    som=note[i]+som
print (som/len(note))
for i in range(0,len(note)):
    print(name[i],note[i])


nombres=[]
n=input("Nombre ")
while n!="":
    nombres.append(int(n))
    n=input("Nombre ")
print(nombres)
print(sum(nombres)/len(nombres))

phr=input( "Nom " )
lister=phr.split(' ')
for i in range (len(lister)):
    print("Hi" ,lister[i])
print(len(lister))

List1=["H","C","N","O","S","Cl"]
List2=[1.008,12.011,14.007,15.999,32.065,35.453]
tot=0.
for i in range(len(List1)):
    n=int(input( "Nombre de {} ".format(List1[i])))
    tot=n*List2[i]+tot
print(tot)
    
n=int(input("degre "))
coef=[]
som=0.
for i in range (n):
    coef.append(int(input("Coef ")))
x=float(input("value X "))
for i in range (n):
    som=x**i*coef[i]+som
print(som)

def respect ():
    print ("Respect")

respect()

Capit ={
"France": "Paris",
"Italie": "Rome",
"England": "London"
        }
for i in Capit:
    print(Capit[i])
print(Capit["France"])

dict ={
  1:"Hello",
  (1,2):"Hello Hi",
  3:[1,2,3]     
       }
print(dict[(1,2)])
print(len(dict))

test=dict({1:"Geek",2:"For",3:"Geeks"})
test2=dict([(1,"Geek"),(2,"For")])

Dict2={1:"Geeks",2:"For",3:{"A":"Welcome","B":"To","C":"Geeks"}}
print(Dict2[3]["A"])
Dict2[3]["A"]=3
print(Dict2[3]["A"])
print(1 in Dict2)
del Dict2[1]
print(1 in Dict2)
print(Dict2)

cities=('Paris','Athens')
Continent='Europe'
mDic=dict.fromkeys(cities,Continent)
print(mDic)

cities2=('Paris','Athens')
country=['France','Greece']
res_dict = dict(zip(cities2, country))
print(res_dict)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
res = dict.fromkeys(employees, defaults)
print(res)
print(res["Kelly"])

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]
for k in keys:
    sample_dict.pop(k)
print(sample_dict)

#Problem1
periodictable = {"H": {"atomicnumber":1,"meltingPoint":14,"boilingPoint":20},
                  "He": {"atomicnumber":2,"meltingPoint":1,"boilingPoint":4},
                  "Li": {"atomicnumber":3,"meltingPoint":453,"boilingPoint":1603},
                  "Be": {"atomicnumber":4,"meltingPoint":1560,"boilingPoint":2742},
                  "B": {"atomicnumber":5,"meltingPoint":2349,"boilingPoint":4200},
                  "C": {"atomicnumber":6,"meltingPoint":3915,"boilingPoint":3915},
                  "N": {"atomicnumber":7,"meltingPoint":63,"boilingPoint":77},
                  "O": {"atomicnumber":8,"meltingPoint":54,"boilingPoint":90},
                  "F": {"atomicnumber":9,"meltingPoint":53,"boilingPoint":85},
                  "Ne": {"atomicnumber":10,"meltingPoint":25,"boilingPoint":27}}
value = str(input("element ? "))
temp = int(input("temperature ? "))
if temp < periodictable[value]["meltingPoint"]:
    print("solid")
elif (temp < periodictable[value]["boilingPoint"]) and (temp > periodictable[value]["meltingPoint"]):
    print("liquid")
else:
    print("gas") 

#Problem2
r=0
Bank_dict = {
    "ANZ":{"Years":2.3,"Years 3":4.1},
    "Bank of Australia":{"Years":0.1,"Years 3":5},
    "Commonwealth Bank":{"Years":3.5,"Years 3":3.8},
    "Westpac":{"Years":3.7,"Years 3":3.7}}
Name = input("Entrez le nom de la banque")
Amount = int(input("Entrez le montant du mortgage"))
Year = int(input("Entrer le nombre d'année à rembourser"))
if(a<=2):
    for i in range (1,Year):
        Amount = Amount + Amount*Bank_dict[Name]["Years"]*0.01

else:
    for i in range (1,Year):
        Amount = Amount + Amount*Bank_dict[Name]["Years"]*0.01
    for i in range (1,Year-2):
         Amount = Amount + Amount*Bank_dict[Name]["Years 3"]*0.01
print( Amount)

def MFunc(frame,lname):
    print(frame+" "+lname)
MFunc("Emil")

def MFunc2 (*kids):
    print(kids[2])
MFunc2("Emil","Tobias","Linus")

def MFunc3 (child3,child2,child1):
    print(child3)
MFunc3(child1="Emil",child2="Tobias",child3="Linus")

def MFunc4(**kid):
    print(kid["lname"])
MFunc4(fname="Tobias",lname="Refsnes")

def MFunc5(fname="test",Lname="xyz"):
    print(fname+" "+Lname)
MFunc5("Tobias")

def MFunc6(x):
    return 5*x
print(MFunc6(4))

def Big(x,y):
    if x>y:
        return x
    else:
        return y
print(Big(5,6))


def Exo1 (a,b,c,d,e):
    List= [a,b,c,d,e]
    print(max(List)," ",min(List))
Nb1=int(input("Nb1 "))
Nb2=int(input("Nb2 "))
Nb3=int(input("Nb3 "))
Nb4=int(input("Nb4 "))
Nb5=int(input("Nb5 "))
Exo1(Nb1,Nb2,Nb3,Nb4,Nb5)

def Even ():
    num=int(input("Enter a number : "))
    if (num%2)==0:
       print("{} is Even".format(num))
    else:
     print("{} is not Even".format(num))
     
try:
    Even()
except:
    print("Error")
else:
    print("ok")
finally:
    print ("finished")
    
def Test ():
   try:
      num=int(input("Enter a number : "))
   except:
    print("Wrong number")
    Test()
   else:
    if (num%2)==0:
        print("{} is Even".format(num))
    else:
        print("{} is not Even".format(num))

Test()
abc=["zbdjhbaiu","ifhzaufhio"]
print(abc[0][1])
def ET(val):
    backward_string= val[::-3]
    
    return backward_string
print(ET("test"))

def longest_prefix(arr):
    if (len(arr)>1) :
            Mont=[len(arr[0])]
            d=len(arr[0])
            for i in range(len(arr)):
                 d=0
                 b=0
                 while arr[i][b]==arr[0][b] and int(b)<len(arr[i])-1:
                     d=d+1
                     b=b+1
                 Mont.append(d)
                 print(Mont)
            return arr[0][:min(Mont)]
    else :
         return arr[0]
print(longest_prefix(["a"]))

def remove_all_before(items, border) :
    try:
        p=items.index(border) 
    except:
        return items
    else:
        return items[p:]
print(remove_all_before([1, 1, 5, 6, 7], 5))

import numpy as np
a=np.array([1,2,3],dtype='int32')
b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
print(a.ndim)
print(b.shape)
print(a.nbytes)
print(b[:, 2])

import numpy as np
arr=np.array([[1,2,3]])
r1=np.repeat(arr,5,axis=0)
print(r1)

import numpy as np
arr=np.array([[1,0,0,0,1]])
r1=np.repeat(arr,5,axis=0)
r1[2,2]=9
r1[0::4,]=1
print(r1)

import numpy as np
print(np.random.randint(-10,10,size=(4,4)))


import numpy as np
npoints=20
values=np.linspace(-2.0,2.0,npoints)
print(values)

import numpy as np
y=np.arange(10,31,1)
y[4]=1
print(y)

import numpy as np
vc=np.arange(9)
vect=np.linspace(11,31,15)
vec=np.arange(0,8,3)
print(vc)
print(vec)
print(vect)

import numpy as np
nel=int(input("data"))
lvec=[]
for i in range (nel):
    comp=input("value {}".format(i))
    lvec.append(float(comp))
vec=np.array(lvec)
print(vec)

import numpy as np
nel=int(input("data"))
vec=np.zeros(nel)
for i in range (nel):
    comp=input("value {}".format(i))
    vec[i]=float(comp)
vec=np.array(lvec)
print(vec)

import numpy
lin=input ("Enter")
smooth=lin.split ()
vec=numpy.float (smooth)
print("List {}".format(smooth))
print("Vector {}".format(vec))

import numpy
mat=numpy.zeros((4,3))

for i in range (4):
    for j in range(3):
        mat[i,j]=float(input("value {},{}".format(i,j)))
print(mat)

import numpy as np
a=np.array([[2,3],[1,2]])
b=np.array([[1,0],[3,1]])
c=np.linalg.inv(a)
g=np.linalg.inv(b)
d=np.dot(a,b)
print(d)
print(np.linalg.inv(d))
print(g@c)

import numpy as np
a=np.array([[1,1],[1,2]])
b=np.array([[4,1],[3,1]])
c=np.array([[24,7],[31,9]])
x=np.linalg.inv(a)
y=np.linalg.inv(b)
z=np.dot(x,c)
z2=np.dot(z,y)
print(z2)


import numpy as np
vect=np.linspace(1,5,21)
vect=vect*0.1
print (vect)

import numpy as np
import math as mt
x0=int(input("x0 "))
s=float(input("s "))
start=int(input("Start "))
finish=int(input("End"))
number=int(input("number"))
values=np.linspace(start,finish,number)
y=1/mt.sqrt(2*np.pi)*np.exp(-(1/2)*(values-x0)**2/s**2)
for i in range(len(y)):
    print("x={value:.2f}  y={y:.5f}".format(value=values[i],y=y[i]))

import numpy as np
temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
'November', 'December']
temp_mar_arr=np.array(temp_mar)
print("The average temperature is {}".format(np.average(temp_mar_arr)))
print("The coldest temperature was {} and it was in {}".format(np.min(temp_mar_arr),months[temp_mar.index(np.min(temp_mar_arr))]))
print("The warmest temperature was {} and it was in {}".format(np.max(temp_mar_arr),months[temp_mar.index(np.min(temp_mar_arr))]))

nb_std=int(input("Number of student "))
table=np.zeros((nb_std,4))
for i in range(nb_std):
    table[i,0]=i
    table[i,1]=float(input("Theory Grade for student {} ".format(i)))
    table[i,2]=float(input("Problem Grade for student {} ".format(i)))
    table[i,3]=table[i,1]*0.4+table[i,2]*0.6
print (table)
print("The maximum total is {} by student {}".format(np.max(table[:,-1]),table[np.where(table[:,-1]==np.max(table[:,-1])),0])) 
print("The minimum total is {}  ".format(np.min(table[:,-1])))   
print("The average total is {}  ".format(np.average(table[:,-1])))   

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-2,2,101)
y=x**2
print(x)
plt.plot(x,y)
plt.show

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,3*np.pi,500)
print(x)
plt.plot(x,np.sin(x**2))
plt.title('A simple chirp')

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f(x)")
y2= x**2
plt.plot(x,y2,'g',label="x2")
y3 =x**3
plt.plot(x,y3,'r',label="x3")
y4=x**4
plt.plot(x,y4,'b',label="x4")
plt.legend()
plt.show()

n = int(input("nb"))
x = np.linspace(-1,1,n)
y = np.cos(2*np.pi*x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y,'g',label="2pix")
plt.legend()
plt.show()
plt.savefig("cos2pix.png")

n = int(input("nb"))
x = np.linspace(-1,1,n)
y = np.cos(2*np.pi*x)
y2=np.sin(2*np.pi*x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y,'g',label="2pix")
plt.plot(x,y2,'bo',label="3pix")
plt.legend()
plt.show()
plt.savefig("cos2pix.png")

import numpy as np
while True:
    try:
        n = int(input("number: "))
        if(n>0):
            break
        print("no valid number")
            
    except ValueError:
        print("no valid number")
x = np.linspace(0,4,n)
y = np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
plt.plot(x,y,'g',label = 'fonc')
plt.legend()
plt.show()

n = int(input("nb"))
T = int(input("T"))
x = np.linspace(2,10,n)
y = 0.08206*T/x
plt.plot(x,y,'g',label = 'fonc')
plt.legend()
plt.show()

x = np.linspace(-1,1,100)
s = float(input("s"))
x0 = float(input("x0"))
y = (1/np.sqrt(2*np.pi))*np.exp((-1/2)((x-x0)*2)/(s*2))
plt.plot(x,y,'g',label = 'fonc')
plt.title("Gaus")
plt.legend()
plt.show()

import matplotlib.pyplot as plt
n = int(input("nb"))
x = np.linspace(0,3,n)
plt.xlabel("x")
plt.ylabel("f(x)")
y2= np.exp(-x)
y=np.sin(3*np.pi*x)*np.exp(-x)
plt.plot(x,y,'g',label="e-x")
plt.plot(x,y2,'bo',label="sin(3pix)e-x")
plt.legend()
plt.show()

n = int(input("How many?"))
for i in range (0,n):
    x = np.linspace(-1,1,100)
    s = float(input("s"))
    x0 = float(input("x0"))
    y = (1/np.sqrt(2*np.pi))*np.exp((-1/2)*((x-x0)**2)/(s**2))
    a = input("line : ")
    plt.plot(x,y,a,label = 'fonc')

plt.title("Gaus")
plt.legend()
plt.show()

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
a=np.arange(10,22).reshape(3,4)
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
print(z)

import numpy as np
test=np.arange(0,101)
a=float(input("nombre a chercher "))
test2=abs(test-a)
print(test2.argmin())


variable=open("jhon.txt")
for i in variable:
    if("a" in i):
       i=i.strip()
       print(i)
       
       
with open("jhon.txt","r") as f:
    f_contents=f.read()
    print(f_contents)
    
    with open("jhon.txt","w")as f:
        val='names'
        val1='10'
        val2='niamh'
        f.write(val+'\n'+val1+'\n'+val2)
        f.seek(0)
        f.write("Test")
        f.seek(6)
        f.write('z')
