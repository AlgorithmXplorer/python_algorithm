
indices = [4,5,6,7,0,2,1,3]
s = "codeleet"
def Shuffle_string(index_list , str_word):
    result , lenght_list= "",len(index_list)
    str_word = list(str_word)
    for i in range(lenght_list):
        index = index_list.index(i)
        result += str_word[index]
    return result
    

Shuffle_string(indices,s)

#* Chatgbt ' s code
def shuffle_string(index_list, str_word):
    result = [''] * len(index_list)  # Sonucu saklamak için bir liste oluştur
    for i, char in zip(index_list, str_word):  # Her bir indeks ve karakter için döngü
        result[i] = char  # Doğru indekse doğru karakteri yerleştir
    return ''.join(result)  # Sonucu birleştirerek döndür


