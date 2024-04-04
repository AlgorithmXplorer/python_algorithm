
x =[1, 3, 5, 4, 2, 8, 9, 0]
def missing_number(lst):
    lst.sort()
    x = []
    for i in range(lst[0],lst[-1]):
        if i  not in lst:
            x.append(i)
    return f"listede olmayan sayılar: {x}"

            

print(missing_number(x))