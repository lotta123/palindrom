def reverse_integer(input_integer):
    reversed_integer = reversed(str(input_integer))

    reversed_list = []
    for x in reversed_integer:
        reversed_list.append(x)
    return int( ''.join(reversed_list))


def is_it_a_palindrome(number):
    if reverse_integer(number) == number:
        print(number, "It's a palindrome")
        return True
    else:
        print(number, "It's not a palindrome")
        return False

if not is_it_a_palindrome():





#if str(input_integer) == ''.join(reversed_list):
 #   print('this is already a palindrome', input_integer)
  #  else:
   #     input_integer +






def main():
    z = is_it_a_palindrome(455)
    print(z)






# if a == b:
#    print(a)
#else:
#    if a+ int(b) == reversed(str(a+ int(b))):
 #       print(a + int(b))
  #  else:




if __name__ == '__main__':
    main()

