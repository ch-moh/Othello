from fltk import *
import os
from constants import FILE_NAME
from graphics import button, error_message
from utils import is_in_button
from main import play

cree_fenetre(800, 800)
rectangle(0, 1000, 1000, 0, 'green', 'green')
texte(300, 100, 'Othello', 'black', "nw", "Arial", 50)

while True:
    ev = donne_ev()
    tev = type_ev(ev)
    button('Nouvelle partie', 100, 500, 300, 400)
    button('Charger partie', 500, 500, 700, 400)

    if tev == "ClicGauche":
        coord_click = (abscisse(ev), ordonnee(ev))
        if is_in_button(100, 500, 300, 400, coord_click):
            ferme_fenetre()
            play()
        if is_in_button(500, 500, 700, 400, coord_click):
            if not os.path.isfile(FILE_NAME):
                error_message(250, 700, "Pas de sauvegarde !")
                continue
            ferme_fenetre()
            play(load=True)
    mise_a_jour()
