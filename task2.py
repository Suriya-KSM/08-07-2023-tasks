numberList = [10, 501, 22, 37, 100, 999, 87, 351]
 
ansList = []
 

for num in numberList :
     

    if num == 0 or num == 1 :
        continue
         
    for i in range(2, num // 2 + 1) :
 

        if num % i == 0 :
            break

    else :

        ansList.append(num)

if len(ansList) :
     
    print("Prime Numbers in the given list : ",end = " ")

    for ans in ansList :
        print(ans, end = " ")
else :
    print("No any number from the given list is Prime")

counter = 0

for i in ansList:
    counter = counter + 1

print ('\n', "Total count fo prime number is : " + str(counter))
