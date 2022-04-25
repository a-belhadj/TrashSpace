import math
import pygame
import model
import time
import random

size = (w, h) = 768, 768
def CircleCollide(dechet1:model.Dechet, dechet2:model.Dechet):
    px = dechet1.x
    py = dechet1.y

    cptx = dechet2.x
    cpty = dechet2.y

    circN = (pygame.math.Vector2(cptx - px, cpty - py)).normalize()
    vecI = pygame.math.Vector2(math.cos(dechet1.angle), math.sin(dechet1.angle))
    # print(math.degrees(math.atan2(vecI[0], vecI[1])))
    vecR = vecI - 2 * circN.dot(vecI) * circN

    dechet1.angle = math.atan2(vecR[1], vecR[0])
    dechet2.angle = math.pi + dechet1.angle
    speedTotal = dechet1.speed + dechet2.speed
    dechet1.speed, dechet2.speed = speedTotal / 2, speedTotal / 2;
    dechet1.derniereCollision = dechet2
    dechet2.derniereCollision = dechet1

def getXCentre(x=0):
    return x - 768/2

def getYCentre(y=0):
    return -(y - 768/2)

def getXYDechet():
    rayonCercle = (0.95 * 768) / 2

    angle = random.uniform(0,math.pi*2)
    rayonApparition = random.uniform(0,rayonCercle-60)
    x = 768 / 2 + math.cos(angle)*rayonApparition
    y = 768 / 2 + math.sin(angle)*rayonApparition

    return x,y

def CollideTrash(Circle, unePoubelle: model.Poubelle):
    # poubelle
    x = Circle.x - w / 2
    y = Circle.y - h / 2
    angle= math.atan2(y, x)
    xr1 = Circle.x - (w / 2)
    yr1 = Circle.y - (h / 2)

    murTouche = math.hypot(xr1, yr1) + Circle.width / 2 >= 0.95 * h / 2

    if angle > (-unePoubelle.angle - unePoubelle.tailleAngle/2) and angle < (-unePoubelle.angle + unePoubelle.tailleAngle/2) and murTouche:
        return True
    else:
        return False


def collision(sprite, group):
    rectCol = pygame.sprite.spritecollide(sprite, group, False)
    return [s for s in rectCol if pygame.sprite.collide_mask(sprite, s)]


class Score:
    def __init__(self):
        self.val = 0
        self.lvl = 1
        self.scarpSpeed = 0.7
        self.nbMaxType = 1
        self.combo = 1
        self.nbTriReussi = 0
        self.nbTriRate = 0
        self.comboMax = 0
        self.augmentationNiv = [300, 400, 600, 750, 900, 1200, 1400, 1600, 1800]
        self.apparitions = [6, 5, 4, 3, 3, 3, 2, 1, 1]
        self.nbDechetMax = [3, 3, 3, 3, 4, 4, 4, 4, 5]

    def score_plus(self):
        self.val += 100*self.combo
        self.nbTriReussi += 1
        if self.combo < 9:
            self.combo += 1
            if self.combo > self.comboMax:
                self.comboMax = self.combo
        if self.val >= self.lvl*self.augmentationNiv[self.lvl - 1]:
            if self.lvl < 9:
                self.lvl += 1
                if self.lvl > 3 and self.scarpSpeed < 2.5:
                    self.scarpSpeed += 0.05
                return True
        return False

    def score_moins(self):
        self.nbTriRate += 1
        self.val += 10
        self.combo = 1
        if self.val < 0:
            self.val = 0

    def affichage(self, win, nImg):
        nImg = str(nImg)
        info = pygame.image.load("image/new_dechet_"+nImg+".png").convert_alpha()
        win.blit(info, (100, 300))
        pygame.display.flip()
        time.sleep(2)

    def finDuJeu(self):
        print("COMBO MAX ATTEINT: ", self.comboMax)
        print("DECHETS TRIES: ", self.nbTriReussi)
        print("DECHETS PERDUS: ", self.nbTriRate)
