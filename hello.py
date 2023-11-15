"""input("What is your name? :")
print("hello, World")
print("meow\n" * 3, end= "")
def main():
    print_column(3)



def print_column(height):
    for _ in range(height):
        print("#" * 3)


main()
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()"""
#user_input = input("name: ")
"""for i, u in enumerate(user_input):
    if u.isupper():
            user_input[i] += "_" + u.lower()
            # output = user_input[:i] + "_" + u.lower()
    else:
        output += u
    print(output)"""

'''output = ""
for i in user_input:
    if i.isupper():
        output = output +  "_" + i.lower()
    else:
        output = output + i
print(output)'''

'''original_string = "apple, banana, cherry, date, apple"
substitutions = {'a': 'x', 'e': 'z'}

modified_string = original_string
for old, new in substitutions.items():
    modified_string = modified_string.replace(old, new)

print("Original String:", original_string)
print("Modified String:", modified_string)'''

#p = "AA122"
"""for i, v in enumerate(p):
    print(v)"""
#print(p[0])

"""def is_first_numeric_digit_zero(s):
    if s and s[0].isalpha():
        rest_of_string = s[1:]
        if rest_of_string.isdigit() and rest_of_string[0] == '0':
            return True
    return False

# Test the function with "cs05"
test_string = "cs500"
result = is_first_numeric_digit_zero(test_string)

print(f"{test_string}: {result}")"""
'''def first_num_zero(s):
    if s.isalnum():
        r = s[2:]
        if r[0] == 0:
            t = True
        else:
            t = False
    return t
test_string = "ca500"
result = first_num_zero(test_string)
print(f"{test_string}: {result}")'''

x = "J02"
def not_starting_zero(m):
    for char in m:
        if char.isdigit() == True:
            if char == "0":
                return True
            # otherwise, return False
            return False

    # if we get here, there weren't any numbers
    return False
print(f"{test_string}: {result}")
