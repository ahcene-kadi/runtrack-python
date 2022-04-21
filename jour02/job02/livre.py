#from auteur import Auteur

class Livre(): 
    def __init__(self, titre, Auteur):
        
        self.titre = titre
        self.auteur = Auteur
        
    def printTitre(self): 
        print(self.titre)


# t = Livre("Diego", "prince", "", "LOL")
# t.printTitre()
# # t.SePresenter()
# # t.ecrireUnLivre()
# # t.ecrireUnLivre()
# # t.listerOeuvre()




# # thislist = ["apple", "banana", "cherry"]
# # print(thislist)
# # fruit = input("nouveau fruit")
# # print(fruit)
# # thislist.append(fruit)
# # print(thislist)