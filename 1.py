####---------------
#   decleration
x = 55
if(x%2==0):
    print("Even")
else:
    print("Odd")
    
print(10+2)

x = 2
x = "Bangladesh"

x = y = z = 12

x,y=10,12

#x = 10,y = 12 //WRONG in python
x = 10;y = 12

x,y = 10,12
x,y = y,x+6
print(x,y,"Hello",sep='\t',end='')

###---------------
#  INPUT
#s = input()
#s = input("Enter a string")
#s = int(input())
#s = eval(input())

##-------------
#  operators
print(10+2)
print(10-2)
print(10*2)
print(10**2)
print()

print("Divission: ")
print(10/3)
print(10//3)
print(10//3.0)
print(10.0//3)
print(10.0//3.0)
print()

print("Modulus: ")
print(10%3)
print(10%-3)
print(-10%3)
print(-10%-3)
print(divmod(10,3))
x,y=divmod(1,3)
print(x,y)

##------------------
# control statement
x = 10
if x==10:
    print('If works!!!')

if x<10:
    print('Below 10')
else:
    print('above 10.')
    
a,b,c=15,10,22
if(a>b>c):
    print("a is greater")
elif b>a>c:
    print("b is greater")
elif c>a>b:
    print("c is greater")
else:
    print("a,b,c are equal")
    
    
a,b,c=2,3,4
if a>b:
    if a>c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")


##---------------
#  Loop      
print("Simple while loop: ")
x = 0
while x<5:
    print("NEUB")
    x = x+1
print('\n')

print("another simple while: ")
flag,a = True,5
while flag:
    if a>10:
        flag = False
    print(a,"   ",end='')
    a = a+1

print('\n')
print("Nested while loop:")
x = 0
while x<5:
    y = 0
    while y<25:
        print("* ",end='')
        y = y+1
    x = x+1
    print()
    
print("Simple for loop 1:")
num = [5,7,13,6,19]
for x in num:
    print(x,"    ",end='')
print()

for x in range(5):
    print(x,"   ",end='')
print()

for x in range(2,5):
    print(x,"   ",end='')
print()

for x in range(2,10,2):
    print(x,"   ",end='')
print()

for x in range(5,0,-1):
    print(x,"   ",end='')
print()

##-------------
#  Function
def sum(a,b):
    x = a+b
    return x
a,b=2,3
ans = sum(a,b)
print(ans)

s = sum
ans = s(a,b)
print(ans)

def sub(a=0,b=0):
    return a-b
ans = sub(b=4)
print(ans)

f = lambda x,y,z: x +3
ans = f(2,3,1)
print(ans)

import matplotlib.pyplot as plt
x,y = [34,200,302,400],[2002,30,4000,450]
plt.plot(x,y)


## --------------
#   List


a = [1,2,3,4,5]
b = [1,"hh",'aaa',12]
c = [1,2,[2,3,4],67]
d = [[2,3,4],[4,5,6]]

print(a[0])
print(a)
print(c)
print(c[0])
print(c[2])
print(c[2][1])
print(d)

e = [[[1,2,3],[2,2],2,4]]
print(e[0][0][0])

print(a[1:3])
print(a[1:4:2])

a[0] = 5
c[2] = 0
c[1] = [1,2,"jfhf"]
#c[4] = 343255 out of range
print(c)

del a[0]
a = [] #all delete list data
del a #delete from memory

a = [1,2,3]
a.append([[10,2],23])
print(a)
a.extend([[10,20],3])
print(a)
a = [1,2,3]
a = a+[2,[2,3]]
print(a)
print(a*3)
print(a)
a = a*3
print(a)


a= [2,3]
x,y=a
print(x,y)
a= [2,3,4]
x,y,z=a
print(x,y,z)

##-----------------
#   string
s1 = 'First String'
s2 = "Second String"
s3 = '''Third String'''
s4 = """Fourth String"""
print(s1,s2,s3,s4,sep='\t')

s5 = "{} is {} ".format("Python","Elegent")
s6 = "{1} is {0}".format("Python","Elegent")
print(s5,s6,sep='\t')

s7 = r"A\nB"
print(s7)
s8 = "\u099C\u09BE\u09AB\u09B0\u09C1\u09B2"
print(s8)

##--------------------------------
# Tuple:
t = 1,2,3
t2 = (1,2,3)
t3 = ()
t4 = ('hello',)

print(t)
print(t2)
print(t3)
print(t4)

for g,h in enumerate(t):
    print(g,h)

t5 = t,(4,5,6)
t6 = ([1,2,3],[4,5,6])
print(t5)
print(t6)

t6[0][1] = 10000
print(t6)

##----------------------
##  Set
x = set()
y = {'a','b'}
z = {'bangladesh'}
print(x)
print(y)
print(z)

##-----------
#Dictionary
print("ahfey7ruyfurye74")
d1 = {}
d2 = {'one':'1','two':'2'}
print(d2)
d2['three'] = '3'
d2['two'] = '22'
print(d1)
print(d2)
print(d2['three'])


print(d2.keys())
print(d2.values())
print(d2.items())
del d2['two']
print(d2.items())
d2.clear()##all element delete
print(d2)
del d2 ##delete from memory

##-------------------------
# List comprehension
zz = [x for x in range(5) if x%2==0]
print(zz)

f = []
for x in range(5):
    if(x%2==0):
        f.append(x)

s = {x**2 for x in range(5)}
print(s)

d = {x:x**3 for x in range(5)}
print(d)

zv = [0 for x in range(5)]
print("YES" ,zv)


##------------------------------
##  Enumerate
g = [1,2,3,4,5]
for index,data in enumerate(g):
    print(index,data,end="\n")
    
##------------------------------------
# Enumerate
print()
print()

h = [1,2,3]
i = [4,5,6]
r = zip(h,i)

for x,y in zip(h,i):
    print(x, y)

z = set('abcda')
print(z)

a = 10;y = 20
a = a+y
