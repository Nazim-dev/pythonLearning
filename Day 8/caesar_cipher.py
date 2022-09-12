import cipher_art

print(cipher_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    word = ""
    if shift > 26 :
        shift = round(shift / 5)

    for item in text:

        for char in item:

            if char in alphabet:

                char_index = alphabet.index(char)
                if direction == "decode":
                    char_index -= shift
                    if char_index < 0:
                        char_index = char_index + 26
                    word += alphabet[char_index]

                elif direction == "encode":
                    char_index += shift
                    if char_index > 25:
                        char_index = char_index - 26
                    word += alphabet[char_index]
            else:
                word += char
        word += " "

    print(f"The {direction}d word is {word}")

choice = True
while choice is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    sentence = text.split()
    caesar(sentence, shift, direction)

    choice = input("Would you like to continue? type 'Yes' or 'No' \n").lower()
    if choice == "No":
        choice = False
    else:
        choice = True


