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


def run(letter, rotor1, rotor2, rotor3, reflector):
    letter = rotor1.forward(letter)
    letter = rotor2.forward(letter)
    letter = rotor3.forward(letter)
    letter = reflector.forward(letter)
    letter = rotor3.backward(letter)
    letter = rotor2.backward(letter)
    letter = rotor1.backward(letter)
    return letter


def encrypt_message(message, rotor1, rotor2, rotor3, reflector):
    encrypted_message = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for char in message:
            letter = alphabet.index(char)
            encrypted_letter = run(letter, rotor1, rotor2, rotor3, reflector)
            encrypted_message += alphabet[encrypted_letter]
            
            # Rotate rotors after each letter
            rotor1.rotate()
            if rotor1.position == 0:
                rotor2.rotate()
            if rotor1.position == 0 and rotor2.position == 0:
                rotor3.rotate()
        

    return encrypted_message


def bombe_attack(ciphertext, known_plaintext, rotor1, rotor2, rotor3, reflector):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        for j in range(26):
            for k in range(26):
                rotor1.set_position(i)
                rotor2.set_position(j)
                rotor3.set_position(k)
                
                decrypted_message = encrypt_message(ciphertext, rotor1, rotor2, rotor3, reflector)
                
                if known_plaintext in decrypted_message:
                    return i, j, k, decrypted_message
    return None


# Rotor and Reflector configurations
array1 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
array2 = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]
array3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
reflect_arr = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

rotor1 = Rotor(array1)
rotor2 = Rotor(array2)
rotor3 = Rotor(array3)
reflector = Rotor(reflect_arr)

# Example ciphertext and known plaintext
ciphertext = "SNMKGGSTZZUGARLV"
known_plaintext = "WETTERVORHERSAGE"

# Run Bombe attack
result = bombe_attack(ciphertext, known_plaintext, rotor1, rotor2, rotor3, reflector)

if result:
    position1, position2, position3, decrypted_message = result
    print(f"Rotor positions found: Rotor1={position1}, Rotor2={position2}, Rotor3={position3}")
    print(f"Decrypted message: {decrypted_message}")
else:
    print("No matching rotor positions found.")

