import pygame
from pygame.locals import *

import time
import math
import utils
import datetime
import random

import model
import ihm

pygame.init()

# BOUCLE INFINIE

size = width, height = 768, 768
rayonCercle = (0.95 * height) / 2
rect = pygame.Rect(width / 2 - rayonCercle, height / 2 - rayonCercle, rayonCercle * 2, rayonCercle * 2)


# COULEURS
black = 0, 0, 0
blue = 89, 120, 255
white = 255, 255, 255
# SON
sonChoc = []
for i in range(1,5) :
    son = pygame.mixer.Sound("son/choc_"+str(i)+".ogg")
    sonChoc.append(son)

sonPoint = []
son = pygame.mixer.Sound("son/point_marquer.ogg")
sonPoint.append(son)
son = pygame.mixer.Sound("son/point_retirer.ogg")
sonPoint.append(son)

sonfin = pygame.mixer.Sound("son/son_fin.ogg")

sonNiveau= pygame.mixer.Sound("son/level_up.ogg")

sonRessort = []

son = pygame.mixer.Sound("son/Ressort1.ogg")
sonRessort.append(son)
son = pygame.mixer.Sound("son/Ressort2.ogg")
sonRessort.append(son)
son = pygame.mixer.Sound("son/Ressort3.ogg")
sonRessort.append(son)

pygame.display.set_caption("Trash Space")
nbDechet = 1
spriteGroup = pygame.sprite.Group()
screen = pygame.display.set_mode((1024, 768))
rail = model.Plateform(1, rect)
listeDechet = []
listPoubelles = []

pers = model.Scrapy()
# -------------------CREATION des DECHET-------------------------
x ,y = utils.getXYDechet()

dechet = model.Dechet(x, y)
spriteGroup.add(dechet)
listeDechet.append(dechet)
nbDechet += 1

# -------------------CREATION des POUBELLE-----------------------
listPoubelles.append(model.Poubelle(90, 1))

#--------------------PARAMETRE--------------------------------
#SCORE
scor = utils.Score()


nom_joueur = "nom"

start_time = datetime.datetime.now().time()
h = 0
if start_time.minute+3 > 59:
    h = 1
