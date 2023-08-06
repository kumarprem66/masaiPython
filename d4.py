def anagram(s1,s2):
    my_map = {}
    for i in s1:
        is_avail = my_map.get(i,0)
        if is_avail == 0:
            my_map[i] = my_map.get(i,1)
        else:
            my_map[i] = my_map.get(i)+1

    for i in s2:
        is_avail = my_map.get(i,0)
        if is_avail == 0:
           return False
        else:
            my_map[i] = my_map.get(i)-1

    for i in my_map:
        if my_map.get(i) != 0:
            return False
    return True


def bubbleSort(li):
    for i in range(len(li)):
        for j in range(len(li)-1):
            if li[j]>li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp



arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)

print(arr)

