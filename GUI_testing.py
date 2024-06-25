from tkinter import *
expression = ""

def press(letter):
	# point out the global expression variable and set it
	global expression
	expression = expression + str(letter)
	equation.set(expression)

def clear():
	global expression
	expression = ""
	equation.set(expression)

# Driver code	
if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="brown")
	gui.title("Enigma Keyboard")
	gui.geometry("589x350")
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation)
	expression_field.grid(columnspan=10, ipadx=70)
	equation.set('enter your message')
	buttonQ = Button(gui, text=' Q ', fg='black', bg='light grey',
					command=lambda: press('Q'), height=3, width=7,)
	buttonQ.grid(row=3, column=0)
	buttonW = Button(gui, text=' W ', fg='black', bg='light grey',
					command=lambda: press('W'), height=3, width=7)
	buttonW.grid(row=3, column=1)
	buttonE = Button(gui, text=' E ', fg='black', bg='light grey',
					command=lambda: press('E'), height=3, width=7)
	buttonE.grid(row=3, column=2)
	buttonR = Button(gui, text=' R ', fg='black', bg='light grey',
					command=lambda: press('R'), height=3, width=7)
	buttonR.grid(row=3, column=3)
	buttonT = Button(gui, text=' T ', fg='black', bg='light grey',
					command=lambda: press('T'), height=3, width=7)
	buttonT.grid(row=3, column=4)
	buttonY = Button(gui, text=' Y ', fg='black', bg='light grey',
					command=lambda: press('Y'), height=3, width=7)
	buttonY.grid(row=3, column=5)
	buttonU = Button(gui, text=' U ', fg='black', bg='light grey',
					command=lambda: press('U'), height=3, width=7)
	buttonU.grid(row=3, column=6)
	buttonI = Button(gui, text=' I ', fg='black', bg='light grey',
					command=lambda: press('I'), height=3, width=7)
	buttonI.grid(row=3, column=7)
	buttonO = Button(gui, text=' O ', fg='black', bg='light grey',
					command=lambda: press('O'), height=3, width=7)
	buttonO.grid(row=3, column=8)
	buttonP = Button(gui, text=' P ', fg='black', bg='light grey',
					command=lambda: press('P'), height=3, width=7)
	buttonP.grid(row=3, column=9)
	# -------------------- NEW LINE -----------------------------#
	buttonA = Button(gui, text=' A ', fg='black', bg='light grey',
					command=lambda: press('A'), height=3, width=7)
	buttonA.grid(row=4, column=0)
	buttonS = Button(gui, text=' S ', fg='black', bg='light grey',
					command=lambda: press('S'), height=3, width=7)
	buttonS.grid(row=4, column=1)
	buttonD = Button(gui, text=' D ', fg='black', bg='light grey',
					command=lambda: press('D'), height=3, width=7)
	buttonD.grid(row=4, column=2)
	buttonF = Button(gui, text=' F ', fg='black', bg='light grey',
					command=lambda: press('F'), height=3, width=7)
	buttonF.grid(row=4, column=3)
	buttonG = Button(gui, text=' G ', fg='black', bg='light grey',
					command=lambda: press('G'), height=3, width=7)
	buttonG.grid(row=4, column=4)
	buttonH = Button(gui, text=' H ', fg='black', bg='light grey',
					command=lambda: press('H'), height=3, width=7)
	buttonH.grid(row=4, column=5)
	buttonJ = Button(gui, text=' J ', fg='black', bg='light grey',
					command=lambda: press('J'), height=3, width=7)
	buttonJ.grid(row=4, column=6)
	buttonK = Button(gui, text=' K ', fg='black', bg='light grey',
					command=lambda: press('K'), height=3, width=7)
	buttonK.grid(row=4, column=7)
	buttonL = Button(gui, text=' L ', fg='black', bg='light grey',
					command=lambda: press('L'), height=3, width=7)
	buttonL.grid(row=4, column=8)
	# -------------------- NEW LINE -----------------------------#
	buttonZ = Button(gui, text=' Z ', fg='black', bg='light grey',
					command=lambda: press('Z'), height=3, width=7)
	buttonZ.grid(row=5, column=1)
	buttonX = Button(gui, text=' X ', fg='black', bg='light grey',
					command=lambda: press('X'), height=3, width=7)
	buttonX.grid(row=5, column=2)
	buttonC = Button(gui, text=' C ', fg='black', bg='light grey',
					command=lambda: press('C'), height=3, width=7)
	buttonC.grid(row=5, column=3)
	buttonV = Button(gui, text=' V ', fg='black', bg='light grey',
					command=lambda: press('V'), height=3, width=7)
	buttonV.grid(row=5, column=4)
	buttonB = Button(gui, text=' B ', fg='black', bg='light grey',
					command=lambda: press('B'), height=3, width=7)
	buttonB.grid(row=5, column=5)
	buttonN = Button(gui, text=' N ', fg='black', bg='light grey',
					command=lambda: press('N'), height=3, width=7)
	buttonN.grid(row=5, column=6)
	buttonM = Button(gui, text=' M ', fg='black', bg='light grey',
					command=lambda: press('M'), height=3, width=7)
	buttonM.grid(row=5, column=7)
	# -------------------- NEW LINE -----------------------------#
	button_clear = Button(gui, text=' Clear ', fg='black', bg='light grey',
					command = clear, height=3, width=7)
	button_clear.grid(row=6, column=4)
	# start the GUI
	gui.mainloop()