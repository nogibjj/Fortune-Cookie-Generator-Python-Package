"encryption and decryption of the fortune cookie database"
import random
import csv

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
    random_number = random.randint(1, 1019)
    return random_numer
