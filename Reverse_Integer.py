x = 1230000
def reverse_int(num):
    num,a = str(num),""
    num = list(num)
    num.reverse()
    num_1 = num[:]
    for x in num_1:
        if x == "0":
            num.pop(0)
        else:
            break
    for i in num:
        a+=i
    return int(a)
        
    
    
            
        

    
        
print(reverse_int(x))





