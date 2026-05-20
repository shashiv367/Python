x=8
x="hello"
print(x)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Assign multiple variables to multiple values

z,y,x = "str","jkhvd","jvs"
print(x)
print(y)
print(z)

# One value to multiple variables

x=y=z = "blue"
print(x)
print(y)
print(z)

# Extraction of values
fruits = ["Apples","Mango","Banana"]
x,y,z=fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

name = "Shashi"
age = "21"

print(name)
print(age)

x = "hemz"
y=55

print(x)
print(y)

a="hello"
b=13
c=44.56
d=True
e="hey,bye,gm"
f=5+6j
g=None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

x=10
print(x==10)

a,b,c = 10,20,30

print(a,b,c)

#swapping

a=10
b=20

a,b=b,a
print(a)
print(b)

x=100
def test():
    print(x)

test()
print(x)

x=10
def test():
    y=30
    print(y)

test()
print(x)

x=122
def test1():
    y=25
    print(y)
def test2():
    print(x)
test1()
test2()

x=10
def changed():
    global x
    x=20
    print(x)

changed()
print(x)

x=5
def test():
    x=10
    print(x)
test()
print(x)

a=[1,2,3]
a.append(4)
print(a)

a=10
b=a

print(a == b)
print(a is b)