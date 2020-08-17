"""Complete the function called is_either_even_and_less_than_9.

is_either_even_and_less_than_9 takes two numbers as parameters. It returns True if either one of the parameters is even AND both of them are less than 9. It will return false if both conditions are not met.

output = is_either_even_and_less_than_9(2, 4)
print(output) # --> True

output = is_either_even_and_less_than_9(72, 2)
print(output) # --> False

"""
def is_either_even_and_less_than_9(num1, num2):
  if ((num1%2==0 or num2%2==0) and ((num1<9) and (num2<9))):
    return True
  else:
    return False

output=is_either_even_and_less_than_9(72,60)
print(output)