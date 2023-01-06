def caesar_cipher(text, shift):
    encrypted_text = ""
    for ch in text:
        if ch.isalpha():
            shift_ch = chr((ord(ch) - 65 + shift) % 26 + 65)
            encrypted_text += shift_ch
        else:
            encrypted_text += ch
    return encrypted_text

text = input("Enter some text to encrypt: ")

# Hardcode the shift value to 3
shift = 3

encrypted_text = caesar_cipher(text, shift)

print(f"Encrypted text: {encrypted_text}")
