
#region #todo my code
def main(arrays):
    return max(arrays,key=arrays.count)

x = [2, 2, 1, 1, 1, 2, 2]
print(main(x))

#endregion

#region #todo chatgbt's code
def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
print(majorityElement(x))

#endregion


