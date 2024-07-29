#Create 2 empty list
l1 = []
l2 = []


#Separation of couples and individuals
for i in range (1,101):
    if i % 2 == 0:
        l1.append(i)
    elif i % 2 != 0:
        l2.append(i)        
        
        
#Result
print("even numbers" , l1)
print("odd numbers" , l2)