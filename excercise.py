def extendList(val, list=[1]):
         list.append(val)
         return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')
list4 = extendList('bbb')
	
print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)
print ("list4 = %s" % list4)

name = "John"
print("Hello, %s!" % name)