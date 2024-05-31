n = 15
def fizz_buzz(num):
    rtrn_lst = []
    for i in range(1, num+1):
        if (i % 3) == 0 and (i % 5) == 0:
            rtrn_lst.append("fizzbuzz")
        elif (i % 3) == 0:
            rtrn_lst.append("fizz")
        elif (i % 5) == 0:
            rtrn_lst.append("buzz")
        else:        
            rtrn_lst.append(str(i))
    return rtrn_lst



print(fizz_buzz(n))





