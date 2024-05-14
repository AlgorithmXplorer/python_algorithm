
candies = [2,3,5,1,3]
extra_candys = 3
def candy_questions(arrays,extra_candy):
    result = []
    max_candy = max(arrays) 
    for i in arrays:
        if (i + extra_candy) >= max_candy:
            result.append(True)
        else:
            result.append(False)
    return result
            

