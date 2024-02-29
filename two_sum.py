nums = [2,7,11,15]
target = 9
def two_sum(arrays):
    target_list = []
    for i in arrays:
        x,y = 0,True
        while y:
            if i + arrays[x] == target:
                target_list.append([i,arrays[x]])
            if x == len(arrays)-1:
                y = False
            x +=1
    print(target_list)

two_sum(nums)
