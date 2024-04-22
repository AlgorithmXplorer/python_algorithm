import random_array_of_num
nums = random_array_of_num.random_array()

def Move_zeroes(numbers):
    for i in numbers:
        if i == 0:
            numbers.remove(i)
            numbers.append(i)

    return numbers
Move_zeroes(nums)