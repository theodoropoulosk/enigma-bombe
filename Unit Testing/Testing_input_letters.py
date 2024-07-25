#Applied Programming Enigma

from subprocess import call

import keyboard
import time

#Changing The letter 
def function_change(letter_passed):
    for s in range(6):
        if letter_passed == connection_list[s][0]:
            letter_passed = connection_list[s][1]
        elif letter_passed == connection_list[s][1]:
            letter_passed = connection_list[s][0]   
    return letter_passed
    

#Populating The connection list
def enter_settings(numcon):
    start = 0
    for i in range(6):
        if connection_list[i][0] == "0":
            start = i
            break
    for j in range(start, (start+numcon)):
        print("For connection", j+1)
        ok = 0
        while ok == 0:
            print("Enter first capital letter:")
            letter = input().upper()
            for k in range(j+1):
                if connection_list[k][0] == letter or connection_list[k][1] == letter:
                    ok = 0
                    print("Repeated letter, Try again")
                    break
                else:
                    ok = 1
        connection_list[j][0] = letter
        ok = 0
        while ok == 0:
            print("Enter second capital letter:")
            letter = input().upper()
            for k in range(j+1):
                if connection_list[k][0] == letter or connection_list[k][1] == letter:
                    ok = 0
                    print("Repeated letter, Try again")
                    break
                else:
                    ok = 1
        connection_list[j][1] = letter  
        

connection_list = [["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"]]     

 # Loop For Plugboard
def plugbrd_loop():
    reply = "A"

    while reply != "E":
        print("Make connection (M), Delete connection (D), View connections (V), Exit (E)")
        reply = input().upper()
        if reply == "M":
            print("How many connections do you want to make? (1-6)")
            numcon = int(input())
            available_conn = sum(1 for conn in connection_list if conn[0] == "0")
            if numcon > available_conn:
                print("Number of connections not possible")
            else:
                enter_settings(numcon)
                print(connection_list)
        elif reply == "D":
            print(connection_list)
            print("Enter number of connection you want to delete")
            num2 = int(input())
            print(connection_list[num2-1])
            print("Are you sure you want to delete this connection? (Y or N)")
            reply2 = input().upper()
            if reply2 == "Y":
                connection_list[num2-1] = ["0","0"]
                print(connection_list)
        elif reply == "V":
            print(connection_list)   


## ---------------- UNIT TEST HERE  ----------------------
with open("test1.txt","r") as f:#change the name of text file to change test case
    testlist = f.read().splitlines()
#testcase=f.readlines()
testcase = testlist[0:18] 
selection = testcase[1]
# moretestvar = testcase[3]
# moretestvar2 = testcase[4]
# moretestvar3 = testcase[5]
# moretestvar4 = testcase[6]
# moretestvar5 = testcase[7]
# moretestvar6 = testcase[8]
# moretestvar7 = testcase[9]
# moretestvar8 = testcase[10]
testassert = testlist[19:] #values to compare with

# Rotors
class Rotor:
    def __init__(self, array):
        self.array = array
        self.position = 0

    def set_position(self, position):
        self.position = int(position) % 26

    def forward(self, in_char):
        shifted_input = (in_char + self.position) % 26
        return (self.array[shifted_input] - self.position) % 26

    def backward(self, in_char):
        return (self.array.index((in_char + self.position) % 26) - self.position) % 26

    def rotate(self):
        self.position = (self.position + 1) % 26
        return self.position == 0

def asign_starts(rotor1, rotor2, rotor3):
   

    setting1 = input("Enter the starting configuration of rotor 1 (number 0-25) ")
    setting2 = input("Enter the starting configuration of rotor 2 (number 0-25) ")
    setting3 = input("Enter the starting configuration of rotor 3 (number 0-25) ")
    rotor1.set_position(setting1)
    rotor2.set_position(setting2)
    rotor3.set_position(setting3)
    

