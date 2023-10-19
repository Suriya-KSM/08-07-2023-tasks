def NonRepeating(lis, n):
 
    for i in range(n):
        j = 0

        while(j < n):
            if (i != j and lis[i] == lis[j]):
                break
            j += 1

        if (j == n):
            return lis[i]
 
    return -1
 
lis = [1, 4, 5, 3, 4, 1, 3]
n = len(lis)
print("The first non repeating element is:",NonRepeating(lis, n))