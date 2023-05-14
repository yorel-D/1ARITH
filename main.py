import random
import re


def enlever_ponctuation(texte):
    return re.sub("[^A-Za-z]", '', texte).upper()


def generer_alphabet_melange():
    alphabet = [chr(i) for i in range(65, 91)]
    random.shuffle(alphabet)
    return ''.join(alphabet)


def creer_cylindre(nom_fichier, n):
    with open(nom_fichier, "w") as fichier:
        for i in range(n):
            fichier.write(generer_alphabet_melange() + "\n")


def charger_cylindre(nom_fichier):
    resultat = {}
    with open(nom_fichier) as fichier:
        lignes = fichier.read().splitlines()
        for i in range(len(lignes)):
            resultat[i+1] = lignes[i]
    return resultat


def cle_valide(cle, n):
    for x in cle:
        if x < 1 or x > n:
            return False
    return True


def creer_cle(n):
    cle = []
    for x in range(0, 27):
        cle += [int(random.randrange(1, n))]
    return cle


def trouver_position(lettre, alphabet):
    lettre_majuscule = lettre.upper()
    position = 0
    for x in alphabet:
        if x == lettre_majuscule:
            return position
        else:
            position += 1


def decalage(i):
    return (i + 6) % 26


def chiffrer_lettre(lettre, alphabet):
    return alphabet[decalage(trouver_position(lettre, alphabet))]


def chiffrer_texte(cylindre, cle, texte):
    if not cle_valide(cle, len(cylindre)):
        return 'Error'
    texte_chiffre = [cylindre[cle[i]][decalage(trouver_position(enlever_ponctuation(texte)[i], cylindre[cle[i]]))] for i in range(len(cylindre))]
    return ''.join(texte_chiffre)


def dechiffrer_texte(cylindre, cle, texte):
    if not cle_valide(cle, len(cylindre)):
        return 'Error'
    texte_dechiffre = [cylindre[cle[i]][(trouver_position(enlever_ponctuation(texte)[i], cylindre[cle[i]])) - 6] for i in range(len(cylindre) - 1)]
    return ''.join(texte_dechiffre)

