from random import choice
from random import randrange

# -- LISTS OF CHARS, LETTERS AND NUMBERS

# LOWERCASE LETTERS
a_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'u', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z'
]

# UPPERCASE LETTERS
A_letters = [x.upper() for x in a_letters]

# NUMBERS
numbers = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '0'
]

# CHARS AND SIGNS
chars = [
    '@', '#', '$', '%',
    '&', '*', '_', '-',
    '=', '<', '>', '?'
]


# -- RANDOM STRONG PASSWORD GENERATOR FUNCTION
def random_password(length=5):
    password = ''
    char_list = []

    for i in range(0, length):
        # APPEND RANDOM VALUE FROM BEFORE DECLARED LISTS TO THE MAIN LIST
        char_list.append(choice(a_letters))
        char_list.append(choice(A_letters))
        char_list.append(choice(numbers))
        char_list.append(choice(chars))

        # INSERT RANDOM VALUE FROM THE MAIN ARRAY TO THE CHAIN "PASSWORD"
        password = password + char_list[randrange(0, 4)]

        char_list.clear()

    return password


print("Your generated password is:    {}".format(random_password(10)))
