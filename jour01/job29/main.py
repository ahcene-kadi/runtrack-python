note_eleve = int(input("Entre ta note : "))


def correction(note_eleve):

    if note_eleve >= 40 and (note_eleve +2) % 5 ==0 :
        return print("Bravo tu as réussi le test! J'arrondi ta note a",note_eleve+2) 
    elif  note_eleve >= 40 :
        return print("Tu as reussi le test jeune palawan!")
    else:
        return print("Tu as échoué au test jeune palawan!")
    
correction(note_eleve)
