import string
from logging import exception
from string import ascii_lowercase,punctuation,digits


def encrypt(original_text,shift_amount):
    alphabet = list(ascii_lowercase)

    message_list = list(original_text)
    encrypted_text = ""

    for letter in message_list:
        if letter not in alphabet:
            encrypted_text += letter
        else:
            index = (alphabet.index(letter)+shift) % len(alphabet)
            encrypted_text += alphabet[index]

    print(f"Here is the encrypted message: {encrypted_text}")
def decrypt(original_text,shift_amount):
    alphabet = list(ascii_lowercase)
    message_list = list(original_text)
    decrypted_text = ""

    for letter in message_list:
        if letter not in alphabet:
            decrypted_text += letter
        else:
            index = (alphabet.index(letter) - shift) % len(alphabet)
            decrypted_text += alphabet[index]

    print(f"Here is the encrypted message: {decrypted_text}")
def ceaser(original_text, shift_amount, encode_or_decode):
    output = ""
    message_list = list(original_text)
    alphabet = list(ascii_lowercase)

    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in message_list:
        if letter not in alphabet:
            output += letter
        else:
            index = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output += alphabet[index]

    print(f"Here is the {encode_or_decode}d message: {output}")

start = True
while  start:

    text = input("enter message:\n").lower()
    shift = int(input("Enter the shift number:\n"))
    direction = input("enter encode or decode: ")
    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    program = input("restart the cipher program? type yes or No: ").lower()
    if program == "yes":
        start = True
    elif program == 'no':
        print("Goodbye")
        start = False
    else:
        print("Entered incorrect text, initiate ceaser program again by providing data to the asked questions")


