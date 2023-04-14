import argparse

# Fonction qui lit un fichier et retourne son contenu sous forme de liste de caractères
def lire_fichier(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        contenu = fichier.read()
    liste_caracteres = [caractere for caractere in contenu]
    return liste_caracteres

# Fonction qui chiffre un message avec la méthode de Vigenère
def chiffrement_vigenere(message, cle):
    resultat = ""
    for i, caractere in enumerate(message):
        cle_caractere = cle[i % len(cle)]
        resultat += chr(((ord(caractere) + ord(cle_caractere) - 2 * ord('A')) % 26) + ord('A'))
    return resultat

# Fonction qui déchiffre un message chiffré avec la méthode de Vigenère
def dechiffrement_vigenere(message_chiffre, cle):
    resultat = ""
    for i, caractere in enumerate(message_chiffre):
        cle_caractere = cle[i % len(cle)]
        resultat += chr(((ord(caractere) - ord(cle_caractere) + 26) % 26) + ord('A'))
    return resultat


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--chiffrement", help="Permet de spécifier l'action de chiffrement", action="store_true")
parser.add_argument("-d", "--dechiffrement", help="Permet de spécifier l'action de déchiffrement", action="store_true")
parser.add_argument('fichier', help='Le nom du fichier à chiffrer/déchiffrer')
parser.add_argument('cle', help='La clé pour le chiffrement Vigenère')
parser.add_argument('destination', help='Le nom du fichier de destination')
args = parser.parse_args()

if args.chiffrement:
    try:
        message = lire_fichier(args.fichier)
        cle = args.cle
        message_chiffre = chiffrement_vigenere(message, cle)
        with open(args.destination, 'w') as fichier:
            fichier.write(message_chiffre)
        print(f"Le message a été chiffré et enregistré dans {args.destination}")

    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé")

elif args.dechiffrement:
    try:
        with open(args.fichier, 'r') as fichier:
            message_chiffre = fichier.read()
        cle = args.cle
        message_dechiffre = dechiffrement_vigenere(message_chiffre, cle)
        with open(args.destination, 'w') as fichier:
            fichier.write(message_dechiffre)
        print(f"Le message a été déchiffré et enregistré dans {args.destination}")

    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé")
else:
    print("Veuillez spécifier une action à effectuer (-c/--chiffrement ou -d/--dechiffrement).")
