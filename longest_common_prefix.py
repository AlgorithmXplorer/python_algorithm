arrays = ["dog","racecar","car"]
#* bu soruda tek bir tane liste elamanını alman yeterli olur.
#*sebebi ise 2 elemalı bir listede hepsinin ortak elemanı olmalı.
#*ikisinde olup birtanesinde olmazsa sayılmaz
def longest_common_prefix(params):
    min_letters = list(map(lambda strings: len(strings) , params ))
    index = min_letters.index(min(min_letters))
    main_letters= params[index]
    params.remove(main_letters)
    params.insert(0,main_letters)
    #* yukarıdaki kısımda listede bulunan en kısa kelime alındı. çünkü en kısa kelime alınmmazsa ortak harfler aranırken döngü bozuluyor
    #* ayrıca en kısa kelimeyi listenin en başına ekledik
    common_letters = [] #*ortak veriler
    
    for  i in params[1:]:#* en kısa kelime sonrasında bulunan kelimeler dolaşılıyor
    
        for index,letter in enumerate(main_letters): #* ana kelimenin harfleri ve indexleri alınıyor. indexler diğer kelimedeki harfler ile karşılaştırabilmek için
            if i[index] ==  letter: #* eğerki ana kelimedeki harf diğerkelimedeki aynı indexde bulunan harfle aynı olursa o zaman common_letters listesine ekleniyor
                common_letters.append(letter)
            else:
                break

    common_letters_1 = list(filter( lambda harf :common_letters.count(harf) >1, common_letters )) #* burdaki listede tüm kelimelrde olmayıp bazı kelimeler arasında olan harfleri siliyoruz
    x = []
    for i in common_letters_1:
        if x.count(i) == 0:
            x.append(i)
        elif x.count(i) > 1 :
            break
    if len(x) >0:
        letters = ""
        for i in x:
            letters += i
        return letters
    else: 
        return [""]

    # print(common_letters)
 
print(longest_common_prefix(arrays[::]))
