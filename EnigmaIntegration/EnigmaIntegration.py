#Declairing Letter As a Global Variable

letter_passed = "X"

##Applied Programming Enigma Keyboard
def main():
    message = []
    
    while True:
        # Ask user for a Letter
        letter_passed = input("Please enter the letter you wish to send: ").upper() #upper forces letters to be uppercase after entry
        
        message.append(letter_passed)
        
        # Display current message
        print("The message so far is: ")
        print(" ".join(message)) #Print message with space between each letter
        
        # Ask if complete?
        while True: #While loop to continue asking until Y is entered 
            choice = input("Is your message complete (Y/N): ").upper() #Force Uppercase 
            
            if choice != 'Y' and choice != 'N': #Anything other than a Y or N is invalid
                print("Invalid choice. Please enter Y or N.")
            else:
                break

        # Yes is chosen final message is printed. 
        if choice == 'Y': 
            print("Message has been sent. The final message is: ")
            print(" ".join(message))
            return 
        
    letter_passed = message
    return letter_passed    

print (letter_passed) 

if __name__ == "__main__":
    main()

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

    test3 = function_change("A")
    print(test3)
    

plugbrd_loop() 
print ("Rotors")

print (letter_passed) 
plugbrd_loop() 
# print (test2)


    

