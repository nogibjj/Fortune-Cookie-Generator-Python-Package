"encryption and decryption of the fortune cookie database"

def encrypt(text, shift):
    result = ''
    for c in text:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            offset = (ord(c) - base + shift) % 26
            result += chr(base + offset)
        else:
            result += c
    return result

def decrypt(text, shift):
    return encrypt(text, 26 - shift)
