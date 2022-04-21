class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
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


    def SePresenter(self):  
        print(self.nom + ' ' + self.prenom)

class Livre: 
    def __init__(self, titre, Auteur):
        self.titre = titre
        self.auteur = Auteur 

class Auteur(Personne):
    def __init__(self, nom, prenom, oeuvre):
        self.nom = nom
        self.prenom = prenom
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)

A1 = Auteur("Hugo", "Victor")
 
L1 = Livre("Miserables", A1)

print(L1.auteur.prenom)