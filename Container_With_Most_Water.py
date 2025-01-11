height =[10, 14, 10, 4, 10, 14, 10]

def main(array):
    def slicing(param):       
        slice_list = []
        value_list =[]
        for index,num in enumerate(param,1):
            for indx,number in enumerate(param,1):
                lst = [num,number]
                slice_list.append(lst)
                value = abs(index-indx) * min(lst)
                value_list.append(value)


        return [slice_list,value_list]
    dual_list = slicing(array)
    return max(dual_list[1])    



    

            



