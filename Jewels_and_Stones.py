
jewels = "aA"
stones = "aAAbbbb"

def Jewels_and_Stones(mücevher,taslar):
    mücevher = list(mücevher)
    result = 0
    for i in taslar:
        if i in mücevher:
            result +=1
    return result

print(Jewels_and_Stones(jewels,stones))


