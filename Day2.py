#Question 1
a = input("Enter a string")
print("Swapcase::",a.swapcase())
print("Isalpha::",a.isalpha())
print("upper case::",a.upper())
n=len(a)-1
print("Find '"+a[n]+"' ::",a.find(a[n]))
print("Count '"+a[n]+"' ::",a.count(a[n]))
print("replace '"+a[n]+"' with 'b'::",a.replace(a[n], "'b'"))


#Question2
lst=[10,20,30,5,20]
print("List elements::",lst)
lst.append(1)
print("Append 1 to list::",lst)
lst.sort()
print("Sorted list::",lst)
lst.reverse()
print("Reverse List::",lst)
lst.pop(3)
print("Pop 3rd element from list",lst)
print("Count of 20 in list::",lst.count(20))
lst.clear()
print("List.clear()::",lst)

#Question3
dic={"key1":"value1","key2":"value2","key3":"value3"}
print("Dictionary::",dic)
dic.update({"key4":"value4"})
print("Update::",dic)
print("Items::",dic.items())
print("Keys::",dic.keys())
print("Values",dic.values())
print("Get key1::",dic.get("key1"));
print("Pop key2::",dic.pop("key2"))
print(dic)
