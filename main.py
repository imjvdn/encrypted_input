def caesar_cipher(text, shift):
    if not isinstance(shift, int):
        return "Error: shift value must be an integer"
    encrypted_text = ""
    for ch in text:
        if ch.isalpha():
            shift_ch = chr((ord(ch) - 65 + shift) % 26 + 65)
            encrypted_text += shift_ch
        else:
            encrypted_text += ch
    return encrypted_text

text = input("Enter some text to encrypt: ")

try:
    shift = int(input("Enter a shift value (an integer): "))
except ValueError:
    print("Error: shift value must be an integer")
    shift = None

if shift is not None:
    encrypted_text = caesar_cipher(text, shift)
    print(f"Encrypted text: {encrypted_text}")
