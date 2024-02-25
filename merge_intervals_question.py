dizi = [[1,3],[2,6],[8,10],[15,18]]

def dizi_birlestiren(liste):
    array_lenght = len(liste)
    x = 0
    new_array = []
    while x < array_lenght:
        a = []

        x +=1
        print(liste[x])
        if x == array_lenght-1:
            break
        else:
            if liste[x-1][1] < liste[x][0]:    
                new_array.append(liste[x])
            
            elif liste[x-1][1] >= liste[x][0]:
                if liste[x-1][0] <= liste[x][0]:
                    a.append(liste[x-1][0])
                    if liste[x-1][1] <= liste[x][1]:
                        a.append(liste[x][1])
                    elif liste[x-1][1] >= liste[x][1]:
                        a.append(liste[x-1][1])

                if liste[x-1][0] >= liste[x][0]:
                    a.append(liste[x][0])
                    if liste[x-1][1] <= liste[x][1]:
                        a.append(liste[x][1])
                    elif liste[x-1][1] >= liste[x][1]:
                        a.append(liste[x-1][1])

        new_array.append(a)
    return new_array    
                

print(dizi_birlestiren(dizi))

#*                                                 [4,15] [9,17]