end_time = datetime.time((start_time.hour+h)%24, (start_time.minute+3) % 60, start_time.second+0)
sec = 180
pygame.key.set_repeat(30, 5)
n = 0
frame = 0
# -------------------DEBUT DU WHILE--------
continuer = 1
play = 0
tuto = 0
credit = 0
anim_explosion = 0
oldscore = 10
temp_poub = listPoubelles[0]
dance = 0
while continuer:

    if datetime.datetime.now().time() > end_time and play ==1:
        ihm.finjeux()
        scor.finDuJeu()
        scor.affichage(screen, 4)
        ihm.playSon(sonfin)
        ihm.updateTextFin(scor)
        pygame.display.flip()
        boucle = 1
        while boucle:
            for event in pygame.event.get():  # Attente des événements
                if event.type == QUIT:
                    continuer = 0
                    boucle = 0
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and ihm.checkButtonClick("exit", event):  # Si clic gauche
                        continuer = 0
                        boucle = 0
                    if event.button == 1 and ihm.checkButtonClick("exitTuto", event):  # Si clic gauche
                        boucle = 0
        play = 0

    if not play and not credit and not tuto:
        ihm.updateAffichageMenu()
        ihm.updateAffichageCurrentNom(nom_joueur)
        ihm.playMusic("son/Menu_Theme.mp3")
        ihm.AnimationMenuDance(dance)
        dance += 1
        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                continuer = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and ihm.checkButtonClick("exit", event):  # Si clic gauche
                    continuer = 0
                if event.button == 1 and ihm.checkButtonClick("play", event):  # Si clic gauche
                    ihm.stopMusic()
                    dance = 0
                    play = 1
                    sec = 180
                    scor = utils.Score()
                    listPoubelles[:] = []
                    listeDechet[:] = []
                    nbDechet=0
                    listPoubelles.append(model.Poubelle(90, 1))
                    start_time = datetime.datetime.now().time()
                    print("START: ", start_time)
                    h = 0
                    m = 3
                    if start_time.minute + 3 > 59:
                        h = 1
                    end_time = datetime.time(start_time.hour+h, (start_time.minute+3) % 60, (start_time.second+0)%60)
                    print("END: ", end_time)
                if event.button == 1 and ihm.checkButtonClick("credit", event):  # Si clic gauche
                    credit = 1
                if event.button == 1 and ihm.checkButtonClick("tuto", event):  # Si clic gauche
                    tuto = 1
                if event.button == 1 and ihm.checkButtonClick("nom", event):
                    pygame.key.set_repeat(400, 50)
                    nom_joueur = ""
                    while len(nom_joueur) < 3:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if  event.key != pygame.K_COMMA :
                                    nom_joueur += str(chr(event.key))
                                    pygame.key.set_repeat(30, 5)
                        ihm.updateAffichageMenu()
                        ihm.updateAffichageScore()
                        ihm.AnimationMenuDance(dance)
                        dance += 1
                        ihm.updateAffichageCurrentNom(nom_joueur)
                        pygame.display.flip()

    elif tuto:
        screen.blit(ihm.bgTuto, (0, 0))
        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                continuer = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and ihm.checkButtonClick("exit", event):  # Si clic gauche
                    continuer = 0
                if event.button == 1 and ihm.checkButtonClick("exitTuto", event):  # Si clic gauche
                    ihm.updateAffichageMenu()
                    tuto = 0

    elif credit:
        screen.blit(ihm.bgCredit, (0, 0))
        for event in pygame.event.get():  # Attente des événements
            if event.type == QUIT:
                continuer = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and ihm.checkButtonClick("exit", event):  # Si clic gauche
                    continuer = 0
                if event.button == 1 and ihm.checkButtonClick("exitCredit", event):  # Si clic gauche
                    ihm.updateAffichageMenu()
                    credit = 0
    else:

        chrono = (end_time.second-datetime.datetime.now().second)+(end_time.minute-datetime.datetime.now().minute)*60

        ihm.updateAffichagJeu()
        ihm.playMusic("son/Theme_jeu.mp3")


        # PARTIE COLLISION
        for unDechet in listeDechet:
            # Collision avec les rails
            rail.collide(unDechet)
            # Collision avec le personnage
            a = pygame.sprite.collide_mask(pers, unDechet)
            if a is not None and pers.tirEnCour:
                pers.tirerUnDechet(unDechet)



        for count1, dechet1 in enumerate(listeDechet):
            for count2, dechet2 in enumerate(listeDechet[:-len(listeDechet) + count1]):
                # Boucle qui permet d'eviter les repetitions et d'avoir toutes les pairs possibles

                if math.hypot(dechet1.x - dechet2.x, dechet1.y - dechet2.y) <= (dechet1.width / 2 + dechet2.width / 2):
                    ihm.playSon(sonChoc[random.randint(0,len(sonChoc)-1)])
                    # print("colision entre deux cercle")
                    if dechet1.derniereCollision != dechet2 or dechet2.derniereCollision != dechet1:
                        utils.CircleCollide(dechet1, dechet2)

        dechetAsupprimer = None
        # On ne peut pas toucher a une liste sur la quelle on boucle , obliger de stocker le dechet puis de le supprimer
        for unDechet in listeDechet[:]:
            for unePoublle in listPoubelles:
                a = pygame.sprite.collide_mask(unDechet, unePoublle)
                if a != None:
                    dechetAsupprimer = unDechet
                    temp_poub = unePoublle
                    nbDechet -= 1
                    if unDechet.type == unePoublle.type:
                        anim_explosion = 1
                        if scor.score_plus():
                            ihm.playSon(sonNiveau)
                        ihm.playSon(sonPoint[0])
                    else:
                        anim_explosion = -1
                        scor.score_moins()
                        ihm.playSon(sonPoint[1])


        if dechetAsupprimer != None:
            listeDechet.remove(dechetAsupprimer)
            spriteGroup.remove(dechetAsupprimer)
            dechetAsupprimer = None


        # FIN PARTIE COLLISION
        if anim_explosion > 0:
            ihm.AnimationExplosionNegatif(anim_explosion, temp_poub)
            anim_explosion += 1
            if anim_explosion > 45:
                anim_explosion = 0
        elif anim_explosion < 0:
            ihm.AnimationExplosion(anim_explosion, temp_poub)
            anim_explosion -= 1
            if anim_explosion < -45:
                anim_explosion = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                ihm.finjeux()
                continuer = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and ihm.checkButtonClick("exit", event):  # Si clic gauche
                    ihm.finjeux()
                    continuer = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pers.deplacer(1)
                if event.key == pygame.K_RIGHT:
                    pers.deplacer(-1)
                if event.key == pygame.K_UP:
                    ihm.playSon(sonRessort[random.randint(0, 2)])
                    n = 1
                if event.key == pygame.K_SPACE:
                    n = 1
                    ihm.playSon(sonRessort[random.randint(0, 2)])

        # ----ANIMATION TIR---------
        if n > 0 and n < 3:
            pers.tirer(1)
            n += 1
        elif n > 0 and n < 15:
            pers.tirer(2)
            n += 1
        elif n > 0 and n < 20:
            pers.tirer(1)
            n += 1
        elif n > 0 and n < 25:
            pers.tirer(0)
            n = 0

        # -------------------CREATION des DECHET-------------------------
        # print(chrono+1, " ? ", sec)
        # print("nbDechet: ", nbDechet)
        if (chrono+1 < sec and nbDechet < 5) or (chrono < 170 and nbDechet == 0):
            x ,y = utils.getXYDechet()
            i = 0
            nbTentative = 0
            while i < len(listeDechet) and nbTentative < len(listeDechet) * 3:
                nbTentative += 1
                unDechet = listeDechet[i]
                if (x >= unDechet.x - 60) and (x <= unDechet.x + 60) and (y >= unDechet.y - 60) and (
                        y <= unDechet.y + 60):
                    i = 0
                    x ,y = utils.getXYDechet()

                i += 1
            dechet = model.Dechet(x, y, random.randint(1, scor.nbMaxType), scor.scarpSpeed)
            spriteGroup.add(dechet)
            listeDechet.append(dechet)
            nbDechet += 1
            sec -= scor.apparitions[scor.lvl-1]


        # -------------------CREATION des POUBELLES-------------------------
        if scor.lvl == 2 and len(listPoubelles) < 2:
            listPoubelles.append(model.Poubelle(210, 2))
            scor.nbMaxType += 1
            scor.affichage(screen, 2)
        elif scor.lvl == 4 and len(listPoubelles) < 3:
            listPoubelles.append(model.Poubelle(330, 3))
            scor.nbMaxType += 1
            scor.affichage(screen, 3)

        # -- ON DESSINE --
        for i in listeDechet:
            i.draw(screen)
        for i in listPoubelles:
            i.draw(screen)
        pers.draw(screen)
        ihm.updateAffichageCurrentScore(scor.val)
        if oldscore != scor.val:
            ihm.addScore(nom_joueur,scor.val)
            oldscore = scor.val
        ihm.updateTimer(chrono)
        ihm.updateAfficheCombo(scor.combo)
        ihm.updateAfficheLvl(scor.lvl)

    ihm.updateScore()
    ihm.updateAffichageScore()

    pygame.display.flip()
