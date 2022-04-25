import pygame
from pygame.locals import *
import model, utils
import math

pygame.init()

screen = pygame.display.set_mode((1024, 768), HWSURFACE | DOUBLEBUF | RESIZABLE)

from pygame.locals import *

#Déclaration image Liam

text_size = 30
bg_col = [0,0,0]
text_col = [104,180,46]

fond = pygame.image.load("image/backgroundGames.png").convert()
screen.blit(fond, (0, 0))

bgCredit = pygame.image.load("image/credit.png").convert()

# Chargement et collage du personnage
bpPlay = pygame.image.load("image/play-button.png").convert_alpha()
screen.blit(pygame.transform.scale(bpPlay, (150, 150)), (768/2-75, 768/2-75))

bpTuto = pygame.image.load("image/bpTuto.png").convert_alpha()
screen.blit(pygame.transform.scale(bpTuto, (100, 100)), (768 / 2 - 50, 768 / 2 + 225))

bpCredit = pygame.image.load("image/bpcredit.png").convert_alpha()
screen.blit(pygame.transform.scale(bpCredit, (180, 50)), (768/2-90, 768/2+150))

bgTuto = pygame.image.load("image/tuto.png").convert_alpha()

dance0 = pygame.image.load("image/dance0.png").convert_alpha()
dance1 = pygame.image.load("image/dance1.png").convert_alpha()
dance2 = pygame.image.load("image/dance2.png").convert_alpha()
dance3 = pygame.image.load("image/dance3.png").convert_alpha()
dance4 = pygame.image.load("image/dance4.png").convert_alpha()

combo1 = pygame.image.load("image/1.png").convert_alpha()
combo2 = pygame.image.load("image/2.png").convert_alpha()
combo3 = pygame.image.load("image/3.png").convert_alpha()
combo4 = pygame.image.load("image/4.png").convert_alpha()
combo5 = pygame.image.load("image/5.png").convert_alpha()
combo6 = pygame.image.load("image/6.png").convert_alpha()
combo7 = pygame.image.load("image/7.png").convert_alpha()
combo8 = pygame.image.load("image/8.png").convert_alpha()
combo9 = pygame.image.load("image/9.png").convert_alpha()
combo = [combo1,combo2,combo3,combo4,combo5,combo6,combo7,combo8,combo9]

lvl1 = pygame.image.load("image/lvl1.png").convert_alpha()
lvl2 = pygame.image.load("image/lvl2.png").convert_alpha()
lvl3 = pygame.image.load("image/lvl3.png").convert_alpha()
lvl4 = pygame.image.load("image/lvl4.png").convert_alpha()
lvl5 = pygame.image.load("image/lvl5.png").convert_alpha()
lvl6 = pygame.image.load("image/lvl6.png").convert_alpha()
lvl7 = pygame.image.load("image/lvl7.png").convert_alpha()
lvl8 = pygame.image.load("image/lvl8.png").convert_alpha()
lvl9 = pygame.image.load("image/lvl9.png").convert_alpha()
lvl = [lvl1,lvl2,lvl3,lvl4,lvl5,lvl6,lvl7,lvl8,lvl9]

explosion0 = pygame.image.load("image/explosion0.png").convert_alpha()
explosion1 = pygame.image.load("image/explosion1.png").convert_alpha()
explosion2 = pygame.image.load("image/explosion2.png").convert_alpha()
explosion3 = pygame.image.load("image/explosion3.png").convert_alpha()
explosion4 = pygame.image.load("image/explosion4.png").convert_alpha()
explosion5 = pygame.image.load("image/explosion5.png").convert_alpha()
explosion6 = pygame.image.load("image/explosion6.png").convert_alpha()
explosion7 = pygame.image.load("image/explosion7.png").convert_alpha()
explosion8 = pygame.image.load("image/explosion8.png").convert_alpha()

