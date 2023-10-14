"encryption and decryption of the fortune cookie database"
import random
import csv

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = ((char_code - ord('a') + shift) % 26) + ord('a')
            if is_upper:
                char_code = chr(char_code).upper()
            else:
                char_code = chr(char_code)
            encrypted_text += char_code
        else:
            encrypted_text += char  # Preserve non-alphabet characters
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = ((char_code - ord('a') - shift) % 26) + ord('a')
            if is_upper:
                char_code = chr(char_code).upper()
            else:
                char_code = chr(char_code)
            decrypted_text += char_code
        else:
            decrypted_text += char  # Preserve non-alphabet characters
    return decrypted_text

def fetch_value_from_csv(csv_filename):
    try:
        # Check if the random number is within the valid range
        random_number = random_no()
        if 1 <= random_number <= 1019:
            with open(csv_filename, mode='r', newline='') as file:
                csv_reader = csv.reader(file)
                # Subtract 1 from the random number since Python uses 0-based indexing
                row_number = random_number - 1
                for i, row in enumerate(csv_reader):
                    if i == row_number:
                        return row
            return None  # Random number was out of range
        else:
            return None  # Random number is out of the valid range
    except FileNotFoundError:
        return None  # CSV file not found or couldn't be opened

def random_no():
    random_number = random.randint(2, 1018)
    return random_number
