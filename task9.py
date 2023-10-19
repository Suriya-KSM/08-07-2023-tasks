def findTriplets(list, m):
    triplet_count = 0
    final_temp_list =[]
     
    for i in range(0, len(list)-1): 
         
        s = set() 
        temp_list = []
 
        # Adding first element
        temp_list.append(list[i])
 
        curr_m = m - list[i] 
         
        for j in range(i + 1, len(list)): 
             
            if (curr_m - list[j]) in s: 
                triplet_count += 1
                 
                # Adding second element
                temp_list.append(list[j])
 
                # Adding third element
                temp_list.append(curr_m - list[j])
                 
                # Appending tuple to the final list
                final_temp_list.append(tuple(temp_list))
                temp_list.pop(2)
                temp_list.pop(1)
            s.add(list[j])
             
    return final_temp_list
     
list = [10, 20, 30, 9]
m = 59
print(findTriplets(list, m))