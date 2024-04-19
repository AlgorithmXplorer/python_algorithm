
nums = [1,3,2,4,5,9,2,5,7,3]
def Shuffle_the_array(lst):
    index = int(input("index: "))
    list_1 = lst[:index]
    list_2 = lst[index:]
    print(list_1,list_2)
    x = len(list_2) >= len(list_1)
    list_1yedek = list_1[::]
    list_2yedek = list_2[::]
    if x:
        for index,num in enumerate(list_1):
            list_1yedek.insert(list_1yedek.index(num)+1 , list_2[index])
        # listee = list_2[len(list_1):] 
        # list_1yedek += listee
        print(list_1yedek)




2,1,5,3,7,2,3,46

Shuffle_the_array(nums)