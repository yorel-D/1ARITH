import random
import string

def random_string():
    return ''.join(random.sample(string.ascii_uppercase, 26))
def Creation_du_cylindre(filename, n):
    with open(filename, 'w') as f:
        for _ in range(n):
            f.write(random_string() + '\n')
def lecture_du_cylindre(filename):
    cylinder = {}
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines(), start=1):
            cylinder[i] = line.strip()
    return cylinder
def is_permutation(lst, n):
    return sorted(lst) == list(range(1, n + 1))
def generate_permutation(n):
    return random.sample(range(1, n + 1), n)
def encrypt_letter(letter, alphabet, shift=6):
    index = (alphabet.index(letter) + shift) % 26
    return alphabet[index]
def remove_spaces(text):
    return text.replace(" ", "")

def jefferson_encrypt(Mot, cylinder, key, shift=6):
    text=remove_spaces(Mot)
    encrypted_text = ''
    for i, letter in enumerate(text):
        if letter.isalpha():
            alphabet = cylinder[key[i % len(key)]]
            encrypted_text += encrypt_letter(letter.upper(), alphabet, shift)
        else:
            encrypted_text += letter
    return encrypted_text

def jefferson_decrypt(text, cylinder, key, shift=-6):
    return jefferson_encrypt(text, cylinder, key, shift)
cylinder = lecture_du_cylindre("cylinderWiki.txt")
key = [7, 9, 5, 10, 1, 6, 3, 8, 2, 4]
encrypted_text = jefferson_encrypt("RetreatNow", cylinder, key)
print(encrypted_text)  # Doit afficher "OMKEGWPDFN"

cylinder_1ARIT_MP = lecture_du_cylindre("1ARIT-MP.txt")
key_1ARIT_MP = [12, 16, 29, 6, 33, 9, 22, 15, 20, 3, 1, 30, 32, 36, 19, 10, 35, 27, 25, 26, 2, 18, 31, 14, 34, 17, 23, 7, 8, 21, 4, 13, 11, 24, 28, 5]
decrypted_text = jefferson_decrypt("GRMYSGBOAAMQGDPEYVWLDFDQQQZXXVMSZFS", cylinder_1ARIT_MP, key_1ARIT_MP)
print(decrypted_text)  # Doit afficher le texte déchiffré
