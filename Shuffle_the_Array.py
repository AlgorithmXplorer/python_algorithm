
nums = [1,3,2,4,5,9,2,5,7,3]
def Shuffle_the_array(lst,index):
    list_1 = lst[:index]
    list_2 = lst[index:]
    x = len(list_2) >= len(list_1)
    last_list = []
    if x:
        for index,nums in enumerate(list_1):
            last_list.append(nums)
            last_list.append(list_2[index])
        x = list_2[len(list_1):]
        last_list += x

    else:
        for index,nums in enumerate(list_2):
            last_list.append(list_1[index])
            last_list.append(nums)
        x = list_1[len(list_2):]
        last_list += x
    return last_list

print(Shuffle_the_array(nums,3))
