# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:22:58 2020

@author: carlitorigami
"""
import matplotlib.image as mpimg
import numpy as np


#documentation : 
#https://deptinfo-ensip.univ-poitiers.fr/ENS/doku/doku.php/stu:python_gui:tuto_images

#-----------quelques méthodes--------
#Lire l'image
img = mpimg.imread("capture.png")
if img.dtype == np.float32: # Si le résultat n'est pas un tableau d'entiers
    img = (img * 255).astype(np.uint8)
#save une image
mpimg.imsave("resultat.png", img)
#un pixel à 3 composante
img[100,220]=(220,0,0) #rouge vert bleu
#exemple simple -> fonction qui renvoit une image qu'avec du rouge (ne modifie pas l'original)
def filtre_rouge(img_orig):
    im = np.copy(img_orig) # On fait une copie de l'original
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            r, v, b = im[i, j]
            im[i, j] = (r, 0,0)
    return im
#------------fin-------------------


#---------début du code----------
#transformée de Karhunen-Loève

def mat_cov():
    
    
    return

#x image initiale 
#FI la matrice de transformée
#Nb la taille des blocs carrés
def tkl2d(x,FI,Nb):
    width=len(x.shape[0])
    height=len(x.shape[1])
    image = np.zeros((width, height, 3), dtype=np.uint8)
    return x,xt,xrec