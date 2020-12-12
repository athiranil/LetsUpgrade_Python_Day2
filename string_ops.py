a = input("Enter a string")
print("Swapcase::",a.swapcase())
print("Isalpha::",a.isalpha())
print("upper case::",a.upper())
n=len(a)-1
print("Find '"+a[n]+"' ::",a.find(a[n]))
print("Count '"+a[n]+"' ::",a.count(a[n]))
print("replace '"+a[n]+"' with 'b'::",a.replace(a[n], "'b'"))
