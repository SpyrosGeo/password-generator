
### password generator
import random
import string
letters_of_password = int(input('Enter Number of letters of password: \n'))
numbers_of_password = int(input('enter Number of numbers of password: \n'))

num_list = ''.join(random.choice(string.digits)
                   for i in range(numbers_of_password))
letter_list = ''.join(random.choice(string.ascii_letters)
                    for i in range(letters_of_password))
syntax_list = num_list + letter_list + '!@#'
if len(syntax_list) < 6:
    print('Password should be minimum 6 characters')
    exit()
result = random.sample(syntax_list, len(syntax_list))
password = ''.join((result))
print('Your password is {}'.format(password))