def run(letter, rotor1, rotor2, rotor3, reflector):
    letter = rotor1.forward(letter)
    letter = rotor2.forward(letter)
    letter = rotor3.forward(letter)
    letter = reflector.forward(letter)
    letter = rotor3.backward(letter)
    letter = rotor2.backward(letter)
    letter = rotor1.backward(letter)
    return letter


# ------------------------------------------------TEST INSERT PLUGBOARD
time.sleep(1)
keyboard.write(testcase[1])
keyboard.press('enter')

# To enter Plugboard Settings
plugbrd_loop()


# To enter Rotor Settings 
array1 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
array2 = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]
array3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
reflect_arr = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
rotor1 = Rotor(array1)
rotor2 = Rotor(array2)
rotor3 = Rotor(array3)
# ----------------------------------------------TEST INSERT POSITIONS
time.sleep(1)
keyboard.write(testcase[2])
keyboard.press('enter')
time.sleep(1)
keyboard.write(testcase[3])
keyboard.press('enter')
time.sleep(1)
keyboard.write(testcase[4])
keyboard.press('enter')
asign_starts(rotor1, rotor2, rotor3)

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# To Enter the message
# --------------------------------------------TEST INSERT LETTER
time.sleep(1)
keyboard.write(testcase[5])
keyboard.press('enter')
print("Enter your letter: ")
initial_mes = input().upper()
print(initial_mes)
encirpted_mes = 0

# Integration Loop
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
reflector = Rotor(reflect_arr)

wheel1 = rotor1.position
wheel2 = rotor2.position
i = 0
y = 6
for x in range(int(testcase[0])-1):
    
    print("Passed Letter: ") 
    print(initial_mes[i])

    test1 = function_change(initial_mes[i]) 
    print("Plugboard 1: ")
    print(test1)

    letter = alphabet.index(test1)

    n = run(letter, rotor1, rotor2, rotor3, reflector) 
    test2 = alphabet[n]
    print("Rotors: ")
    print(test2)

    test3 = function_change(test2)
    print("Plugboard 2: ")
    print(test3)

    
    print("\n")

    encirpted_mes = test3

    # Rotors rotation logic
    # router 1
    rotor1.rotate()
    wheel1 = wheel1 + 1
    # router 2
    if (wheel1 % 26) == 0:
        rotor2.rotate()
        wheel2 = wheel2 + 1
    # router 3
    if (((wheel2 % 26)+(wheel1 % 26)) == 0):
        rotor3.rotate()
         
    print("Rotor Positions:")
    print(rotor1.position)
    print(rotor2.position)
    print(rotor3.position)
    print("Initial Message: ")
    print(initial_mes)
    print("Encrypted Letter: ")
    print(encirpted_mes)
    print("------------------------------------------------")
    
   
    time.sleep(1)
    keyboard.write(testcase[y])
    keyboard.press('enter')
    # To Enter the message
    print("Enter your letter: ")
    initial_mes = input().upper()
    print(initial_mes)
    if testcase[y + 1] == "Letters_stop":
        print("Passed Letter: ") 
        print(initial_mes[i])

        test1 = function_change(initial_mes[i]) 
        print("Plugboard 1: ")
        print(test1)

        letter = alphabet.index(test1)

        n = run(letter, rotor1, rotor2, rotor3, reflector) 
        test2 = alphabet[n]
        print("Rotors: ")
        print(test2)

        test3 = function_change(test2)
        print("Plugboard 2: ")
        print(test3)

        
        print("\n")

        encirpted_mes = test3

        # Rotors rotation logic
        # router 1
        rotor1.rotate()
        wheel1 = wheel1 + 1
        # router 2
        if (wheel1 % 26) == 0:
            rotor2.rotate()
            wheel2 = wheel2 + 1
        # router 3
        if (((wheel2 % 26)+(wheel1 % 26)) == 0):
            rotor3.rotate()
            
        print("Rotor Positions:")
        print(rotor1.position)
        print(rotor2.position)
        print(rotor3.position)
        print("Initial Message: ")
        print(initial_mes)
        print("Encrypted Letter: ")
        print(encirpted_mes)
        print("------------------------------------------------")
    y = y + 1
    
    
    
 
  