explosion1negatif = pygame.image.load("image/explosion1negatif.png").convert_alpha()
explosion2negatif = pygame.image.load("image/explosion2negatif.png").convert_alpha()
explosion3negatif = pygame.image.load("image/explosion3negatif.png").convert_alpha()
explosion4negatif = pygame.image.load("image/explosion4negatif.png").convert_alpha()
explosion5negatif = pygame.image.load("image/explosion5negatif.png").convert_alpha()
explosion6negatif = pygame.image.load("image/explosion6negatif.png").convert_alpha()
explosion7negatif = pygame.image.load("image/explosion7negatif.png").convert_alpha()
explosion8negatif = pygame.image.load("image/explosion8negatif.png").convert_alpha()

menuDroite = pygame.image.load("image/menuDroite.png").convert_alpha()
screen.blit(pygame.transform.scale(menuDroite, (256, 768)), (768, 0))

plaque = pygame.image.load("image/plaque.png").convert_alpha()
screen.blit(pygame.transform.scale(plaque, (192, 112)), (800, 30))

bpExit = pygame.image.load("image/bpExit.png").convert_alpha()
screen.blit(pygame.transform.scale(bpExit, (197, 105)), (800, 35))

score = pygame.image.load("image/scoreNom.png").convert_alpha()
scoreCurrent = pygame.image.load("image/scoreCurrent.png").convert_alpha()
screen.blit(pygame.transform.scale(score, (192, 490)), (800, 250))

affichageFin = pygame.image.load("image/ecranFIN.png").convert_alpha()

titreScore = pygame.image.load("image/titreScore.png").convert_alpha()
screen.blit(pygame.transform.scale(titreScore, (170, 18)), (810, 263))
# Rafraîchissement de l'écran

myfont = pygame.font.Font(None, text_size)           # uses default pygame font; you can also specify a named font
myfontBig = pygame.font.Font(None, text_size+15)     # uses default pygame font; you can also specify a named font

ArrayTextScore = []
pygame.display.flip()

# Déclaration du nom du fichier source
nomFichierScore = "score.csv"

# -- Fonction Liam --
#Combo
def updateAfficheCombo(num):
    screen.blit(pygame.transform.scale(combo[num-1], (250, 75)), (775, 165))
#fin Combo
#Lvl
def updateAfficheLvl(num):
    screen.blit(pygame.transform.scale(lvl[num-1], (200, 30)), (550, 720))
#fin lvl
#Score :

def finjeux():

    global ArrayTextScore
    updateScore()
    dst = open(nomFichierScore, "w")
    dst.write("Place,Nom,Score,Current\n")
    stop = 1
    for n in range(0, 15):
        if stop:
            if ArrayTextScore[0] != "null" and ArrayTextScore[1] != "null" and ArrayTextScore[2] != "null" and ArrayTextScore[3] != "null":
                dst.write("%s,%s,%s,%s\n" % (str(n + 1), ArrayTextScore[1], ArrayTextScore[2], "0"))
                ArrayTextScore.pop(0)
                ArrayTextScore.pop(0)
                ArrayTextScore.pop(0)
                ArrayTextScore.pop(0)
            else:
                stop = 0
    dst.write("null,null,null,null\n")
    dst.close()
    updateScore()

def updateTextFin(scor:utils.Score):
    screen.blit(pygame.transform.scale(affichageFin, (500, 200)), (150, 80))
    txt1 = myfontBig.render(str(scor.comboMax), True, (255,140,0), bg_col)
    txt2 = myfontBig.render(str(scor.lvl), True, (255,140,0), bg_col)
    txt3 = myfontBig.render( str(scor.nbTriReussi), True, text_col, bg_col)
    txt4 = myfontBig.render(str(scor.nbTriRate), True, (245,12,12), bg_col)
    txt5 = myfontBig.render(str(scor.val), True, text_col, bg_col)
    rect1 = txt1.get_rect()
    rect1.center = [500, 110]
    screen.blit(txt1, rect1)

    rect2 = txt2.get_rect()
    rect2.center = [500, 145]
    screen.blit(txt2, rect2)

    rect3 = txt3.get_rect()
    rect3.center = [500, 180]
    screen.blit(txt3, rect3)

    rect4 = txt4.get_rect()
    rect4.center = [500, 215]
    screen.blit(txt4, rect4)

    rect5 = txt5.get_rect()
    rect5.topleft = [350, 238]
    screen.blit(txt5, rect5)


