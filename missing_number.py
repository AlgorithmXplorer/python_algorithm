from random_array_of_num import *
x = random_array()
def missing_number(lst):
    lst.sort()
    x = []
    for i in range(lst[0],lst[-1]):
        if i  not in lst:
            x.append(i)
    return f"listede olmayan sayılar: {x}"

            

print(missing_number(x))