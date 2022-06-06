numDay = int(input('enter the number of days temperature available? :'))
lst = []
t = 0
for i in range(numDay):
    Daytemp = int(input("enter day "+str(i+1)+"'s temperature :"))
    lst.append(Daytemp)
avg = round(sum(lst)/len(lst),2)
print(str(avg)+" is the average temperature of "+str(numDay)+" days")
for i in lst:
    if i > avg:
        t+=1
print(str(t)+" day(s) temperature is higher than average temperature")
