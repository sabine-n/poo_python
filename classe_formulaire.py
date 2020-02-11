#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:14:46 2020

@author: utilisateur
"""

class formulaire:
    def __init__(self, nom, prenom, anneeNaissance):
        self.nom = nom.upper()
        self.prenom = prenom
        self.anneeNaissance = anneeNaissance
    def age(self):
        return 2020 - self.anneeNaissance
    def majeur(self):
        return self.age() >= 18
    def memeFamille(self, formulaire):
        return self.nom == formulaire.nom
    def memePersonne(self, formulaire):
        return self.nom == formulaire.nom and self.prenom == formulaire.prenom and self.anneeNaissance == formulaire.anneeNaissance
    def __str__(self): # def __repr__(self):
        return '('+self.nom+', '+self.prenom+', %s)' % (self.anneeNaissance)
    
jd = formulaire('Doe', 'John', 2005)
ad = formulaire('Doe', 'Alice', 2000)
sn = formulaire('Nasr', 'Sabine', 1992)
kb = formulaire('Bryant', 'Kobe', 1978)
so = formulaire("O'neal", 'Shaquille', 1972)
ld = formulaire('David', 'Larry', 1947)
jh = formulaire('Hendrix', 'Jimi', 1942)

#print(jd.majeur())
#print(ad.majeur())
#print(jd.memeFamille(ad))
#print(jd, ad)
#rint(ad)

liste_formulaire=[]
liste_formulaire.append(jd)
liste_formulaire.append(ad)
liste_formulaire.append(sn)
liste_formulaire.append(kb)
liste_formulaire.append(so)
liste_formulaire.append(ld)
liste_formulaire.append(jh)


a = sorted(liste_formulaire, key = lambda year : year.anneeNaissance)

for i in a:
    print(i)
    

#print(sorted(liste_formulaire, key = lambda year : year.anneeNaissance))


