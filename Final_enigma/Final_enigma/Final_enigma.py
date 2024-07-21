#Applied Programming Enigma

import sqlite3

# database file connection 
database = sqlite3.connect("EnigmaConfiguration.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 

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
def rotor_configuration(selection):
    #selection= input("please enter the rotor you would like to select:")
    query_result=[]
    rotorconfig=[]

    if selection=='1':
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM ROTOR WHERE ID = 'ROT1'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
   
    elif selection=='2':
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM ROTOR WHERE ID = 'ROT2'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
    elif selection=='3':
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM ROTOR WHERE ID = 'ROT3'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
    
    elif selection=='4':
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM ROTOR WHERE ID = 'ROT4'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()

    elif selection=='5':
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM ROTOR WHERE ID = 'ROT5'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
    
    for x in  range (26):
        rotorconfig.append(query_result[0][x])
        
    return rotorconfig

def reflector_configuration(selection):
    #selection= input("please enter the rotor you would like to select:")
    query_result=[]
    refconfig=[]

    if selection=='1':
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM REFLECTOR WHERE ID = 'REF1'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
   
    elif selection=='2':
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM REFLECTOR WHERE ID = 'REF2'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
    elif selection=='3':
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM REFLECTOR WHERE ID = 'REF3'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
    
    for x in  range (26):
        refconfig.append(query_result[0][x])
        
    return refconfig
        


# To enter Plugboard Settings
plugbrd_loop()

# To enter Rotor Settings 
set=0

while(set==0):
    selection1= input("please enter your selection for rotor 1 (1-5):")
    selection2= input("please enter your selection for rotor 2 (1-5):")
    selection3= input("please enter your selection for rotor 3 (1-5):")

    refselection= input("please enter your selection for the reflecor (1-3): ")
  
    if (selection1 != selection2 != selection3):
            array1=rotor_configuration(selection1)
            array2=rotor_configuration(selection2)
            array3=rotor_configuration(selection3)
            reflect_arr=reflector_configuration(refselection)
            
            set=1
    else:
        print("the same rotor can not be selected more than once ")
# array1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
# array2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
# array3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
#reflect_arr = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
rotor1 = Rotor(array1)
rotor2 = Rotor(array2)
rotor3 = Rotor(array3)
asign_starts(rotor1, rotor2, rotor3)

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# To Enter the message
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
while i == 0:
    
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
    
    # To Enter the message
    print("Enter your letter: ")
    initial_mes = input().upper()
    print(initial_mes)
