from os import name
class Rotor:
    # Attributes
    name = "Default"
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    start_value = 0
    
    # constructor
    def __init__(self, in_name, in_alphabet, in_start_value):
        self.name = in_name
        self.alphabet = in_alphabet
        self.start_value = in_start_value
        
    #methods
    def randomize(self, in_char, in_rotate):
        if in_char == 'A':
            return self.alphabet[(0 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'B':
            return self.alphabet[(1 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'C':
            return self.alphabet[(2 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'D':
            return self.alphabet[(3 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'E':
            return self.alphabet[(4 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'F':
            return self.alphabet[(5 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'G':
            return self.alphabet[(6 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'H':
            return self.alphabet[(7 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'I':
            return self.alphabet[(8 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'J':
            return self.alphabet[(9 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'K':
            return self.alphabet[(10 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'L':
            return self.alphabet[(11 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'M':
            return self.alphabet[(12 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'N':
            return self.alphabet[(13 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'O':
            return self.alphabet[(14 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'P':
            return self.alphabet[(15 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'Q':
            return self.alphabet[(16 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'R':
            return self.alphabet[(17 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'S':
            return self.alphabet[(18 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'T':
            return self.alphabet[(19 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'U':
            return self.alphabet[(20 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'V':
            return self.alphabet[(21 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'W':
            return self.alphabet[(22 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'X':
            return self.alphabet[(23 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'Y':
            return self.alphabet[(24 + (int(self.start_value) + int(in_rotate))) % 26]
        elif in_char == 'Z':
            return self.alphabet[(25 + (int(self.start_value) + int(in_rotate))) % 26]
        

#--------------------------------------------------- Main Code ----------------------------------------------------
wheel1 = 0
wheel2 = 0
wheel3 = 0
number_times = 1
new_alphapet=["B", "C", "A", "Q", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "D", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
char_input = input("Input character: ")

#configure rotor 1
setting1 = input("Enter the starting configuration of rotor 1 (number 0-25) ")
#              A    B    C    D    E    F    G    H    I    J    K    L    M    N    O    P    Q    R    S    T    U    V    W    X    Y    Z
#              0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25
rotor1_arr = ['Q', 'W', 'E', 'R', 'C', 'Y', 'U', 'I', 'H', 'P', 'Z', 'X', 'V', 'T', 'S', 'J', 'A', 'D', 'O', 'N', 'G', 'M', 'B', 'L', 'F', 'K']
rotor1 = Rotor("Rotor 1", rotor1_arr, setting1)

#configure rotor 2
setting2 = input("Enter the starting configuration of rotor 2 (number 0-25) ")
#              A    B    C    D    E    F    G    H    I    J    K    L    M    N    O    P    Q    R    S    T    U    V    W    X    Y    Z
#              0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25
rotor2_arr = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
rotor2 = Rotor("Rotor 2", rotor2_arr, setting2)

#configure rotor 3
# THIS ROTOR ARRAY NEEDS TO BE FIXED!!!!!
setting3 = input("Enter the starting configuration of rotor 3 (number 0-25) ")
#              A    B    C    D    E    F    G    H    I    J    K    L    M    N    O    P    Q    R    S    T    U    V    W    X    Y    Z
#              0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25
rotor3_arr = ['Q', 'W', 'E', 'R', 'C', 'Y', 'U', 'I', 'H', 'P', 'Z', 'X', 'V', 'T', 'S', 'J', 'A', 'D', 'O', 'N', 'G', 'M', 'B', 'L', 'F', 'K']
rotor3 = Rotor("Rotor 3", rotor3_arr, setting3)

#create reflector
#                 A    B    C    D    E    F    G    H    I    J    K    L    M    N    O    P    Q    R    S    T    U    V    W    X    Y    Z
#                 0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25
reflector_arr = ['Q', 'W', 'E', 'R', 'C', 'Y', 'U', 'I', 'H', 'P', 'Z', 'X', 'V', 'T', 'S', 'J', 'A', 'D', 'O', 'N', 'G', 'M', 'B', 'L', 'F', 'K']
reflector = Rotor("Reflector", reflector_arr, 0)



for x in range(number_times):
    pass1 = rotor1.randomize(char_input, wheel1)
    print(pass1)
    pass2 = rotor2.randomize(pass1, wheel2)
    print(pass2)
    pass3 = rotor3.randomize(pass2, wheel3)
    print(pass3)
    pass4 = reflector.randomize(pass3, 0);		# the reflector has a setting of 0. It never rotates
    print(pass4)
    pass5 = rotor3.randomize(pass4, wheel3)
    print(pass5)
    pass6 = rotor2.randomize(pass5, wheel2)
    print(pass6)
    output = rotor1.randomize(pass6, wheel1)
    print(output + "\n")
 
    # router 1
    wheel1+=1
	# router 2
    if (wheel1 % 26) == 0:
         wheel2 += 1
    # router 3
    if (((wheel2 % 26)+(wheel1 % 26)) == 0):
        wheel3 += 1