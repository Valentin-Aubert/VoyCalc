#!/usr/bin/python3.4
# -*-coding: utf-8 -*

import tkinter as tk
import re

SEP_DEC = ','

def bonusReduction(reduction, kms) :
    return round(reduction * kms, 2)
   
def estimationCoutTrajet(kms, consommation, prixDuLitre) :
    return round(kms * consommation * prixDuLitre / 100, 2)
   
def estimationConsommationTrajet(kms, consommation) :
    return round(kms * consommation / 100, 2)

def estimationConsommationTrajetTotal(kms, consommation, reduction) :
    return round((kms * consommation / 100 ) - (reduction * kms), 2)

def afficherResultats(objet) :
    if not objet.getvar('prix') and not objet.getvar('kms') and not objet.getvar('conso') and not objet.getvar('reduc') :
        return
    prix = objet.getvar('prix')
    kms = objet.getvar('kms')
    conso = objet.getvar('conso')
    reduc = objet.getvar('reduc')

    if SEP_DEC != '.' :
        prix = prix.replace(SEP_DEC, '.')
        kms = kms.replace(SEP_DEC, '.')
        conso = conso.replace(SEP_DEC, '.')
        reduc = reduc.replace(SEP_DEC, '.')
       
    resultats = []
    # Contrôles des valeurs
    if not prix :
        resultats.append('Vous devez renseigner le prix au litre du carburant.')
    elif not re.match(r'^\d\.\d{2}$', prix) :
        resultats.append('Le prix du carburant doit être de la forme 0{}00 .'.format(SEP_DEC))
    
    if not kms :
        resultats.append('Vous devez renseigner le nombre de kilomètres à parcourir.')
    elif not re.match('^\d+(\.\d\d?)?$', kms) :
        resultats.append('Kilomètres doit être un entier, ou un nombre décimal à un ou 2 décimaux.')
       
    if not conso :
        resultats.append('Vous devez renseigner la consommation moyenne.')
    elif not re.match('^\d+(\.\d\d?)?$', conso) :
        resultats.append('La consommation doit être un entier, ou un décimal.')
       
    if not reduc : 
        resultats.append('Vous devez renseigner votre réduction, 0 si aucune.')
    elif not re.match(r'^\d\.\d{2}$', reduc) :
        resultats.append('La reduction doit être de forme 0{}00 .'.format(SEP_DEC))
    
    # Erreurs rencontrées
    if resultats :
        objet.setvar('resultat', '\n'.join(resultats))
        return
       
    # Conversion des strings en float pour effectuer les calculs
    prixf = float(prix)
    kmsf = float(kms)
    consof = float(conso)
    reducf = float(reduc)
   
    coutTrajet = str(estimationCoutTrajet(kmsf, consof, prixf))
    consoTrajet = str(estimationConsommationTrajet(kmsf, consof))
    consoTrajetTot = str(estimationConsommationTrajetTotal(kmsf, consof, reducf))
    reduction = str(bonusReduction(kmsf, reducf))

    if SEP_DEC != '.' :
        coutTrajet = coutTrajet.replace('.', SEP_DEC)
        consoTrajet = consoTrajet.replace('.', SEP_DEC)
        consoTrajetTot = consoTrajetTot.replace('.', SEP_DEC)

    resultats.append("Coût du voyage estimé : {}€".format(consoTrajetTot))
    resultats.append("Coût brut du voyage estimé : {}€".format(coutTrajet))
    if reduc :
        pass   
    resultats.append('Consommation : {}L'.format(consoTrajet))
    resultats.append('Réduction : {}€ '.format(reduction))
   
    objet.setvar('resultat', '\n'.join(resultats))

fenetre = tk.Tk()
fenetre.title = "VoyCalc"
fenetre['bg'] = "dark slate grey"

cadre = tk.Frame(fenetre, bg="dark slate grey" )
cadre.grid()
cadre.columnconfigure(2, weight=1)

canvas = tk.Canvas(cadre, width=500, height=50, bg="dark slate grey" )
canvas.grid(row=1, column=1, columnspan=2)

photo = tk.PhotoImage(file="VoyCalc.png" )
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

labelInfo = tk.Label(cadre, text="Calcul du coût du carburant d'un trajet", bg="dark slate grey" )
labelInfo.grid(row=2, column=1, columnspan=2, pady=20)

labelPrix = tk.Label(cadre, text="Prix au litre du carburant :", bg="dark slate grey" )
labelPrix.grid(row=3, column=1, padx=15, pady=5, sticky=tk.E)


varPrix = tk.StringVar(fenetre, "", "prix" ) # tkinter Variable peut prendre 3 arguments => StringVar(master, value, name)
entreePrix = tk.Entry(cadre, textvariable=varPrix, width=10, bg="dark slate grey" )
entreePrix.grid(row=3, column=2, sticky=tk.W)
entreePrix.columnconfigure(1, weight=5)


labelKms = tk.Label(cadre, text="Nombre de kilomètres à parcourir :", bg="dark slate grey" )
labelKms.grid(row=4, column=1, padx=15, pady=5, sticky=tk.E)

varKms = tk.StringVar(fenetre, "", "kms" )

entreeKms = tk.Entry(cadre, textvariable=varKms, width=10, bg="dark slate grey" )
entreeKms.grid(row=4, column=2, sticky=tk.W)


labelConso = tk.Label(cadre, text="Consommation (litres/100) :", bg="dark slate grey" )
labelConso.grid(row=5, column=1, padx=15, pady=5, sticky=tk.E)

varConso = tk.StringVar(fenetre, "", "conso" )
entreeConso = tk.Entry(cadre, textvariable=varConso, width=10, bg="dark slate grey" )
entreeConso.grid(row=5, column=2, sticky=tk.W)

labelReduc= tk.Label(cadre, text="Réduction (optionnel) :", bg="dark slate grey" )
labelReduc.grid(row=6, column=1, padx=15, pady=5, sticky=tk.E)

varReduc = tk.StringVar(fenetre, "", "reduc" )

entreeReduc = tk.Entry(cadre, textvariable=varReduc, width=10, bg="dark slate grey" )
entreeReduc.grid(row=6, column=2, sticky=tk.W)
varResultat = tk.StringVar(fenetre, "", "resultat" )

labelResultat = tk.Label(cadre, textvariable=varResultat, width=70, height=4, justify=tk.LEFT, bg="dark slate grey" )
labelResultat.grid(row=8, column=1, columnspan=2)

boutonCalcul = tk.Button(cadre, text="Calculer", relief="flat", command=lambda f=fenetre : afficherResultats(f))
boutonCalcul.grid(row=7, column=1, columnspan=2, pady=20)

boutonQuit = tk.Button(cadre, text="Quiter", relief="flat", command=fenetre.quit)
boutonQuit.grid(row=9, columnspan=4, pady=20)

fenetre.mainloop()
