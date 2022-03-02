rect=lambda x,y:x*y
sqr=lambda m:m*m
tri=lambda b,h:0.5*b*h
i=int(input("enter the length of the rect: "))
j=int(input("enter the breadth of the rect: "))
k=int(input("enter the length of the square: "))
i1=int(input("enter the height of the triangle: "))
j1=int(input("enter the height of the triangle: "))
print("area of rectangle",rect(i,j))
print("area of square: ",sqr(k))
print("area of triangle",tri(i1,j1))
