#implemrnting if the function
def welcome():
    print('Welcome to Caesar Cipher')
    print('This programs encrypts and decrypts text with Caesar Cipher')
welcome()


# function of enter_message
def enter_message():
    choice = input("Would you like to encrypt or decrypt? (e/d): ")
    text = input("Enter a message: ")
    key = int(input("Enter a number to shift betewen(1-26): "))
    return choice, text, key

# implementing the encrypt() function

def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted = chr((ord(char) + key - 65) % 26 + 65)
            ciphertext += shifted
        else:
            ciphertext += char
    return ciphertext.upper()


# implementing the decrypt()function

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = chr((ord(char) - key - 65) % 26 + 65)
            plaintext += shifted
        else:
            plaintext += char
    return plaintext.upper()

while True:
    choice, text, key = enter_message()
    if choice == 'e':
        ciphertext = encrypt(text, key)
        print("Encrypted message:", ciphertext)
    elif choice == 'd':
        plaintext = decrypt(text, key)
        print("Decrypted message:", plaintext)
    else:
        print("Invalid choice.")
    cont = input("Would you like to continue? (y/n): ")
    if cont.lower() != 'y':
        break
print('Thank you')
