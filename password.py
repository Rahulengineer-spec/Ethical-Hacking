import itertools
import json

def generate_passwords(characters, length):
    passwords = []

    combinations = itertools.permutations(characters, length)
    passwords.extend(''.join(combination) for combination in combinations)

    return passwords

def save_passwords_as_json(passwords, filename):
    with open(filename, 'w') as file:
        json.dump(passwords, file)

# Example usage:
character_string = "Lata203@"
password_length = 9
passwords = generate_passwords(character_string, password_length)
save_passwords_as_json(passwords, "passwords.json")
