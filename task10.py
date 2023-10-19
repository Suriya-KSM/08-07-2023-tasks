def sub_list(list, l):
    for i in range(l - 1):
        s = list[i]
        for j in range(i + 1, l):
            s += list[j]
            if s == 0:
                return True
    return False


list = [4, 2, -3, 1, 6]

print(sub_list(list, len(list)))