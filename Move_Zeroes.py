
#region#*My_code
import random_array_of_num
nums = random_array_of_num.random_array()

def Move_zeroes(numbers):
    for i in numbers:
        if i == 0:
            numbers.remove(i)
            numbers.append(i)

    return numbers
Move_zeroes(nums)
#endregion

#region#*Chatgbt's_code
def moveZeroes(nums):
    zero_index = 0
    
    # Sıfır olmayan elemanları öne taşı
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_index], nums[i] = nums[i], nums[zero_index]
            zero_index += 1
    
    return nums

# Örnek kullanım
nums = [0, 1, 0, 3, 12]
result = moveZeroes(nums)
print(result)

#endregion


