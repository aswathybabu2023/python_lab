str1 = input("Enter first string ")
str2 = input("Enter the second string ")
a = str2[:1] + str1[1:]
b = str1[:1] + str2[1:]
print(a+' '+b)
