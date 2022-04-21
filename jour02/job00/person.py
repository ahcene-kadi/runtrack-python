class Person:
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