x = -2020
po_ne = lambda num: num > 0
def reverse_int(num):
    positive = po_ne(num)
    num,a = str(num),""
    num = list(num)
    num.reverse()
    num.remove("-")
    num_1 = num[:]
    for x in num_1:
        if x == "0":
            num.pop(0)
        else:
            break
    for i in num:
        a+=i
    a = int(a)
    if positive is False:
        a *=-1
        
    return a
        
   
print(reverse_int(x))





