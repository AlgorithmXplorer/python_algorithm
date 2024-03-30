nums = [3, 9, 2, 4, 7]
target = 11
def two_sum(arrays):
    target_list = []
    for i in arrays:
        x,y = 0,True
        while y:
            if i + arrays[x] == target:
                params = [i,arrays[x]]
                params.sort()
                target_list.append(params)
            if x == len(arrays)-1:
                y = False
            x +=1
    for index,params in enumerate(target_list):
        if target_list.count(params) > 1:
            target_list.pop(index)
    print(target_list)
        


two_sum(nums)
