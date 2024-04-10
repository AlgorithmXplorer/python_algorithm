import random_array_of_num
nums = random_array_of_num.random_array()
def Single_Num(arrays):
    single_nums = []
    not_single_nums = []
    for i in arrays:
        if arrays.count(i) == 1:
            single_nums.append(i)
        else:
            not_single_nums.append(i)

    print(single_nums)
    print(not_single_nums)

print(nums)
Single_Num(nums)