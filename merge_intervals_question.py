dizi = [[4,15], [9,17]]

def dizi_birlestiren(liste):
    # acilmis_array = []
    # for array in liste:
    #     x = []
    #     for i in range( array[0] , ( array[-1] + 1 )):
    #         x.append(i)
    #     acilmis_array.append(x)
    array_lenght = len(liste)
    x = 0
    new_array = []
    while x < array_lenght:
        a = []
        if x == array_lenght-1:
            break
        else:
            if liste[x][0] <= liste[x+1][1]:
                a.append(liste[x][0])

                if liste[x][1] >= liste[x+1][0] and liste[x][1] <= liste[x+1][1]:
                    a.append(liste[x+1][1])
        new_array.append(a)
        x +=1
    return new_array    
print(dizi_birlestiren(dizi))

#*                                                 [4,15] [9,17]

