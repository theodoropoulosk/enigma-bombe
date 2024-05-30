from multiprocessing import connection

def function_change(letter_passed):
    for s in range(6):
        if letter_passed == connection_array[s][0]:
            letter_passed = connection_array[s][1]
        elif letter_passed == connection_array[s][1]:
            letter_passed = connection_array[s][0]   
        return letter_passed

def enter_settings(numcon):

    for j in range(numcon):
        print("For connection", j+1)
        ok = 0
        while ok == 0:
            print("Enter first capital letter:")
            letter = input()
            for k in range(j+1):
                if connection_array[k][0] == letter or connection_array[k][1] == letter:
                    ok = 0
                    print("Repeated letter, Try again")
                    break
                else:
                    ok = 1
        connection_array[j][0] = letter
        ok = 0
        while ok == 0:
            print("Enter second capital letter:")
            letter = input()
            for k in range(j+1):
                if connection_array[k][0] == letter or connection_array[k][1] == letter:
                    ok = 0
                    print("Repeated letter, Try again")
                    break
                else:
                    ok = 1
        connection_array[j][1] = letter  



# connection_array = [[0]*2]*6    # arr = [[0]*cols]*rows
connection_array = [["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"]]
print(connection_array)

print("How many conections do you want to make? (1-6)")
numcon = input()
numcon = int(numcon)    # parse string into an integer

test2 = enter_settings(numcon)
print(connection_array)

test3 = function_change("A")
print(test3)

# print (test2)
    

