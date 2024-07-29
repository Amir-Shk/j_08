#get range from user
a = int(input("start of the range :"))
b = int(input("end of the range :"))
c = []


#number divisible by 15
for i in range (a , b) :
    if i % 15 == 0:
        c.append(i)
        
print(c)