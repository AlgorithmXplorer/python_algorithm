x = 2020
pos_or_neg = lambda num: num > 0
def reverse_int(num):
    positive = pos_or_neg(num)
    num,result = list(str(num)),""
    num = num[::-1]
    if positive  == 0:
        num.remove("-")
    num_1 = num[:]
    for x in num_1:
        if x == "0":
            num.pop(0)
        else:
            break
    for i in num:
        result+=i
    if positive is False:
        result = "-" +result
    return result
   
print(reverse_int(x))

#* Improved code from chatgbt
def reverse_int(num):
    # Sayının işaretini kontrol et
    is_positive = num > 0
    # Sayıyı mutlak değere çevir
    num = abs(num)
    # Sayıyı dizeye dönüştür ve tersine çevir
    num_str = str(num)[::-1]
    # Tersine çevrilen sayıda önemli sıfırları kaldır
    num_str = num_str.lstrip("0")
    # Negatif sayıyı tekrar ekle
    if not is_positive:
        num_str = "-" + num_str
    # Sonucu döndür
    return int(num_str)

# Örnek kullanım
x = -2020
print(reverse_int(x))





