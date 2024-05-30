from multiprocessing import connection


def function_change(setting_change, letter_passed):
    if letter_passed == setting_change[0]:
        letter_passed = setting_change[1]
    elif letter_passed == setting_change[1]:
        letter_passed = setting_change[0]
    return letter_passed

def enter_settings(numcon):

    for j in range(numcon):
        print("For connection", j+1)
        print("Enter first capital letter:")
        letter = input()
        connection_array[j][0] = letter
        print("Enter second capital letter:")
        letter = input()
        if letter in connection_array:
            break
        connection_array[j][1] = letter  

setting_change = ["A", "C"]
letter_passed = "A"

test = function_change(setting_change, letter_passed)
print (test)

# connection_array = [[0]*2]*6    # arr = [[0]*cols]*rows
connection_array = [["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"]]
print(connection_array)

print("How many conections do you want to make? (1-6)")
numcon = input()
numcon = int(numcon)    # parse string into an integer

test2 = enter_settings(numcon)
print(connection_array)

# print (test2)
    

