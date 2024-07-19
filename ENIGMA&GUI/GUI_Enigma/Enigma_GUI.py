#Applied Programming Enigma
from tkinter import *
expression = ""
from tkinter import messagebox
from threading import Thread
from subprocess import call
connection_list = [["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],
					["0","0"],["0","0"],["0","0"],["0","0"], ["0","0"],["0","0"],["0","0"]]
count = 0
encirpted_mes = 0
	
def lightup(sample_output):
	# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx LIGHTBOARD xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	if sample_output == 'Q':
		textQ.config(bg = 'yellow')
	else:
		textQ.config(bg = 'white')
	if sample_output == 'W':
		textW.config(bg = 'yellow')
	else:
		textW.config(bg = 'white')	
	if sample_output == 'E':
		textE.config(bg = 'yellow')
	else:
		textE.config(bg = 'white')
	if sample_output == 'R':
		textR.config(bg = 'yellow')
	else:
		textR.config(bg = 'white')		
	if sample_output == 'T':
		textT.config(bg = 'yellow')
	else:
		textT.config(bg = 'white')		
	if sample_output == 'Y':
		textY.config(bg = 'yellow')
	else:
		textY.config(bg = 'white')
	if sample_output == 'U':
		textU.config(bg = 'yellow')
	else:
		textU.config(bg = 'white')	
	if sample_output == 'I':
		textI.config(bg = 'yellow')
	else:
		textI.config(bg = 'white')	
	if sample_output == 'O':
		textO.config(bg = 'yellow')
	else:
		textO.config(bg = 'white')	
	if sample_output == 'P':
		textP.config(bg = 'yellow')
	else:
		textP.config(bg = 'white')
	# -------------------- NEW LINE -----------------------------#
	if sample_output == 'A':
		textA.config(bg = 'yellow')
	else:
		textA.config(bg = 'white')	
	if sample_output == 'S':
		textS.config(bg = 'yellow')
	else:
		textS.config(bg = 'white')		
	if sample_output == 'D':
		textD.config(bg = 'yellow')
	else:
		textD.config(bg = 'white')		
	if sample_output == 'F':
		textF.config(bg = 'yellow')
	else:
		textF.config(bg = 'white')		
	if sample_output == 'G':
		textG.config(bg = 'yellow')
	else:
		textG.config(bg = 'white')		
	if sample_output == 'H':
		textH.config(bg = 'yellow')
	else:
		textH.config(bg = 'white')		
	if sample_output == 'J':
		textJ.config(bg = 'yellow')
	else:
		textJ.config(bg = 'white')		
	if sample_output == 'K':
		textK.config(bg = 'yellow')
	else:
		textK.config(bg = 'white')		
	if sample_output == 'L':
		textL.config(bg = 'yellow')
	else:
		textL.config(bg = 'white')
	# -------------------- NEW LINE -----------------------------#
	if sample_output == 'Z':
		textZ.config(bg = 'yellow')
	else:
		textZ.config(bg = 'white')		
	if sample_output == 'X':
		textX.config(bg = 'yellow')
	else:
		textX.config(bg = 'white')		
	if sample_output == 'C':
		textC.config(bg = 'yellow')
	else:
		textC.config(bg = 'white')		
	if sample_output == 'V':
		textV.config(bg = 'yellow')
	else:
		textV.config(bg = 'white')		
	if sample_output == 'B':
		textB.config(bg = 'yellow')
	else:
		textB.config(bg = 'white')		
	if sample_output == 'N':
		textN.config(bg = 'yellow')
	else:
		textN.config(bg = 'white')
	if sample_output == 'M':
		textM.config(bg = 'yellow')
	else:
		textM.config(bg = 'white')
		
def press(letter):
	# point out the global expression variable and set it
	global expression
	global count 
	expression = expression + str(letter)
	equation.set(expression)
	
	# add one to the global count so that it can be used to grab a letter for output
	get = expression_field.get()
	output = get[count]
	print(output)
	count += 1
		
def two_func_keyboard(letter, rotor1, rotor2, rotor3):
	press(letter)
	enigma_run(letter, rotor1, rotor2, rotor3)
	
def start_main(letter, rotor1, rotor2, rotor3):
    t = Thread(target=two_func_keyboard, args=(letter, rotor1, rotor2, rotor3), daemon=True)
    t.start()

def clear():
	global expression
	global count 
	expression = ""
	equation.set(expression)
	count = 0
	
def update_plugs(letter):
	global connection_list
	possible = 1
	for i in range(12):
		if (connection_list[i][0] == letter) or (connection_list[i][1] == letter):
			possible = 0
			messagebox.showinfo("Warning", "This letter has already been selected.") 
	if (connection_list[12][1] != "0"):
		messagebox.showinfo("Warning","No more plugboard settings possible.")
	elif (possible == 1):
		for i in range(13):
			if (connection_list[i][0] == "0"):
				connection_list[i][0] = letter
				break
			elif (connection_list[i][1] == "0"):
				connection_list[i][1] = letter
				break
	plug1 = Label(gui, text = connection_list[0], height=3, width=6)
	plug1.grid(row=6, column=11, rowspan=1)
	plug2 = Label(gui, text = connection_list[1], height=3, width=6)
	plug2.grid(row=6, column=12, rowspan=1)
	plug3 = Label(gui, text = connection_list[2], height=3, width=6)
	plug3.grid(row=7, column=11, rowspan=1)
	plug4 = Label(gui, text = connection_list[3], height=3, width=6)
	plug4.grid(row=7, column=12, rowspan=1)
	plug5 = Label(gui, text = connection_list[4], height=3, width=6)
	plug5.grid(row=8, column=11, rowspan=1)
	plug6 = Label(gui, text = connection_list[5], height=3, width=6)
	plug6.grid(row=8, column=12, rowspan=1)
	plug7 = Label(gui, text = connection_list[6], height=3, width=6)
	plug7.grid(row=9, column=11, rowspan=1)
	plug8 = Label(gui, text = connection_list[7], height=3, width=6)
	plug8.grid(row=9, column=12, rowspan=1)
	plug9 = Label(gui, text = connection_list[8], height=3, width=6)
	plug9.grid(row=10, column=11, rowspan=1)
	plug10 = Label(gui, text = connection_list[9], height=3, width=6)
	plug10.grid(row=10, column=12, rowspan=1)
	plug11 = Label(gui, text = connection_list[10], height=3, width=6)
	plug11.grid(row=11, column=11, rowspan=1)
	plug12 = Label(gui, text = connection_list[11], height=3, width=6)
	plug12.grid(row=11, column=12, rowspan=1)
	plug13 = Label(gui, text = connection_list[12], height=3, width=6)
	plug13.grid(row=12, column=11, rowspan=1)
	
def update_connection_list(letter):
    h = Thread(target = update_plugs, args=(letter), daemon=True)
    h.start()
	
def clear_plugs():
	global connection_list
	connection_list = [["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],
					["0","0"],["0","0"],["0","0"],["0","0"],["0","0"],["0","0"]]
	plug1 = Label(gui, text = connection_list[0], height=3, width=6) # makes plugboard show up before pressing
	plug1.grid(row=6, column=11, rowspan=1)
	plug2 = Label(gui, text = connection_list[1], height=3, width=6)
	plug2.grid(row=6, column=12, rowspan=1)
	plug3 = Label(gui, text = connection_list[2], height=3, width=6)
	plug3.grid(row=7, column=11, rowspan=1)
	plug4 = Label(gui, text = connection_list[3], height=3, width=6)
	plug4.grid(row=7, column=12, rowspan=1)
	plug5 = Label(gui, text = connection_list[4], height=3, width=6)
	plug5.grid(row=8, column=11, rowspan=1)
	plug6 = Label(gui, text = connection_list[5], height=3, width=6)
	plug6.grid(row=8, column=12, rowspan=1)
	plug7 = Label(gui, text = connection_list[6], height=3, width=6)
	plug7.grid(row=9, column=11, rowspan=1)
	plug8 = Label(gui, text = connection_list[7], height=3, width=6)
	plug8.grid(row=9, column=12, rowspan=1)
	plug9 = Label(gui, text = connection_list[8], height=3, width=6)
	plug9.grid(row=10, column=11, rowspan=1)
	plug10 = Label(gui, text = connection_list[9], height=3, width=6)
	plug10.grid(row=10, column=12, rowspan=1)
	plug11 = Label(gui, text = connection_list[10], height=3, width=6)
	plug11.grid(row=11, column=11, rowspan=1)
	plug12 = Label(gui, text = connection_list[11], height=3, width=6)
	plug12.grid(row=11, column=12, rowspan=1)
	plug13 = Label(gui, text = connection_list[12], height=3, width=6)
	plug13.grid(row=12, column=11, rowspan=1)
	
def clear_plugboard():
    h = Thread(target = clear_plugs, daemon=True)
    h.start()

#Changing The letter 
def function_change(letter_passed):
    for s in range(6):
        if letter_passed == connection_list[s][0]:
            letter_passed = connection_list[s][1]
        elif letter_passed == connection_list[s][1]:
            letter_passed = connection_list[s][0]   
    return letter_passed
    
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

def update_positions(one, two, three):
	rotor_position1 = Text(gui, height=3, width=7)
	rotor_position1.insert(INSERT, '\n   ' + str(one))
	rotor_position1.grid(row = 3,column = 14) 
	rotor_position1.config(state=DISABLED, bg = 'white')
	
	rotor_position2 = Text(gui, height=3, width=7)
	rotor_position2.insert(INSERT, '\n   ' + str(two)) 
	rotor_position2.grid(row = 4,column = 14) 
	rotor_position2.config(state=DISABLED, bg = 'white')
	
	rotor_position3 = Text(gui, height=3, width=7)
	rotor_position3.insert(INSERT, '\n   ' + str(three)) 
	rotor_position3.grid(row = 5,column = 14) 
	rotor_position3.config(state=DISABLED, bg = 'white')



#Enigma functions
def enigma_run(in_char, rotor1:Rotor, rotor2:Rotor, rotor3:Rotor):
	global encirpted_mes
	initial_mes = in_char
	print(initial_mes)
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
		print("New Rotor Positions:")
		print(rotor1.position)
		print(rotor2.position)
		print(rotor3.position)
		print("Initial Message: ")
		print(initial_mes)
		print("Encrypted Letter: ")
		print(encirpted_mes)
		lightup(encirpted_mes)
		update_positions(rotor1.position, rotor2.position, rotor3.position)
		print("------------------------------------------------")
		# To Enter the message
		print("Enter your letter: ")
		initial_mes = input().upper()
		print(initial_mes)
    

# To enter Rotor Settings 
array1 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
array2 = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]
array3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
reflect_arr = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
rotor1 = Rotor(array1)
rotor2 = Rotor(array2)
rotor3 = Rotor(array3)
asign_starts(rotor1, rotor2, rotor3)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="brown")
	gui.title("Enigma")
	gui.geometry("850x650")
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation)
	expression_field.grid(columnspan=10, ipadx=70)
	equation.set('enter your message')
	
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx LIGHTBOARD xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	textQ = Text(gui, height=3, width=7)
	textQ.insert(INSERT, '\n   Q') 
	textQ.grid(row = 3,column = 0) 
	textQ.config(state=DISABLED)
	
	textW = Text(gui, height=3, width=7)
	textW.insert(INSERT, '\n   W') 
	textW.grid(row = 3,column = 1) 
	textW.config(state=DISABLED)
	
	textE = Text(gui, height=3, width=7)
	textE.insert(INSERT, '\n   E') 
	textE.grid(row = 3,column = 2) 
	textE.config(state=DISABLED)
	
	textR = Text(gui, height=3, width=7)
	textR.insert(INSERT, '\n   R') 
	textR.grid(row = 3,column = 3) 
	textR.config(state=DISABLED)
	
	textT = Text(gui, height=3, width=7)
	textT.insert(INSERT, '\n   T') 
	textT.grid(row = 3,column = 4) 
	textT.config(state=DISABLED)
	
	textY = Text(gui, height=3, width=7)
	textY.insert(INSERT, '\n   Y') 
	textY.grid(row = 3,column = 5) 
	textY.config(state=DISABLED)
	
	textU = Text(gui, height=3, width=7)
	textU.insert(INSERT, '\n   U') 
	textU.grid(row = 3,column = 6) 
	textU.config(state=DISABLED)
	
	textI = Text(gui, height=3, width=7)
	textI.insert(INSERT, '\n   I') 
	textI.grid(row = 3,column = 7) 
	textI.config(state=DISABLED)
	
	textO = Text(gui, height=3, width=7)
	textO.insert(INSERT, '\n   O') 
	textO.grid(row = 3,column = 8) 
	textO.config(state=DISABLED)
	
	textP = Text(gui, height=3, width=7)
	textP.insert(INSERT, '\n   P') 
	textP.grid(row = 3,column = 9) 
	textP.config(state=DISABLED)
	
	textA = Text(gui, height=3, width=7)
	textA.insert(INSERT, '\n   A') 
	textA.grid(row = 4,column = 0) 
	textA.config(state=DISABLED)

	textS = Text(gui, height=3, width=7)
	textS.insert(INSERT, '\n   S') 
	textS.grid(row = 4,column = 1) 
	textS.config(state=DISABLED)
	
	textD = Text(gui, height=3, width=7)
	textD.insert(INSERT, '\n   D') 
	textD.grid(row = 4,column = 2) 
	textD.config(state=DISABLED)
	
	textF = Text(gui, height=3, width=7)
	textF.insert(INSERT, '\n   F') 
	textF.grid(row = 4,column = 3) 
	textF.config(state=DISABLED)
	
	textG = Text(gui, height=3, width=7)
	textG.insert(INSERT, '\n   G') 
	textG.grid(row = 4,column = 4) 
	textG.config(state=DISABLED)
	
	textH = Text(gui, height=3, width=7)
	textH.insert(INSERT, '\n   H') 
	textH.grid(row = 4,column = 5) 
	textH.config(state=DISABLED)
	
	textJ = Text(gui, height=3, width=7)
	textJ.insert(INSERT, '\n   J') 
	textJ.grid(row = 4,column = 6) 
	textJ.config(state=DISABLED)
	
	textK = Text(gui, height=3, width=7)
	textK.insert(INSERT, '\n   K') 
	textK.grid(row = 4,column = 7) 
	textK.config(state=DISABLED)
	
	textL = Text(gui, height=3, width=7)
	textL.insert(INSERT, '\n   L') 
	textL.grid(row = 4,column = 8) 
	textL.config(state=DISABLED)
	
	textZ = Text(gui, height=3, width=7)
	textZ.insert(INSERT, '\n   Z') 
	textZ.grid(row = 5,column = 1) 
	textZ.config(state=DISABLED)
	
	textX = Text(gui, height=3, width=7)
	textX.insert(INSERT, '\n   X') 
	textX.grid(row = 5,column = 2) 
	textX.config(state=DISABLED)
	
	textC = Text(gui, height=3, width=7)
	textC.insert(INSERT, '\n   C') 
	textC.grid(row = 5,column = 3) 
	textC.config(state=DISABLED)
	
	textV = Text(gui, height=3, width=7)
	textV.insert(INSERT, '\n   V') 
	textV.grid(row = 5,column = 4) 
	textV.config(state=DISABLED)
	
	textB = Text(gui, height=3, width=7)
	textB.insert(INSERT, '\n   B') 
	textB.grid(row = 5,column = 5) 
	textB.config(state=DISABLED)
	
	textN = Text(gui, height=3, width=7)
	textN.insert(INSERT, '\n   N') 
	textN.grid(row = 5,column = 6) 
	textN.config(state=DISABLED)
	
	textM = Text(gui, height=3, width=7)
	textM.insert(INSERT, '\n   M') 
	textM.grid(row = 5,column = 7) 
	textM.config(state=DISABLED)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx KEYBOARD xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	
	buttonQ = Button(gui, text=' Q ', fg='black', bg='light grey',
					command=lambda: start_main('Q', rotor1, rotor2, rotor3), height=3, width=7,)
	buttonQ.grid(row=6, column=0)
	buttonW = Button(gui, text=' W ', fg='black', bg='light grey',
					command=lambda: start_main('W', rotor1, rotor2, rotor3), height=3, width=7)
	buttonW.grid(row=6, column=1)
	buttonE = Button(gui, text=' E ', fg='black', bg='light grey',
					command=lambda: start_main('E', rotor1, rotor2, rotor3), height=3, width=7)
	buttonE.grid(row=6, column=2)
	buttonR = Button(gui, text=' R ', fg='black', bg='light grey',
					command=lambda: start_main('R', rotor1, rotor2, rotor3), height=3, width=7)
	buttonR.grid(row=6, column=3)
	buttonT = Button(gui, text=' T ', fg='black', bg='light grey',
					command=lambda: start_main('T', rotor1, rotor2, rotor3), height=3, width=7)
	buttonT.grid(row=6, column=4)
	buttonY = Button(gui, text=' Y ', fg='black', bg='light grey',
					command=lambda: start_main('Y', rotor1, rotor2, rotor3), height=3, width=7)
	buttonY.grid(row=6, column=5)
	buttonU = Button(gui, text=' U ', fg='black', bg='light grey',
					command=lambda: start_main('U', rotor1, rotor2, rotor3), height=3, width=7)
	buttonU.grid(row=6, column=6)
	buttonI = Button(gui, text=' I ', fg='black', bg='light grey',
					command=lambda: start_main('I', rotor1, rotor2, rotor3), height=3, width=7)
	buttonI.grid(row=6, column=7)
	buttonO = Button(gui, text=' O ', fg='black', bg='light grey',
					command=lambda: start_main('O', rotor1, rotor2, rotor3), height=3, width=7)
	buttonO.grid(row=6, column=8)
	buttonP = Button(gui, text=' P ', fg='black', bg='light grey',
					command=lambda: start_main('P', rotor1, rotor2, rotor3), height=3, width=7)
	buttonP.grid(row=6, column=9)
	# -------------------- NEW LINE -----------------------------#
	buttonA = Button(gui, text=' A ', fg='black', bg='light grey',
					command=lambda: start_main('A', rotor1, rotor2, rotor3), height=3, width=7)
	buttonA.grid(row=7, column=0)
	buttonS = Button(gui, text=' S ', fg='black', bg='light grey',
					command=lambda: start_main('S', rotor1, rotor2, rotor3), height=3, width=7)
	buttonS.grid(row=7, column=1)
	buttonD = Button(gui, text=' D ', fg='black', bg='light grey',
					command=lambda: start_main('D', rotor1, rotor2, rotor3), height=3, width=7)
	buttonD.grid(row=7, column=2)
	buttonF = Button(gui, text=' F ', fg='black', bg='light grey',
					command=lambda: start_main('F', rotor1, rotor2, rotor3), height=3, width=7)
	buttonF.grid(row=7, column=3)
	buttonG = Button(gui, text=' G ', fg='black', bg='light grey',
					command=lambda: start_main('G', rotor1, rotor2, rotor3), height=3, width=7)
	buttonG.grid(row=7, column=4)
	buttonH = Button(gui, text=' H ', fg='black', bg='light grey',
					command=lambda: start_main('H', rotor1, rotor2, rotor3), height=3, width=7)
	buttonH.grid(row=7, column=5)
	buttonJ = Button(gui, text=' J ', fg='black', bg='light grey',
					command=lambda: start_main('J', rotor1, rotor2, rotor3), height=3, width=7)
	buttonJ.grid(row=7, column=6)
	buttonK = Button(gui, text=' K ', fg='black', bg='light grey',
					command=lambda: start_main('K', rotor1, rotor2, rotor3), height=3, width=7)
	buttonK.grid(row=7, column=7)
	buttonL = Button(gui, text=' L ', fg='black', bg='light grey',
					command=lambda: start_main('L', rotor1, rotor2, rotor3), height=3, width=7)
	buttonL.grid(row=7, column=8)
	# -------------------- NEW LINE -----------------------------#
	buttonZ = Button(gui, text=' Z ', fg='black', bg='light grey',
					command=lambda: start_main('Z', rotor1, rotor2, rotor3), height=3, width=7)
	buttonZ.grid(row=8, column=1)
	buttonX = Button(gui, text=' X ', fg='black', bg='light grey',
					command=lambda: start_main('X', rotor1, rotor2, rotor3), height=3, width=7)
	buttonX.grid(row=8, column=2)
	buttonC = Button(gui, text=' C ', fg='black', bg='light grey',
					command=lambda: start_main('C', rotor1, rotor2, rotor3), height=3, width=7)
	buttonC.grid(row=8, column=3)
	buttonV = Button(gui, text=' V ', fg='black', bg='light grey',
					command=lambda: start_main('V', rotor1, rotor2, rotor3), height=3, width=7)
	buttonV.grid(row=8, column=4)
	buttonB = Button(gui, text=' B ', fg='black', bg='light grey',
					command=lambda: start_main('B', rotor1, rotor2, rotor3), height=3, width=7)
	buttonB.grid(row=8, column=5)
	buttonN = Button(gui, text=' N ', fg='black', bg='light grey',
					command=lambda: start_main('N', rotor1, rotor2, rotor3), height=3, width=7)
	buttonN.grid(row=8, column=6)
	buttonM = Button(gui, text=' M ', fg='black', bg='light grey',
					command=lambda: start_main('M', rotor1, rotor2, rotor3), height=3, width=7)
	buttonM.grid(row=8, column=7)
	# -------------------- NEW LINE -----------------------------#
	button_clear = Button(gui, text=' Clear ', fg='black', bg='light grey',
					command = clear, height=3, width=7)
	button_clear.grid(row=9, column=4)
	
	# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Plug Board xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	
	plugQ_image = PhotoImage(file = "plug_Q.png")
	plugQ = Button(gui, image = plugQ_image, command=lambda: update_connection_list('Q'), height=50, width=53)
	plugQ.grid(row=10, column=0)
	plugW_image = PhotoImage(file = "plug_W.png")
	plugW = Button(gui, image = plugW_image, command=lambda: update_connection_list('W'), height=50, width=53)
	plugW.grid(row=10, column=1)
	plugE_image = PhotoImage(file = "plug_E.png")
	plugE = Button(gui, image = plugE_image, command=lambda: update_connection_list('E'), height=50, width=53)
	plugE.grid(row=10, column=2)
	plugR_image = PhotoImage(file = "plug_R.png")
	plugR = Button(gui, image = plugR_image, command=lambda: update_connection_list('R'), height=50, width=53)
	plugR.grid(row=10, column=3)
	plugT_image = PhotoImage(file = "plug_T.png")
	plugT = Button(gui, image = plugT_image, command=lambda: update_connection_list('T'), height=50, width=53)
	plugT.grid(row=10, column=4)
	plugY_image = PhotoImage(file = "plug_Y.png")
	plugY = Button(gui, image = plugY_image, command=lambda: update_connection_list('Y'), height=50, width=53)
	plugY.grid(row=10, column=5)
	plugU_image = PhotoImage(file = "plug_U.png")
	plugU = Button(gui, image = plugU_image, command=lambda: update_connection_list('U'), height=50, width=53)
	plugU.grid(row=10, column=6)
	plugI_image = PhotoImage(file = "plug_I.png")
	plugI = Button(gui, image = plugI_image, command=lambda: update_connection_list('I'), height=50, width=53)
	plugI.grid(row=10, column=7)
	plugO_image = PhotoImage(file = "plug_O.png")
	plugO = Button(gui, image = plugO_image, command=lambda: update_connection_list('O'), height=50, width=53)
	plugO.grid(row=10, column=8)
	plugP_image = PhotoImage(file = "plug_P.png")
	plugP = Button(gui, image = plugP_image, command=lambda: update_connection_list('P'), height=50, width=53)
	plugP.grid(row=10, column=9)
	plugA_image = PhotoImage(file = "plug_A.png")
	plugA = Button(gui, image = plugA_image, command=lambda: update_connection_list('A'), height=50, width=53)
	plugA.grid(row=11, column=0)
	plugS_image = PhotoImage(file = "plug_S.png")
	plugS = Button(gui, image = plugS_image, command=lambda: update_connection_list('S'), height=50, width=53)
	plugS.grid(row=11, column=1)
	plugD_image = PhotoImage(file = "plug_D.png")
	plugD = Button(gui, image = plugD_image, command=lambda: update_connection_list('D'), height=50, width=53)
	plugD.grid(row=11, column=2)
	plugF_image = PhotoImage(file = "plug_F.png")
	plugF = Button(gui, image = plugF_image, command=lambda: update_connection_list('F'), height=50, width=53)
	plugF.grid(row=11, column=3)
	plugG_image = PhotoImage(file = "plug_G.png")
	plugG = Button(gui, image = plugG_image, command=lambda: update_connection_list('G'), height=50, width=53)
	plugG.grid(row=11, column=4)
	plugH_image = PhotoImage(file = "plug_H.png")
	plugH = Button(gui, image = plugH_image, command=lambda: update_connection_list('H'), height=50, width=53)
	plugH.grid(row=11, column=5)
	plugJ_image = PhotoImage(file = "plug_J.png")
	plugJ = Button(gui, image = plugJ_image, command=lambda: update_connection_list('J'), height=50, width=53)
	plugJ.grid(row=11, column=6)
	plugK_image = PhotoImage(file = "plug_K.png")
	plugK = Button(gui, image = plugK_image, command=lambda: update_connection_list('K'), height=50, width=53)
	plugK.grid(row=11, column=7)
	plugL_image = PhotoImage(file = "plug_L.png")
	plugL = Button(gui, image = plugL_image, command=lambda: update_connection_list('L'), height=50, width=53)
	plugL.grid(row=11, column=8)
	plugZ_image = PhotoImage(file = "plug_Z.png")
	plugZ = Button(gui, image = plugZ_image, command=lambda: update_connection_list('Z'), height=50, width=53)
	plugZ.grid(row=12, column=1)
	plugX_image = PhotoImage(file = "plug_X.png")
	plugX = Button(gui, image = plugX_image, command=lambda: update_connection_list('X'), height=50, width=53)
	plugX.grid(row=12, column=2)
	plugC_image = PhotoImage(file = "plug_C.png")
	plugC = Button(gui, image = plugC_image, command=lambda: update_connection_list('C'), height=50, width=53)
	plugC.grid(row=12, column=3)
	plugV_image = PhotoImage(file = "plug_V.png")
	plugV = Button(gui, image = plugV_image, command=lambda: update_connection_list('V'), height=50, width=53)
	plugV.grid(row=12, column=4)
	plugB_image = PhotoImage(file = "plug_B.png")
	plugB = Button(gui, image = plugB_image, command=lambda: update_connection_list('B'), height=50, width=53)
	plugB.grid(row=12, column=5)
	plugN_image = PhotoImage(file = "plug_N.png")
	plugN = Button(gui, image = plugN_image, command=lambda: update_connection_list('N'), height=50, width=53)
	plugN.grid(row=12, column=6)
	plugM_image = PhotoImage(file = "plug_M.png")
	plugM = Button(gui, image = plugM_image, command=lambda: update_connection_list('M'), height=50, width=53)
	plugM.grid(row=12, column=7)
	plugCL_image = PhotoImage(file = "plug_CL.png")
	plugCL = Button(gui, image = plugCL_image, command=lambda: clear_plugboard(), height=50, width=53)
	plugCL.grid(row=13, column=4)
	
	plugQ.image = plugQ_image	# keep a reference to the images to prevent garbage collection
	plugW.image = plugW_image
	plugE.image = plugE_image
	plugR.image = plugR_image
	plugT.image = plugT_image
	plugY.image = plugY_image
	plugU.image = plugU_image
	plugI.image = plugI_image
	plugO.image = plugO_image
	plugP.image = plugP_image
	plugA.image = plugA_image
	plugS.image = plugS_image
	plugD.image = plugD_image
	plugF.image = plugF_image
	plugG.image = plugG_image
	plugH.image = plugH_image
	plugJ.image = plugJ_image
	plugK.image = plugK_image
	plugL.image = plugL_image
	plugZ.image = plugZ_image
	plugX.image = plugX_image
	plugC.image = plugC_image
	plugV.image = plugV_image
	plugB.image = plugB_image
	plugN.image = plugN_image
	plugM.image = plugM_image
	plugCL.image = plugCL_image
	
	# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Rotor Position xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
	rotor_label = Text(gui, height=3, width=10)
	rotor_label.insert(INSERT, 'Rotor\nPositions:') 
	rotor_label.grid(row = 3,column = 13) 
	rotor_label.config(state=DISABLED, bg = 'white')
	
	rotor_position1 = Text(gui, height=3, width=7)
	rotor_position1.insert(INSERT, '\n   ' + str(rotor1.position))
	rotor_position1.grid(row = 3,column = 14) 
	rotor_position1.config(state=DISABLED, bg = 'white')
	
	rotor_position2 = Text(gui, height=3, width=7)
	rotor_position2.insert(INSERT, '\n   ' + str(rotor2.position)) 
	rotor_position2.grid(row = 4,column = 14) 
	rotor_position2.config(state=DISABLED, bg = 'white')
	
	rotor_position3 = Text(gui, height=3, width=7)
	rotor_position3.insert(INSERT, '\n   ' + str(rotor3.position)) 
	rotor_position3.grid(row = 5,column = 14) 
	rotor_position3.config(state=DISABLED, bg = 'white')
	
	# start the GUI
	plug1 = Label(gui, text = connection_list[0], height=3, width=6) # makes plugboard show up before pressing
	plug1.grid(row=6, column=11, rowspan=1)
	plug2 = Label(gui, text = connection_list[1], height=3, width=6)
	plug2.grid(row=6, column=12, rowspan=1)
	plug3 = Label(gui, text = connection_list[2], height=3, width=6)
	plug3.grid(row=7, column=11, rowspan=1)
	plug4 = Label(gui, text = connection_list[3], height=3, width=6)
	plug4.grid(row=7, column=12, rowspan=1)
	plug5 = Label(gui, text = connection_list[4], height=3, width=6)
	plug5.grid(row=8, column=11, rowspan=1)
	plug6 = Label(gui, text = connection_list[5], height=3, width=6)
	plug6.grid(row=8, column=12, rowspan=1)
	plug7 = Label(gui, text = connection_list[6], height=3, width=6)
	plug7.grid(row=9, column=11, rowspan=1)
	plug8 = Label(gui, text = connection_list[7], height=3, width=6)
	plug8.grid(row=9, column=12, rowspan=1)
	plug9 = Label(gui, text = connection_list[8], height=3, width=6)
	plug9.grid(row=10, column=11, rowspan=1)
	plug10 = Label(gui, text = connection_list[9], height=3, width=6)
	plug10.grid(row=10, column=12, rowspan=1)
	plug11 = Label(gui, text = connection_list[10], height=3, width=6)
	plug11.grid(row=11, column=11, rowspan=1)
	plug12 = Label(gui, text = connection_list[11], height=3, width=6)
	plug12.grid(row=11, column=12, rowspan=1)
	plug13 = Label(gui, text = connection_list[12], height=3, width=6)
	plug13.grid(row=12, column=11, rowspan=1)
	
	gui.mainloop()


  
