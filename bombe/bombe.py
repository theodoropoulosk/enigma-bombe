from os import name

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

# Variable Declaration
plugboard_mapping = [["A","U"],["C","D"],["F","G"],["H","I"],["J","K"],["L","M"]]  
discarded_mapping = [["O","P"],["Q","R"],["S","T"],["U","V"],["W","X"],["Y","Z"]]  
crib_cyphertex = [["U", "E"], ["E", "G"], ["G", "R"], ["R", "A"], ["A", "S"], ["S", "V"], ["V", "E"], ["E", "N"], ["H", "Z"], ["Z", "R"], ["R", "G"], ["G", "L"]]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#Rotor Declaration
array1 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
array2 = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]
array3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
reflect_arr = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
rotor1 = Rotor(array1)
rotor2 = Rotor(array2)
rotor3 = Rotor(array3)
reflector = Rotor(reflect_arr)

# Initiating the Crib and Cyphertext mapping 
# print("Enter the Crib")
# crib_in = input() 
# print("Enter the Cyphertext")
# cyphertext_in = input() 
 
for i in range (26):
    plugboard_guess = alphabet[i] 
    
    for f in range (len(crib_cyphertex)):
        print ("Mapping Guess: ")
        print (plugboard_guess, crib_cyphertex[f][0])
        
        match = False
       
        #Check if plugboard guess already exists in mapping
        for j in range (len(plugboard_mapping)):
            # print ("Plugboard Mapping: ", plugboard_mapping[j])
            if plugboard_guess in plugboard_mapping[j] and crib_cyphertex[f][0] in plugboard_mapping[j]:
                match = True
                print("match")
                break
            
        #Check if plugboard guess already exists in discarded mapping
        for j in range (len(discarded_mapping)):
            # print (discarded_mapping[j])
            if plugboard_guess in discarded_mapping[j] and crib_cyphertex[f][0] in discarded_mapping[j]:
                print("match")
                match = True
                break
            
        if match: 
            continue

    #Run The Rotors
    letter = plugboard_guess

    value = alphabet.index(letter)
    
    n = run(value, rotor1, rotor2, rotor3, reflector) 
    #     #print(alphabet[n])

    print("Rotors Output: ")
    print((alphabet[n]), crib_cyphertex[f][1])
    

    for f in range (len(crib_cyphertex)):
        print ("Rotor1:")
        print (wheel1)
        print ("Rotor2:")
        print (wheel2)
        print ("Rotor3:")
        print (wheel3)
        
        print ("Plugboard Guess: ")
        print (alphabet[n], crib_cyphertex[f][1])
        
        match = False
       
        #Check if plugboard guess already exists in mapping
        for j in range (len(plugboard_mapping)):
            print (plugboard_mapping[j])
            if (alphabet[n]) in plugboard_mapping[j] and crib_cyphertex[f][1] in plugboard_mapping[j]:
                match = True
                print("match")
                break
            
        #Check if plugboard guess already exists in discarded mapping
        for j in range (len(discarded_mapping)):
            print (discarded_mapping[j])
            if (alphabet[n]) in discarded_mapping[j] and crib_cyphertex[f][1] in discarded_mapping[j]:
                print("match")
                match = True
                break
            
        if match:
            discarded_mapping.append(plugboard_mapping.copy())
            plugboard_mapping = []
            print("Discarded Mapping:")
            print(discarded_mapping)
            
            # rotor 1
            rotor1.rotate()
            wheel1 = wheel1 + 1
            # rotor 2
            if (wheel1 % 26) == 0:
                rotor2.rotate()
                wheel2 = wheel2 + 1
                # rotor 3
            if (((wheel2 % 26)+(wheel1 % 26)) == 0):
                rotor3.rotate()
        
        plugboard_mapping.append((alphabet[n], crib_cyphertex[f][1]))
        print ("Plugboard Maping:")
        print (plugboard_mapping)




