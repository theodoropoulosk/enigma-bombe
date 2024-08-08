from os import name

import sqlite3

# database file connection 
database = sqlite3.connect("EnigmaConfiguration.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 


#Rotors Set Up
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

def asign_starts(rotor1, rotor2, rotor3, var):
    sql_command = """SELECT * FROM PAST_CONFIG"""
    cursor.execute(sql_command)
    config_table = cursor.fetchall()
    setting1 = config_table[int(var)][4]
    setting2 = config_table[int(var)][5]
    setting3 = config_table[int(var)][6]
    rotor1.set_position(setting1)
    rotor2.set_position(setting2)
    rotor3.set_position(setting3)
    

def rotation():
    global wheel1
    global wheel2
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


def run(letter, rotor1, rotor2, rotor3, reflector):
    letter = rotor1.forward(letter)
    letter = rotor2.forward(letter)
    letter = rotor3.forward(letter)
    letter = reflector.forward(letter)
    letter = rotor3.backward(letter)
    letter = rotor2.backward(letter)
    letter = rotor1.backward(letter)
    return letter

def array_matching():
    crypted_message=input("Please enter the encripted message (enigma output): ")
    decoder_guess=input("Please enter your possibple guess (must be less than or equal to encrypted message:)")
    
    crypt_length=len([ele for ele in crypted_message if ele.isalpha()])
    guess_length=len([ele for ele in decoder_guess if ele.isalpha()])
    
    length_difference= crypt_length-guess_length
    print(length_difference )
    poss_combo = []
    
    for y in range (length_difference+1):
        for x in range (y, guess_length+y):
            if (crypted_message[x] != decoder_guess[x-y]):
             poss_combo.append([crypted_message[x], decoder_guess[x-y]])
    
     
    print (poss_combo)    
    return poss_combo

def rotor_configuration(selection):
    #selection= input("please enter the rotor you would like to select:")
    cursor = database.cursor() 
    query_result=[]
    rotorconfig=[]

    if selection==1:
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM ROTOR WHERE ID = 'ROT1'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
   
    elif selection==2:
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM ROTOR WHERE ID = 'ROT2'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
    elif selection==3:
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM ROTOR WHERE ID = 'ROT3'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
    
    elif selection==4:
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM ROTOR WHERE ID = 'ROT4'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()

    elif selection==5:
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM ROTOR WHERE ID = 'ROT5'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
    
    print(query_result[0][0])
    for x in  range (26):
        rotorconfig.append(query_result[0][x])
        
    return rotorconfig

def reflector_configuration(selection):
    #selection= input("please enter the rotor you would like to select:")
    query_result=[]
    refconfig=[]

    if selection==1:
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM REFLECTOR WHERE ID = 'REF1'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
   
    elif selection==2:
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM REFLECTOR WHERE ID = 'REF2'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
    elif selection==3:
        sql_command = """SELECT A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z FROM REFLECTOR WHERE ID = 'REF3'""" 
        cursor.execute(sql_command)
        query_result = cursor.fetchall()
    
    for x in  range (26):
        refconfig.append(query_result[0][x])
        
    return refconfig


wheel1 = 0
wheel2 = 0




# Variable Declaration
plugboard_mapping = []  

cursor = database.cursor() 

sql_command = """SELECT * FROM PAST_CONFIG"""
cursor.execute(sql_command)
config_table = cursor.fetchall()

column_names = [description[0] for description in cursor.description]
print(f"{' |'.join(column_names)}")
print('-' * (len(column_names) * 6))

for row in config_table:
   print('  |  '.join(map(str, row)))


var = input("Which row of configuration do you want to try " )
var = int(var)-1
print(var)
crib_cyphertex = array_matching()
#crib_cyphertex = [["U", "E"], ["E", "G"], ["G", "R"], ["R", "A"], ["A", "S"], ["S", "V"], ["V", "E"], ["E", "N"], ["H", "Z"], ["Z", "R"], ["R", "G"], ["G", "L"]]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Rotor Declaration
array1 = rotor_configuration(config_table[var][0]) #[0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
array2 = rotor_configuration(config_table[var][1]) #[21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]
array3 = rotor_configuration(config_table[var][2]) #[1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
reflect_arr = reflector_configuration(config_table[var][3]) #[24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
rotor1 = Rotor(array1)
rotor2 = Rotor(array2)
rotor3 = Rotor(array3)


asign_starts(rotor1, rotor2, rotor3, var)
reflector = Rotor(reflect_arr)

for i in range (len(crib_cyphertex)): 
      
    #Run The Rotors
    letter = crib_cyphertex[i][0]
    value = alphabet.index(letter)
    n = run(value, rotor1, rotor2, rotor3, reflector) 

    print("Rotors Output: ")
    print((alphabet[n]), crib_cyphertex[i][1])
    plugboard_mapping.append((alphabet[n], crib_cyphertex[i][1]))  
            
    rotation()
        
    print("Rotor Positions:")
    print(rotor1.position)
    print(rotor2.position)
    print(rotor3.position)
        
    
    print ("Plugboard Maping:")
    print (plugboard_mapping)
