
#region #todo my way
def main(s,t):
    def inner(my_str):
        copy_str = set(my_str)
        count = {}
        for i in copy_str:
            count.update({i:my_str.count(i)})
        return count
    return inner(s) == inner(t)

print(main("nagaram","anagram"))  
#endregion

#region #todo chatgbt's way
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

print(isAnagram("nagaram","anagram"))  

#endregion



