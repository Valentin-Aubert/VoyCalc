#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import * 
from tkinter.messagebox import *
from functools import partial

## -- Variables -- ##
prixdulitre=0
kms=0
reduction=0
consomation=0


## -- Fonctions -- ##
def cout_deplacement (kms,consomation,prixdulitre):
	return kms * consomation * prixdulitre / 100
	labeldd.config(text=texte)

def recupere():
    prixdulitre = prixlitreE.get()
    kms = kmsE.get()
    reduction = reductionE.get()
    consomation = consomationE.get()

def bonus_reduction (reduction,kms):
	if reduction == 0 :
		return 0
	elif reduction > 0 :
		return reduction * kms
	elif reduction > 10 :
		return "Erreur, le taux de réduction ne peux être au delà de 10€ du km."
	else :
		return "Erreur, le taux de réduction doit être compris entre 0 et 10€."

def cout_total ():
		return cout_deplacement(kms,consomation,prixdulitre)-bonus_reduction(reduction,kms)

cout_deplacement_1 = partial(cout_deplacement, kms, consomation, prixdulitre)
cout_deplacement_1()

## -- GUI -- ##
fenetre = Tk()
fenetre.title('VoyCalc')

## -- Canvas -- ##
photo = PhotoImage(file="VoyCalc.png")
canvas = Canvas(fenetre,width=500, height=50)
canvas.create_image(0, 0, anchor=NW, image=photo)

## -- Labels -- ## 
labeldd = Label(fenetre, text='l')
label = Label(fenetre, text="Hello World")
labelPrix = Label (fenetre, text="Saisir un prix : ")
labelKms = Label (fenetre, text="Entrez le nombre de kms à parcourir : ")
labelConso = Label (fenetre, text="Entrez votre consomation moyenne : ")
labelReduc = Label (fenetre, text="Entrez une réduction : ")

## -- Entrée / Input -- ##
prixdulitre=0
value = StringVar()
value.set("Ici !")
prixlitreE = Entry(fenetre, textvariable=prixdulitre, width=10)
kms=1
value = StringVar()
value.set("Ici !")
kmsE = Entry(fenetre, textvariable=kms, width=10)
consomation=2
value = StringVar()
value.set("Ici !")
consomationE = Entry(fenetre, textvariable=consomation, width=10)
reduction=3
valueRed = StringVar()
valueRed.set("Ici !")
reductionE = Entry(fenetre, textvariable=reduction, width=10)

## Boutons 
boutonValid = Button(fenetre, text = 'Valider', relief=FLAT, command=recupere)
bouttonCalc = Button(fenetre, text ='Calculer', relief=FLAT)
bouttonQuit = Button(fenetre, text ='Quitter', relief=FLAT, command=fenetre.quit)
btttntest = Button (fenetre, text='Test', command=partial(cout_deplacement, kms, consomation, prixdulitre))

## -- Organisation Fenetre -- ##
canvas.grid(row =0, column =0)
label.grid(row =1)
labelPrix.grid(row =2, sticky=W)
prixlitreE.grid(row =2)
labelKms.grid(row =3, sticky=W)
kmsE.grid(row =3)
labelConso.grid(row =4, sticky=W)
consomationE.grid(row =4)
labelReduc.grid(row =5, sticky=W)
reductionE.grid(row =5)
boutonValid.grid (row = 6)
labeldd.grid(row=7)
btttntest.grid(row=8)
bouttonCalc.grid(row = 9, sticky= W)
bouttonQuit.grid(row = 9,sticky=E)

fenetre.mainloop()

"""
## PROGRAME EQUIVALENT SANS GUI ##

print ""
print "###############################################"
print "## MERCI DE RENSEIGNER LES DIFFERENTS CHAMPS ##"
print "###############################################"
print ""

prixdulittre = input("Entrez le prix au littre de votre carburant : ")
kms = input("Entrez le nombre de killomètres à parcourir : ")
consomation = input ("Entrez votre consomation de carburant moyenne sur 100kms : ")
reduction = input ("Entrez votre réduction au km (0 si aucune) : ")

#Module de clacul du deplacement#
def cout_deplacement (kms,consomation,prixdulittre):
	return kms * consomation * prixdulittre / 100


def bonus_reduction (reduction,kms):
	if reduction == 0 :
		return 0
	elif reduction > 0 :
		return reduction * kms
	elif reduction > 10 :
		print "Erreur, le taux de réduction ne peux être au delà de 10€ du km."
	else :
		print "Erreur, le taux de réduction doit être compris entre 0 et 10€."

def cout_total ():
		return cout_deplacement(kms,consomation,prixdulittre)-bonus_reduction(reduction,kms)

print ""
print ""
print "##############"
print "## RESULTAT ##"
print "##############"
print ""
print "Cout brut du voyage estimé :", cout_deplacement(kms,consomation,prixdulittre),"€"
print "Cout estimé du voyage réduction comprise :",cout_total(),"€"
print "Réduction : ", bonus_reduction(reduction,kms), "€"
print "Consomation : ", cout_deplacement(consomation,kms,1),"L"

"""
