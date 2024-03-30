
def palindrome_num(num):
    is_it_palindrome = str(num) == str(num)[::-1]
    if is_it_palindrome:
        print("the number is palindrome")
    else:
        print("the number is not palindrome")
        
num_1 = int(input("number: "))
palindrome_num(num_1)
