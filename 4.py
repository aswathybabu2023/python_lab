n=int(input("ENTER NUMBER OF ELEMENTS:"))
print("ENTER ELEMENTS:")
list=[]
res=[]
for i in range (0,n):
      ele=int(input())
      list.append(ele)
print(list)
for i in list:
    if i>100:
        res.append('over')
    else:
        res.append(i)
print(res)
