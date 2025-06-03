
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


class question:
    def __init__(self,array, static_value:int):
        self.array = array
        self.static_value = static_value
    
    def solution_1(self):
        if len(self.array) < self.static_value:
            return f"there is a problem about static value {self.static_value}"
        
        means = []

        loop_count = (len(self.array) - self.static_value) + 1
        #* the plus one is for the last three element in the array 

        for i in range(loop_count):
            #* slicng
            operation_array = self.array[i : i+self.static_value ]
            
            means.append( float(operation_array.mean()) )
        
        return means
    
    def solution_2(self):
        if len(self.array) < self.static_value:
            return f"Array must have at least {self.static_value} elements"

        # pencere görünümü (örneğin: (8,) -> (6,3) olur eğer static_value=3)
        windows = sliding_window_view(self.array, window_shape=self.static_value)
        
        # her pencerenin ortalamasını al
        means = windows.mean(axis=1)

        return means.tolist()  # liste olarak döndürmek için
    

my_array = np.array([1, 1, 2, 2, 3, 3, 4, 4])
static_value = 2

x = question(array= my_array, static_value = static_value )

result = x.solution_1()
print(result)
