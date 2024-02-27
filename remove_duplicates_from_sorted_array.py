nums = [22,33,44,55,55,55,22]
#region#*1.yol

def tekrar_edilen_ayiran(arrays):
    tek = []
    çift = set([])
    for i in arrays:
        if arrays.count(i) ==1:
            tek.append(i)
        else:
            çift.add(i)
    tek += list(çift)
    return tek
print(f"{tekrar_edilen_ayiran(nums[:])}\n {50*'*'}  ")

#endregion

#region#*2.yol
def else_way(arrays):
    arrays = set(arrays)
    arrays = list(arrays)
    arrays.sort()
    return arrays

print(f"{else_way(nums[:])}\n {50*'*'}  ")

#endregion

#region#*3.yol
def third_way(arrays):
    x = lambda nums: set(nums)
    return x(arrays)

print(f"{third_way(nums[:])}\n {50*'*'}  ")
#endregion

#region#*4.yol
def fourth_way(params):
    x = lambda nums: [i  for i in nums if i not in nums]
    return x(params)
nums_2 = [20,20,14,11,23,14,23,11,56,22,56,77]
print(f"{third_way(nums_2[:])}\n {50*'*'}  ")

#endregion



