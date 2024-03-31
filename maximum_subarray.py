
#region#*My Codes
nums = [5, -3, 7, -8, 2, 1, -9, 10]
x = [-1, -2, -3, -4, -5]
def lists(num,arrays):
    first_int ,last_int,params,x= 0, num,[],len(arrays)+1
    while last_int <= x :
        little_list = arrays[first_int : last_int]
        params.append(sum(little_list))
        first_int +=1
        last_int +=1
    params.append(sum(arrays))
    return max(params)
        
def consecutive(arrays):
    if max(arrays) == -1:
        return [-1]
    x = len(arrays)
    a = []
    for i in range(x):
        a.append(lists(i,arrays))
    return max(a)

print(consecutive(x))
print(consecutive(nums))
#endregion

#region#*Chatgbt`s codes
def maxSubArray(nums):
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Örnek kullanım
nums = [5, -3, 7, -8, 2, 1, -9, 10]
result = maxSubArray(nums)
print(result)

#endregion
