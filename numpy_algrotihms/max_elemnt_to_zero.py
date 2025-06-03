import numpy as np

#* elimize gelen matrisin her satırını teker teker kontrol edicez
#* bunun için matrisin satır sayısı kadar bir döngü ile her satıra ulaşılır ve satırın verisi değişir ve matrise atanır
#* dizilerin max value nun index numarası alınabilidğiğ için max value indexine 0 atanır
class question:
    def __init__(self,matris):
        self.matris = matris

    def solution_1(self):

        line_count = len(self.matris)

        for i in range(line_count):
            line = self.matris[i,:]

            max_value_elemnt = line.argmax()

            self.matris[i,max_value_elemnt] = 0

        return self.matris

    def solution_2(self):

        line_count = len(self.matris)
        max_values = self.matris.argmax(axis=1)

        for i in range(line_count):
            self.matris[i,max_values[i]] = 0

        return self.matris


my_param = np.array([3,5,1,7,2,4]).reshape(2,3)

x =question(matris=my_param)
# print(x.solution_1())
print(x.solution_2())

