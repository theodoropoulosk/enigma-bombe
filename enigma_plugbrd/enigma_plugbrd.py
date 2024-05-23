
def function_change(setting_change, letter_passed):
    if letter_passed == setting_change[0]:
        letter_passed = setting_change[1]
    elif letter_passed == setting_change[1]:
        letter_passed = setting_change[0]
    return letter_passed

setting_change = ["A", "C"]
letter_passed = "A"

test = function_change(setting_change, letter_passed)

print (test)

print("How many conections do you want to make? (1-6)")
numcon = input()

def enter_settings(numcon):

    rows, cols = (6, 2)
    conect = [[0]*cols]*rows
    print (conect)

    for j in range (numcon):
        
    
        for i in range(2):
            print("Enter Capital letter:")
            conect[i][j] = input()


        return conect

test2 = enter_settings()

print (test2)
    
