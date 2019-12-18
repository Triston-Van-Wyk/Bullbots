def my_function(number):
    return number
x = my_function(1)
def is_odd(num):
    return num%2 == 1
print(is_odd(int(input("chose number to see if it is odd:"))))
def is_even(numb):
    return not is_odd(numb)
print(is_even(int(input("chose number to see if it is even:"))))