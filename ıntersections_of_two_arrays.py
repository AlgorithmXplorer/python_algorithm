
nums1 = [1,2,3,4,5]
nums2 =  [6,7,8,9,10]

#region #todo my code
def intersection_of_Two_Arrays(nums_1,nums_2):
    set_1 = set(nums_1)
    set_2 = set(nums_2)

    def inner(big_list, small_list):
        ıntersection = []
        for i in big_list:
            if i in small_list:
                ıntersection.append(i)
        return ıntersection
    if len(set_1) >= len(set_2):
        return inner(set_1,set_2)
    else:
        return inner(set_2,set_1)

print(intersection_of_Two_Arrays(nums2,nums1))
#endregion

#region #todo chatgbt's code
def intersection_of_Two_Arrays_2(nums_1, nums_2):
    return list(set(nums_1).intersection(set(nums_2)))

print(intersection_of_Two_Arrays_2(nums2,nums1))
#endregion 