def addScore(nomPlayer,scorePlayer):

    global ArrayTextScore
    updateScore()
    dst = open(nomFichierScore, "w")
    dst.write("Place,Nom,Score,Current\n")
    decalage = 0
    remove = 0
    stop = 1
    for n in range(0,15):
        if stop:
            if ArrayTextScore[0] != "null" and ArrayTextScore[1] != "null" and ArrayTextScore[2] != "null" and ArrayTextScore[3] != "null":
                if ArrayTextScore[3] == "0":
                    if int(ArrayTextScore[2]) < scorePlayer and decalage == 0:
                        dst.write("%s,%s,%s,%s\n" % (n+1+remove, nomPlayer, scorePlayer, "1"))
                        decalage = 1
                    dst.write("%s,%s,%s,%s\n" % (str(n+1+decalage+remove), ArrayTextScore[1], ArrayTextScore[2], "0"))
                    ArrayTextScore.pop(0)
                    ArrayTextScore.pop(0)
                    ArrayTextScore.pop(0)
                    ArrayTextScore.pop(0)
                else:
                    ArrayTextScore.pop(0)
                    ArrayTextScore.pop(0)
                    ArrayTextScore.pop(0)
                    ArrayTextScore.pop(0)
                    remove = -1
            elif not decalage:
                dst.write("%s,%s,%s,%s\n" % (n + 1 + remove, nomPlayer, scorePlayer, "1"))
                decalage = 1
            else:
                stop = 0
    dst.write("null,null,null,null\n")
    dst.close()
    updateScore()

def updateScore():
    # Lit l'en-tête, élimine la fin de ligne, et extrait les
    # champs séparés par une virgule

    global ArrayTextScore
    ArrayTextScore = []

    src = open(nomFichierScore, "r")

    entete = src.readline().rstrip('\n\r').split(",")

    # Détermine l'index des différents champs qui nous sont utiles
    listplace = entete.index("Place")
    listnom = entete.index("Nom")
    listscore = entete.index("Score")
    listcurrent = entete.index("Current")

    # Puis les données
    for ligne in src:
        # Extraction des données de la ligne séparées par une virgule
        donnees = ligne.rstrip('\n\r').split(",")
        ArrayTextScore.append(donnees[listplace])
        ArrayTextScore.append(donnees[listnom])
        ArrayTextScore.append(donnees[listscore])
        ArrayTextScore.append(donnees[listcurrent])

    src.close()


def updateAffichageCurrentScore(score):
    my_image = myfontBig.render(str(score),True, text_col, bg_col)
    rect = my_image.get_rect()
    rect.center = [895,718]
    screen.blit(my_image, rect)


def updateAffichageCurrentNom(nom):
    my_image = myfontBig.render(str(nom), True, text_col, bg_col)
    rect = my_image.get_rect()
    rect.center = [895,718]
    screen.blit(my_image, rect)


def updateAffichageScore():
    col = 315
    global ArrayTextScore
    stop = 1
    for n in range(0,15):
        if stop:
            if ArrayTextScore[n*4] != "null" and ArrayTextScore[n*4+1] != "null" and ArrayTextScore[n*4+2] != "null" and ArrayTextScore[n*4+3] != "null" and n == int(ArrayTextScore[n*4])-1:
                my_image = myfont.render(str(ArrayTextScore[n*4]) + " " + str(ArrayTextScore[n*4+1]) + " : " + str(ArrayTextScore[n*4+2]), True, text_col, None)
                rect = my_image.get_rect()
                rect.center = [895, col]
                screen.blit(my_image, rect)
                col = col + 23
            else:
                stop = 0

    screen.blit(pygame.transform.scale(titreScore, (170, 18)), (810, 263))

