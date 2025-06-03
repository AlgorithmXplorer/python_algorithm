
import numpy as np

#* Bu soruda geçen transpose  demek satır ve sütunları yer değiştirince
#* aynı matrisi elde etmek demek
#* burda aldığımız matrisdeki aynı indexli satır ve sütunları karşılaştırıcaz. aynı ise 
#* o zaman simetrik
class question:
    def __init__(self,array):
        self.array = array
    
    def solution_1(self):
        if len(self.array[0,:]) != len(self.array[:,0]):
            return False

        colon_count = len(self.array[0,:])
        

        for index in range(colon_count):
            line = self.array[index,:]
            colon = self.array[:,index]
            
            comparison = line == colon
            if False in comparison:
                return False
            """
            if not np.all(comparison):
                return False
            """
        
        else:
            return True

    def solution_2(self):
        return np.array_equal(self.array, self.array.T)

my_array = np.array([1, 2, 3, 4, 2, 5, 6, 7, 3, 6, 8, 9, 4, 7, 9, 0]).reshape(4,4)
x = question(array=my_array)

print(x.solution_2())

