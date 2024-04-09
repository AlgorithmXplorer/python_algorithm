import random
def random_array():
    first_num,last_num,step = int(input("liste için ilk sayı: ")),int(input("son sayı: ")), int(input("adım sayısı: "))
    array = list(range(first_num,last_num,step))
    adet = int(input("kaç adet sayı olsun: "))
    return random.sample(array,adet)
