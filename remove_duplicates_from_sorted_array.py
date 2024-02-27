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



