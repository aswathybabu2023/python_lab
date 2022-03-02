start=int(input("Enter start year: "))
end=int(input("Enter end year: "))
print("leap years are: ")
for year in range(start,end):
    if(year % 4 ==0) and (year % 100!=0) or (year % 400 ==0):
        print(year)