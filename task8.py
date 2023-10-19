
def MinElement(list1):
   min = list1[0]
   for i in list1:
      if i < min :
         min = i
   return min

list1 = [100, 1, 5, 80, 20]
list1.sort()
print("Minimum element fof the sorted list is ", MinElement(list1))