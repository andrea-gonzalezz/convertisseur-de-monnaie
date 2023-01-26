import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import StringVar


#  ****************INTERFACE GRAPHIQUE **********************


#COULEURS
bleu_clair = "#B8CBD0"
vert_clair = "#C9E3CC"
kaki = "#B0B9A8"
vert = "#606C5A"
vert_fonce = "#424340"

#Polices d'écriture et tailles


# Création de la fenêtre
window = tk.Tk()
window.title("Convertisseur de devices")
window.geometry('300x400')
window.iconbitmap("currencies.ico")
window.config(background= vert_fonce)

#Label titre convertisseur

titre = tk.Label(window,text = "Convertisseur de devises", font=("Arial", 15), bg = vert_fonce, fg = vert_clair)
titre.pack( pady=20)

entree_devise_1 = Entry(window, width=15, borderwidth=5, font=("Arial", 10))
entree_devise_1.pack()
#Première device (à convertir) eet saisie du montant à convertir
devise_1 = Label(window, text = "Monnaie à convertir", bg = vert_fonce, fg= 'white', font = ("Arial", 10))
devise_1.pack(pady=20)
choix_devise_1 = ["euros", "dollars", "yen"]
c_devise_1 = ttk.Combobox(window, values = choix_devise_1)
c_devise_1.current(0)
c_devise_1.pack()

#Choix de la device à laquelle on converti
devise_2 = Label(window, text = "Convertir vers", bg = vert_fonce, fg= 'white', font = ("Arial", 10))
devise_2.pack()
choix_devise_2 = ["euros", "dollars", "yen"]
c_devise_2 = ttk.Combobox(window, values = choix_devise_2)
c_devise_2.current(0)
c_devise_2.pack()

#Zone pour afficher le résultat
result_label = Label(window, text="Résultat :", bg= vert_fonce, fg=vert_clair, font=("Arial", 10))
result_label.pack()

# Création d'une zone de texte pour afficher le résultat de la conversion
resultat = Listbox(window, width=30, height=2)
resultat.pack(padx=50, pady=20)


# ****************CODE PROGRAMME **************************************



#Code programme

#Facteurs de taux de conversion fixes

euros_dollars = 1.08
dollars_euros = 0.92
euros_yen = 141.63
yen_euros = 0.0071
dollars_yen = 129.80
yen_dollars = 0.0077

def verification_conversion(choix_devise_1, choix_devise_2):
    if choix_devise_1 == choix_devise_2:
        print("Conversion impossible")
        return False
    return True

def effectuer_conversion(montant, choix_devise_1, choix_devise_2):
    if choix_devise_1 == "euros":
        if choix_devise_2 =="dollars":
            return montant * euros_dollars
        elif choix_devise_2 == "yen":
            return montant * euros_yen
    elif choix_devise_1 == "dollars":
        if choix_devise_2 == "euros":
            return montant * dollars_euros
        elif choix_devise_2 == "yen":
            return montant * dollars_yen
    elif choix_devise_1 == "yen":
        if choix_devise_2 == "euros":
            return montant * yen_euros
        elif choix_devise_2 =="dollars":
            return montant * yen_dollars


def bouton_convertir():
    montant = float(entree_devise_1.get())
    choix_devise_1 = c_devise_1.get()
    choix_devise_2 = c_devise_2.get()
    if verification_conversion(choix_devise_1, choix_devise_2):
        res = str(effectuer_conversion(montant, choix_devise_1, choix_devise_2))
        resultat.delete(0, END)
        resultat.insert(0, res)
    fichier = open("histo_conversion.txt", "a")
    fichier.writelines([str(montant), " ", choix_devise_1, " ", '->', " ", res, " ", choix_devise_2, '\n'])


# Création du bouton "Convertir"
bouton = Button(window, text="Convertir", borderwidth=5, bg= vert_fonce, fg= kaki, font=("Arial", 23), command=bouton_convertir)
bouton.pack()


window.mainloop()