


nums = [88, 76, 97]
def main(array):
    def inner(numbers:list,slice_num:int):
        Ability_to_divide = [[],[]]
        for i in numbers:
            if i/slice_num > i//slice_num:
                Ability_to_divide[0].append(False)
                Ability_to_divide[1].append(i)
            else:
                Ability_to_divide[0].append(True)
                Ability_to_divide[1].append(i/slice_num)
        return Ability_to_divide
    
    Prime_numbers = [2,3,5,7]
    smallest_common_multiple = [] 
    def inner1(index:int,arrays:list):
        print(arrays[1])
        if index == len(Prime_numbers):
            return [arrays[1],smallest_common_multiple]
        else:
            prime_num = Prime_numbers[index]
            new_list = inner(arrays[1],prime_num)

            if new_list[0].count(True) >=1:
                smallest_common_multiple.append(prime_num)
                return inner1(index , inner(arrays[1],prime_num))
            
            else:
                return inner1(index+1, inner(arrays[1],prime_num))
                
    lists = inner1(0,inner(array,1))
    last_list = list(set(lists[0])) + lists[1]
    result = 1
    for i in last_list:
        result*=i


main([131, 6])

#region#todo chatgbt's code
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def find_lcm_of_list(nums):
    result = nums[0]
    for num in nums[1:]:
        result = lcm(result, num)
    return result


nums = [50, 75, 100]
result = find_lcm_of_list(nums)
print("LCM:", result)


#endregion
