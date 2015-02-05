from datetime import date, datetime
import sys

'''
TP Python // TP#1

@author: Antoine
'''
def helloworld():
    print("helloworld !")

'''
    classe personne
'''
class Personne(object):
    def __init__(self, pPrenom, pNom, pDateNaissance):
        self._nom = pNom
        self._prenom = pPrenom
        self._dateNaissance = pDateNaissance

    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, value):
        self._nom = value
    @property
    def prenom(self):
        return self._prenom
    @prenom.setter
    def prenom(self, value):
        self._prenom = value
    @property
    def dateNaissance(self):
        return self._dateNaissance
    @dateNaissance.setter
    def dateNaissance(self, value):
        self._dateNaissance = value

    def __repr__(self):
        return "{} {} ne(e) le {}".format(self._nom, self._prenom, self._dateNaissance)

    def __str__(self):
        return str(self._prenom + " " + self._nom + " : a " + str(self.getAge()) + " ans.")

    def getAge(self):
        try:
            datePersTmp = datetime.strptime(self._dateNaissance.lstrip().rstrip(), "%d/%m/%Y")
        except Exception as e:
            print("Erreur de lecture de la date :"+str(e))
            datePersTmp = datetime.now()
        dateNow = datetime.now()
        return int((dateNow-datePersTmp).days / 365.25)

'''
    lecture du fichier CSV
'''
def lireFichierCSV(nomFichier):
    lstRsl = []
    try:
        with open(nomFichier,'r') as monFichier:
            for ligne in monFichier:
           #     print("oui "+str(ligne))
                ligneLue = ligne.rstrip('\n').split(";")
                if len(ligneLue) == 3:
                    lstRsl.append(Personne(ligneLue[0],ligneLue[1],ligneLue[2]))
    except IOError:
        print("Error: Impossible de lire le fichier {}".format(nomFichier))  
    return lstRsl

'''
    écriture du fichier CSV
'''
def ecrireFichierCSV(nomFichier, pLstPersonnes):
    try:
        monFichier = open(nomFichier,'w')
        for pers in pLstPersonnes:
            monFichier.write("{};{};{}\n".format(pers.nom, pers.prenom, pers.dateNaissance))
    except IOError:
        print("Error: Impossible d'ecrire le fichier {}".format(nomFichier))  
    return

'''
    Boucle principale (main)
'''
if __name__ == '__main__':
    helloworld()
    print(),
    # arv[0] est le script python lui même, donc ici on controle juste s'il y a un ou deux paramètres à suivre
    if len(sys.argv) >= 3:
        fichierSortie = sys.argv[2]
    else:
        fichierSortie = "tp1_new.csv"
    if len(sys.argv) >= 2:
        fichierEntree = sys.argv[1]
    else:
        fichierEntree = "tp1.csv"

    lstPersonnes = lireFichierCSV(fichierEntree)
    print("\n=== Liste des personnes :")
    for pers in lstPersonnes:
        print(str(pers))
    print("\najoute une nouvelle personne (Marie Valon).")
    print("\najoute une nouvelle personne (saisie utilisateur) :")
    unnom = input("entrez le nom de la nouvelle personne > ")
    unprenom = input("entrez le prenom de la nouvelle personne > ")
    unedate = input("entrez la date de naissance la nouvelle personne (format 10/10/1980) > ")
    lstPersonnes.append(Personne(unnom, unprenom, unedate))
    lstPersonnes.append(Personne("Marie", "Valon", "10/10/1986"))
    print("supprime la 2nde personne de la liste.")
    del lstPersonnes[1]  # supprime un objet -- variante : lstPersonnes.pop(1)
    print("\n=== Liste des personnes :")
    for pers in lstPersonnes:
        print(str(pers))
    print("\n=== Enregistre un nouveau fichier CSV :")
    ecrireFichierCSV(fichierSortie, lstPersonnes)

