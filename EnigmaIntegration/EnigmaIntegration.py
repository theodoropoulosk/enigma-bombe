# ##Applied Programming Enigma Keyboard
# def main():
#     message = []
    
#     while True:
#         # Ask user for a Letter
#         letter_passed = input("Please enter the letter you wish to send: ").upper() #upper forces letters to be uppercase after entry
        
#         message.append(letter_passed)
        
#         # Display current message
#         print("The message so far is: ")
#         print(" ".join(message)) #Print message with space between each letter
        
#         # Ask if complete?
#         while True: #While loop to continue asking until Y is entered 
#             choice = input("Is your message complete (Y/N): ").upper() #Force Uppercase 
            
#             if choice != 'Y' and choice != 'N': #Anything other than a Y or N is invalid
#                 print("Invalid choice. Please enter Y or N.")
#             else:
#                 break

#         # Yes is chosen final message is printed. 
#         if choice == 'Y': 
#             print("Message has been sent. The final message is: ")
#             print(" ".join(message))
#             break
        
#     letter_passed = message
#     return letter_passed   

# if __name__ == "__main__":
#     passed_var = main()
 
passed_var = input("Enter a Letter: ")

# passed_var = "A"
print ("Passed Var: ") 
print (passed_var)

from multiprocessing import connection

#Changing The letter 
def function_change(letter_passed):
    for s in range(6):
        if letter_passed == connection_list[s][0]:
            letter_passed = connection_list[s][1]
        elif letter_passed== connection_list[s][1]:
            letter_passed = connection_list[s][0]   
        return letter_passed


#Populating The conection list
def enter_settings(numcon):

    for j in range(numcon):
        print("For connection", j+1)
        ok = 0
        while ok == 0:
            print("Enter first capital letter:")
            letter = input()
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
            letter = input()
            for k in range(j+1):
                if connection_list[k][0] == letter or connection_list[k][1] == letter:
                    ok = 0
                    print("Repeated letter, Try again")
                    break
                else:
                    ok = 1
        connection_list[j][1] = letter  
        

# connection_list = [[0]*2]*6    # arr = [[0]*cols]*rows
connection_list = [["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"]]
print(connection_list)

 # Loop For Plugboard
def plugbrd_loop ():
    reply = "A"
    while (reply != "E"):
        print("Make connection (M), Delete connection (D), View connections (V), Exit (E)")
        reply = input()
        if reply == "M":
            print("How many connections do you want to make? (1-6)")
            numcon = input()
            numcon = int(numcon)    # parse string into an integer
            test2 = enter_settings(numcon)
            print(connection_list)
        elif reply == "D":
            print(connection_list)
            print("Enter number of connection you want to delete")
            num2 = input()
            num2 = int(num2)
            print(connection_list[num2-1])
            print("Are you sure you want to delete this connection? (Y or N)")
            reply2 = input()
            if reply2 == "Y":
                del connection_list[num2-1]
                connection_list.append(["0","0"])
                print(connection_list)
        elif reply == "V":
            print(connection_list)

plugbrd_loop()
test3 = function_change(passed_var)  
print(test3)     

print ("Rotors")
# Rotors
from os import name
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
    if rotor1.rotate() or rotor2.rotate() or rotor3.rotate():
        pass
    return letter

wheel1 = 0
wheel2 = 0
wheel3 = 0
number_times = 1
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#letter = input("Input letter: ")
letter = test3 
array1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
array2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
array3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
reflect_arr = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
rotor1 = Rotor(array1)
rotor2 = Rotor(array2)
rotor3 = Rotor(array3)
reflector = Rotor(reflect_arr)
asign_starts(rotor1, rotor2, rotor3)

value = alphabet.index(letter)

for x in range(number_times):
    n = run(value, rotor1, rotor2, rotor3, reflector) 
    print(alphabet[n])
    
    # router 1
    rotor1.rotate()
    # router 2
    if (wheel1 % 26) == 0:
        rotor2.rotate()
    # router 3
    if (((wheel2 % 26)+(wheel1 % 26)) == 0):
        rotor3.rotate()


    

