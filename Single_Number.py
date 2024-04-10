import random_array_of_num
nums = random_array_of_num.random_array()
def Single_Num(arrays):
    single_nums = []
    for i in arrays:
        if arrays.count(i) == 1:
            single_nums.append(i)
    return single_nums



print(f"list: {nums}\nsingle numbers: {Single_Num(nums)}")
