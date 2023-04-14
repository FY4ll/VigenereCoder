import argparse

def getresult(filename):
    with open(filename, 'r') as file:
        x = file.read()
    xarray = [char for char in x]

    return xarray

def vigenere_encrypt(message, key):
    result = ""
    for i, char in enumerate(message):
        key_char = key[i % len(key)]
        result += chr(((ord(char) + ord(key_char) - 2 * ord('A')) % 26) + ord('A'))
    return result

def vigenere_decrypt(message, key):
    result = ""
    for i, char in enumerate(message):
        key_char = key[i % len(key)]
        result += chr(((ord(char) - ord(key_char) + 26) % 26) + ord('A'))
    return result


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--chiffrement", help="Permet de spécifier l'action de chiffrement", action="store_true")
parser.add_argument("-d", "--déchiffrement", help="Permet de spécifier l'action de déchiffrement", action="store_true")
parser.add_argument('Fichier', help='Le nom du fichier à chiffrer/déchiffrer')
parser.add_argument('Clé', help='La clé pour le chiffrement Vigenère')
parser.add_argument('destination', help='Le nom du fichier de destination')
args = parser.parse_args()

if args.chiffrement:
    try:
        message = getresult(args.Fichier)
        key = args.Clé
        encrypted_message = vigenere_encrypt(message, key)
        with open(args.destination, 'w') as file:
            file.write(encrypted_message)
        print(f"Le message a été chiffré et enregistré dans {args.destination}")

    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé")

elif args.déchiffrement:
    try:
        with open(args.Fichier, 'r') as file:
            message = file.read()
        key = args.Clé
        decrypted_message = vigenere_decrypt(message, key)
        with open(args.destination, 'w') as file:
            file.write(decrypted_message)
        print(f"Le message a été déchiffré et enregistré dans {args.destination}")

    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé")
else:
    print("Veuillez spécifier une action à effectuer (-c/--chiffrement ou -d/--déchiffrement).")