#fin Score
#Menu


def updateAffichageMenu():
    # Re-collage
    screen.blit(fond, (0, 0))
    screen.blit(pygame.transform.scale(bpPlay, (150, 150)), (768 / 2 - 75, 768 / 2 - 75))
    screen.blit(pygame.transform.scale(bpCredit, (180, 50)), (768 / 2 - 90, 768 / 2 + 150))
    screen.blit(pygame.transform.scale(menuDroite, (256, 768)), (768, 0))
    screen.blit(pygame.transform.scale(plaque, (192, 112)), (800, 30))
    screen.blit(pygame.transform.scale(bpExit, (197, 105)), (800, 35))
    screen.blit(pygame.transform.scale(bpTuto, (100, 100)), (768 / 2 - 50, 768 / 2 + 225))
    screen.blit(pygame.transform.scale(score, (192, 490)), (800, 250))

#fin Menu
#jeu

def updateAffichagJeu():
    # Re-collage
    screen.blit(fond, (0, 0))
    screen.blit(pygame.transform.scale(menuDroite, (256, 768)), (768, 0))
    screen.blit(pygame.transform.scale(plaque, (192, 112)), (800, 30))
    screen.blit(pygame.transform.scale(bpExit, (197, 105)), (800, 35))
    screen.blit(pygame.transform.scale(scoreCurrent, (192, 490)), (800, 250))

#fin Menu
#Button

def checkButtonClick(name,event):
    if name == "exit" and event.pos[0] >= 820 and event.pos[0] <= 800+172 and event.pos[1] >= 50 and event.pos[1] <= 35+85:
        return True
    if name == "credit" and event.pos[0] >= 768/2-90 and event.pos[0] <= 768/2+180-90 and event.pos[1] >= 768/2+150 and event.pos[1] <= 768/2+200:
        return True
    if name == "play" and event.pos[0] >= 768/2-75 and event.pos[0] <= 768/2+150-75 and event.pos[1] >= 768/2-75 and event.pos[1] <= 768/2+150-75:
        return True
    if name == "exitCredit" and event.pos[0] >= 602 and event.pos[0] <= 760 and event.pos[1] >= 688 and event.pos[1] <= 761:
        return True
    if name == "nom" and event.pos[0] >= 807  and event.pos[0] <= 807+181 and event.pos[1] >= 700 and event.pos[1] <= 700 + 37:
        return True
    if name == "tuto" and event.pos[0] >= 768/2-50 and event.pos[0] <= 768/2+50 and event.pos[1] >= 768/2+225 and event.pos[1] <= 768/2+325:
        return True
    if name == "exitTuto" and event.pos[0] >= 0 and event.pos[0] <= 768 and event.pos[1] >= 0 and event.pos[1] <= 768:
        return True

#fin Button
#Music
def playMusic(name):
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(name)
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play()

def playSon(name):
    name.play()

def stopMusic():
     pygame.mixer.music.stop()
#fin Music
#Animation
def AnimationMenuDance(frame):
    frame = frame%120
    if frame < 5*3:
        screen.blit(pygame.transform.scale(dance0, (344, 344)), (768 / 2 + 344/4, 768-290))
    elif frame < 10*3:
        screen.blit(pygame.transform.scale(dance1, (344, 344)), (768 / 2 + 344/4, 768-290))
    elif frame < 15*3:
        screen.blit(pygame.transform.scale(dance2, (344, 344)), (768 / 2 + 344/4, 768-290))
    elif frame < 20*3:
        screen.blit(pygame.transform.scale(dance3, (344, 344)), (768 / 2 + 344/4, 768-290))
    elif frame < 25*3:
        screen.blit(pygame.transform.scale(dance4, (344, 344)), (768 / 2 + 344/4, 768-290))
    elif frame < 30*3:
        screen.blit(pygame.transform.scale(dance3, (344, 344)), (768 / 2 + 344/4, 768-290))
    elif frame < 35*3:
        screen.blit(pygame.transform.scale(dance2, (344, 344)), (768 / 2 + 344/4, 768-290))
    elif frame < 40*3:
        screen.blit(pygame.transform.scale(dance1, (344, 344)), (768 / 2 + 344/4, 768-290))


