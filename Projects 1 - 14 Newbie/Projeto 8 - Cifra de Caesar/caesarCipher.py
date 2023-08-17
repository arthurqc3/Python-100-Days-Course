from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo()
ceasar_Cipher = True


def ceasar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(plain_text, shift_amount):
        plain_text = list(plain_text)

        for num, letter in enumerate(plain_text):
            if letter in alphabet:
                if alphabet.index(letter) + shift_amount > (len(alphabet) - 1):
                    indexAlphabet = (alphabet.index(letter) + shift_amount) - (len(alphabet) - 1)
                    plain_text[num] = alphabet[indexAlphabet - 1]
                else:
                    plain_text[num] = alphabet[alphabet.index(letter) + shift_amount]

        encryptText = ''.join(plain_text)
        print(f"You encrypt code: {encryptText}")

    def decrypt(plain_text, shift_amount):
        plain_text = list(plain_text)

        for num, letter in enumerate(plain_text):
            if letter in alphabet:
                if alphabet.index(letter) + shift_amount > (len(alphabet) - 1):
                    indexAlphabet = (alphabet.index(letter) - shift_amount) - (len(alphabet) - 1)
                    plain_text[num] = alphabet[indexAlphabet - 1]
                else:
                    plain_text[num] = alphabet[alphabet.index(letter) - shift_amount]

        decryptText = ''.join(plain_text)
        print(f"You decrypt code: {decryptText}")

    if direction == 'encode':
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == 'decode':
        decrypt(plain_text=text, shift_amount=shift)

while ceasar_Cipher == True:
    ceasar()
    again = input("Do you want to use again? type Yes or No").lower()

    if again == 'no':
        ceasar_Cipher = False
    elif again == 'yes':
        continue
    else:
        ceasar_Cipher = False
