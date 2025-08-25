def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - 65 + s) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - 97 + s) % 26 + 97)

        # Leave non-alphabetic characters unchanged
        else:
            result += char

    return result

# check the above function
text = input("Enter text to be encrypted: ")
en_s = int(input("Enter shift number (1-25): "))
print("Text  : " + text)
print("Shift : ", en_s)
print("Cipher: " + encrypt(text, en_s))

choice = int(input("to decrypt, press: 1 \nto exit, press :0\n"))
if choice == 1:
    text = input("Enter text to be decrypted: ")
    print("Cipher: " + text)
    print("Shift : ", en_s)
    print("Text  : " + encrypt(text, 26 - en_s))

else:
    exit()