def AnimationExplosion(frame, poubelle:model.Poubelle):
    frame = abs(frame) % 45
    t = int(344*0.5)
    a = math.degrees(poubelle.angle + math.pi/2)
    anglePlacement = -poubelle.angle
    rayonCercle = 768*0.40

    x = math.cos(anglePlacement)*rayonCercle+360
    y = math.sin(anglePlacement)*rayonCercle+384
    rect = pygame.Rect((x, y), (t, t))
    rect.center= (x, y)
    if frame < 5:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion0, (t, t)), a), rect)
    elif frame < 10:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion1, (t, t)), a), rect)
    elif frame < 15:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion2, (t, t)), a), rect)
    elif frame < 20:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion3, (t, t)), a), rect)
    elif frame < 25:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion4, (t, t)), a), rect)
    elif frame < 30:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion5, (t, t)), a), rect)
    elif frame < 35:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion6, (t, t)), a), rect)
    elif frame < 40:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion7, (t, t)), a), rect)
    elif frame < 45:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion8, (t, t)), a), rect)

def AnimationExplosionNegatif(frame, poubelle:model.Poubelle):
    frame = abs(frame) % 45
    t = int(344*0.5)
    a = math.degrees(poubelle.angle + math.pi/2)
    anglePlacement = -poubelle.angle
    rayonCercle = 768*0.40
    # rect = pygame.Rect((poubelle.x, poubelle.y), (t, t))
    # rect.center= (math.radians(math.cos(a))*rayonCercle+384, math.radians(math.sin(a))*rayonCercle+384)
    x = math.cos(anglePlacement)*rayonCercle+360
    y = math.sin(anglePlacement)*rayonCercle+384
    rect = pygame.Rect((x,y), (t, t))
    rect.center= (x,y)
    # rect.x += 75*math.sin(poubelle.angle)
    # rect.y += -75*math.cos(poubelle.angle)
    if frame < 5:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion0, (t, t)), a), rect)
    elif frame < 10:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion1negatif, (t, t)), a), rect)
    elif frame < 15:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion2negatif, (t, t)), a), rect)
    elif frame < 20:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion3negatif, (t, t)), a), rect)
    elif frame < 25:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion4negatif, (t, t)), a), rect)
    elif frame < 30:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion5negatif, (t, t)), a), rect)
    elif frame < 35:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion6negatif, (t, t)), a), rect)
    elif frame < 40:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion7negatif, (t, t)), a), rect)
    elif frame < 45:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(explosion8negatif, (t, t)), a), rect)


#fin Animation
# Timer
def updateTimer(sec):
    text_size = 50
    myfont2 = pygame.font.Font(None, text_size)  # uses default pygame font; you can also specify a named font
    bg_col = [0, 0, 0]
    text_col = [232, 44, 12]
    if sec > 60:
        text_col = [255, 83, 13]
    if sec > 120:
        text_col = [104, 180, 46]
    seconde = str(sec%60)
    min = str(int(sec/60))
    if len(str(sec%60))<=1:
        seconde="0"+seconde;
    sec= min+":"+seconde
    my_image = myfont2.render(sec, True, text_col, bg_col)
    rect = my_image.get_rect()
    rect.center = [706,44]
    screen.blit(my_image, rect)
# fin Timer
#fin Déclaration
