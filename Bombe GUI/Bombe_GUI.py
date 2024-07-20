from tkinter import *
from tkinter import ttk
from os import name

connection_list = [["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],
					["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"]]



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


# Variable Declaration
plugboard_mapping = []  
discarded_mapping = [] 
crib_cyphertex = array_matching()
#crib_cyphertex = [["U", "E"], ["E", "G"], ["G", "R"], ["R", "A"], ["A", "S"], ["S", "V"], ["V", "E"], ["E", "N"], ["H", "Z"], ["Z", "R"], ["R", "G"], ["G", "L"]]
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


def test_func():
	print(e2.get())
    
def update_positions(one, two, three):
	rotor_position1 = Text(gui, height=3, width=7)
	rotor_position1.insert(INSERT, '\n   ' + str(one))
	rotor_position1.grid(row = 3,column = 5) 
	rotor_position1.config(state=DISABLED, bg = 'white')
	
	rotor_position2 = Text(gui, height=3, width=7)
	rotor_position2.insert(INSERT, '\n   ' + str(two)) 
	rotor_position2.grid(row = 4,column = 5) 
	rotor_position2.config(state=DISABLED, bg = 'white')
	
	rotor_position3 = Text(gui, height=3, width=7)
	rotor_position3.insert(INSERT, '\n   ' + str(three)) 
	rotor_position3.grid(row = 5,column = 5) 
	rotor_position3.config(state=DISABLED, bg = 'white')
    
def run_bombe():
    global alphabet
    global plugboard_mapping
    global discarded_mapping
    global crib_cyphertex
    for i in range (26):
        plugboard_guess = alphabet[i] 
            
        for f in range (len(crib_cyphertex)):

            if (plugboard_guess == crib_cyphertex[f][0]) :
                continue

            print ("Mapping Guess: ")
            print (plugboard_guess, crib_cyphertex[f][0])

            match = False
       
            #Check if plugboard guess already exists in mapping
            for j in range (len(plugboard_mapping)):
                print ("Plugboard Mapping: ", plugboard_mapping[j])
                if plugboard_guess in plugboard_mapping[j] and crib_cyphertex[f][0] in plugboard_mapping[j]:
                    match = True
                    print("match")
                    break
            
            #Check if plugboard guess already exists in discarded mapping
            for j in range (len(discarded_mapping)):
                print ("Discarded Mapping: ",discarded_mapping[j])
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

        print("Rotors Output: ")
        print((alphabet[n]), crib_cyphertex[f][1])

        for f in range (len(crib_cyphertex)):
            if (alphabet[n] == crib_cyphertex[f][1]):
                continue
            print ("Mapping Guess: ")
            print (alphabet[n], crib_cyphertex[f][1])
            match = False
       
            #Check if plugboard guess already exists in mapping
            for j in range (len(plugboard_mapping)):
                # print (plugboard_mapping[j])
                if (alphabet[n]) in plugboard_mapping[j] and crib_cyphertex[f][1] in plugboard_mapping[j]:
                    match = True
                    print("match")
                    break

            if match:
                discarded_mapping.append(plugboard_mapping.copy())
                plugboard_mapping = []
                print("Discarded Mapping:")
                print(discarded_mapping)
                       
            print("Rotor Positions:")
            update_positions(rotor1.position, rotor2.position, rotor3.position)
            print(rotor1.position)
            print(rotor2.position)
            print(rotor3.position)
            
            plugboard_mapping.append((alphabet[n], crib_cyphertex[f][1]))
            print ("Plugboard Maping:")
            print (plugboard_mapping)
            



if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="grey")
	gui.title("Bombe Machine")
	gui.geometry("450x450")
    
	
	# ------ Cypher Text ----- #
	
	cypher_label = Text(gui, height=2, width=10)
	cypher_label.insert(INSERT, 'Cypher\nText:') 
	cypher_label.grid(row = 1,column = 1) 
	cypher_label.config(state=DISABLED, bg = 'white')
	
	e1 = Entry(gui)
	e1.grid(row=1, column=2, columnspan=2, pady=2)
	
	buttonCypher = Button(gui, text='Enter', fg='black', bg='light grey',
					command=lambda: test_func(), height=2, width=7,)
	buttonCypher.grid(row=1, column=4)
	
	# ----- Crib Text ----- #
	
	crib_label = Text(gui, height=2, width=10)
	crib_label.insert(INSERT, 'Crib\nText:') 
	crib_label.grid(row = 2,column = 1) 
	crib_label.config(state=DISABLED, bg = 'white')
	
	e2 = Entry(gui)
	e2.grid(row=2, column=2, columnspan=2, pady=2)
		
	buttonCrib = Button(gui, text='Enter', fg='black', bg='light grey',
					command=lambda: test_func(), height=2, width=7,)
	buttonCrib.grid(row=2, column=4)
    
    # ---------- START --------- #
	Start_Button = Button(gui, text='Start', fg='black', bg='light grey',
					command=lambda: run_bombe(), height=2, width=7,)
	Start_Button.grid(row=6, column=4)
    
	# ---------- Rotor Position labels --------- #
	rotor_label = Text(gui, height=3, width=10)
	rotor_label.insert(INSERT, 'Guessed\nRotor\nPositions:') 
	rotor_label.grid(row = 3,column = 4) 
	rotor_label.config(state=DISABLED, bg = 'white')
	
	rotor_position1 = Text(gui, height=3, width=7)
	rotor_position1.insert(INSERT, '\n   ' + str(rotor1.position))
	rotor_position1.grid(row = 3,column = 5) 
	rotor_position1.config(state=DISABLED, bg = 'white')
	
	rotor_position2 = Text(gui, height=3, width=7)
	rotor_position2.insert(INSERT, '\n   ' + str(rotor2.position)) 
	rotor_position2.grid(row = 4,column = 5) 
	rotor_position2.config(state=DISABLED, bg = 'white')
	
	rotor_position3 = Text(gui, height=3, width=7)
	rotor_position3.insert(INSERT, '\n   ' + str(rotor3.position)) 
	rotor_position3.grid(row = 5,column = 5) 
	rotor_position3.config(state=DISABLED, bg = 'white')
	
	# ------- Plugboard labels -------- #
	plug_label = Text(gui, height=3, width=10)
	plug_label.insert(INSERT, 'Guessed\nPlugboard\nSettings:') 
	plug_label.grid(row = 3,column = 1) 
	plug_label.config(state=DISABLED, bg = 'white')
	
	plug1 = Label(gui, text = connection_list[0], height=3, width=7)
	plug1.grid(row=3, column=2, rowspan=1)
	plug2 = Label(gui, text = connection_list[1], height=3, width=7)
	plug2.grid(row=3, column=3, rowspan=1)
	plug3 = Label(gui, text = connection_list[2], height=3, width=7)
	plug3.grid(row=4, column=2, rowspan=1)
	plug4 = Label(gui, text = connection_list[3], height=3, width=7)
	plug4.grid(row=4, column=3, rowspan=1)
	plug5 = Label(gui, text = connection_list[4], height=3, width=7)
	plug5.grid(row=5, column=2, rowspan=1)
	plug6 = Label(gui, text = connection_list[5], height=3, width=7)
	plug6.grid(row=5, column=3, rowspan=1)
	plug7 = Label(gui, text = connection_list[6], height=3, width=7)
	plug7.grid(row=6, column=2, rowspan=1)
	plug8 = Label(gui, text = connection_list[7], height=3, width=7)
	plug8.grid(row=6, column=3, rowspan=1)
	plug9 = Label(gui, text = connection_list[8], height=3, width=7)
	plug9.grid(row=7, column=2, rowspan=1)
	plug10 = Label(gui, text = connection_list[9], height=3, width=7)
	plug10.grid(row=7, column=3, rowspan=1)
	plug11 = Label(gui, text = connection_list[10], height=3, width=7)
	plug11.grid(row=8, column=2, rowspan=1)
	plug12 = Label(gui, text = connection_list[11], height=3, width=7)
	plug12.grid(row=8, column=3, rowspan=1)
	plug13 = Label(gui, text = connection_list[12], height=3, width=7)
	plug13.grid(row=9, column=2, rowspan=1)
    
	gui.mainloop()
    
