print ("hello zaryab")
print ("this is the first program")

a = [1,2,3,4,'a','b','c']
print(a)
a[2] = 'modified'
print(a[2])
print(a[2:6])
print(a[1:])

#tuple

t = (1,2,6,'tuple')
print(t)
print(t[2])


""" string examples """
str = 'this is a String'
print(str)
print(str[2])

""" set example"""
a = {1,2,3,4,5,5,5,5}
print(a)


""" dictionary test"""

d = {1:'a',2:'b',3:'c'}
print(d[1], d[2])

""" data conversion in python"""

a = 10.3
b = 8
c = float(b)
print(c)

#implecit type conversion

a = 10.2
b = 2

c = a+b
print(c)

"""input and output in python"""

num = input('inter a number')

print(num)

""" Sorting method """

def myFunc(e):
    return e['year']

cars = [{'car':'BMW', 'year':2009}, {'car':'AUDI', 'year':2006}]
cars.sort(key=myFunc)

""" if elif example """
num = input("enter a number")
if num > 0:
    print('number is positive')
elif num == 0:
    print('number is zero')
else:
    print('number is negative')
