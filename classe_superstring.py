#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:39:48 2020

@author: utilisateur
"""

class superstring : 
  def __init__(self, chaine):
    self.ch = chaine
  def ajoute (self, char):
    self.ch += char
  def insert (self, char , i):
    self.ch = self.ch[:i] + char + self.ch[i:]
  def upper(self):
    self.ch = self.ch.upper()
  def capsdown(self):
    self.ch = self.ch.lower()  
  def tri(self):
    self.ch = self.ch.split(' ')
    #self.ch = self.ch.sort()
    #self.ch=' '.join(x)
    #self.ch = sorted(self.ch)
    self.ch = ' '.join(sorted(self.ch))
  def __str__(self):
    return 'type : superstring, contents: '+self.ch.upper()+'!'



s1 = superstring("this is a pretty python code")
#s1.tri()
print(s1)

#s1 = "this is a pretty python code"
#x = s1.split()
#print(x)
#
#x.sort()
#y=' '.join(x)
#print(x)
#print(y)
#
