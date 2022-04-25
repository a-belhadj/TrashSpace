import pygame
import math
import random
import time
import utils
size = (w, h) = 768, 768
REGLAGE_IUT = False
MULTIPLICATEUR = 0
if REGLAGE_IUT:
    MULTIPLICATEUR = 2
else:
    MULTIPLICATEUR = 1.5

class Plateform(pygame.sprite.Sprite):

    def __init__(self, nbP, rect):
        super().__init__()
        # ox, oy centre de la platforme r son rayon
        # nbP ses poubelle
        self.poubelles = []
        self.rect = rect
        self.rayonCercle =rect.width/2

    def draw(self, win):
        pygame.draw.ellipse(win, (0, 0, 0), self.rect, 2)

    def collide(self,unDechet):
        xr1 = utils.getXCentre(unDechet.x)
        yr1 = utils.getYCentre(unDechet.y)

        if math.hypot(xr1, yr1) >= self.rayonCercle - unDechet.width/3*2:
            px = unDechet.x
            py = unDechet.y
            cptx = w / 2
            cpty = h / 2

            circN = (pygame.math.Vector2(cptx - px, cpty - py)).normalize()
            vecI = pygame.math.Vector2(math.cos(unDechet.angle), math.sin(unDechet.angle))
            vecR = vecI - 2 * circN.dot(vecI) * circN

            unDechet.angle = math.atan2(vecR[1], vecR[0])

            unDechet.derniereCollision = None



class Poubelle(pygame.sprite.Sprite):
    def __init__(self, pos, typeDechet=1):
        super().__init__()
        self.type = str(typeDechet)
        pos = math.radians(pos)
        self.angle = pos  # en radiant
        self.image = pygame.image.load("image/p" + self.type + ".png").convert_alpha()
        self.rect = self.image.get_rect()
        self.taille = self.rect.width * 0.5

        self.image = pygame.transform.scale(self.image, (int(self.taille), int(self.rect.height * 0.5)))
        self.image = pygame.transform.rotate(self.image, math.degrees(self.angle + math.pi / 2 + math.pi))
        self.x = int(w / 2 + math.cos(self.angle) * 0.93 * h / 2)
        self.y = int(h / 2 - math.sin(self.angle) * 0.93 * h / 2)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.rect.width = self.taille
        self.tailleAngle = self.taille / (0.95 * h / 2)
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win):
        win.blit(self.image, self.rect)




class Scrapy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        ox = w / 2
        oy = h / 2
        ray = 0.95 * h / 2

        #image
        self.image0 = pygame.image.load("image/scrapi0.png").convert_alpha()
        self.image1 = pygame.image.load("image/scrapi1.png").convert_alpha()
        self.image2 = pygame.image.load("image/scrapi2.png").convert_alpha()

        pos = random.uniform(0,math.pi*2)
        self.angle = pos  # en radiant
        self.imageInit = self.image0
        self.rect = self.imageInit.get_rect(center=(ox, oy))
        self.imageInit = pygame.transform.scale(self.imageInit,
                                                (int(self.rect.width * 0.3), int(self.rect.height * 0.3)))
        self.image = pygame.transform.rotate(self.imageInit, math.degrees(self.angle + math.pi / 2))
        self.mask = pygame.mask.from_surface(self.image)
        self.tirEnCour = False
        self.lastFrame = 0



    def draw(self, win):

        ox = w / 2
        oy = h / 2
        ray = 0.95 * h / 2

        x = ox + (ray - 149) * math.cos(self.angle)
        y = oy - (ray - 149) * math.sin(self.angle)
        self.rect = self.image.get_rect(center=(x, y))

        win.blit(self.image, self.rect)

    def deplacer(self, direction):
        if direction == -1:
            self.angle += 1.6*2*math.pi /360*MULTIPLICATEUR
            self.image = pygame.transform.rotate(self.imageInit, math.degrees(self.angle + math.pi / 2))
        elif direction == 1:
            self.angle -= 1.6*2*math.pi /360*MULTIPLICATEUR
            self.image = pygame.transform.rotate(self.imageInit, math.degrees(self.angle + math.pi / 2))
        else:
            print("position differente de 1 ou -1")

        self.mask = pygame.mask.from_surface(self.image)


    def tirer(self, frame):
        ox = utils.getXCentre()
        oy = utils.getYCentre()
        if frame > self.lastFrame:
            self.tirEnCour = True
        else:
            self.tirEnCour = False
        if frame == 0:
            self.imageInit = self.image0
        elif frame == 1:
            self.imageInit = self.image1
        elif frame == 2:
            self.imageInit = self.image2

        self.rect = self.imageInit.get_rect(center=(ox, oy))
        self.imageInit = pygame.transform.scale(self.imageInit,
                                                (int(self.rect.width * 0.3), int(self.rect.height * 0.3)))
        self.image = pygame.transform.rotate(self.imageInit, math.degrees(self.angle + math.pi / 2))
        self.mask = pygame.mask.from_surface(self.image)
        self.lastFrame = frame

    def tirerUnDechet(self,unDechet):
        unDechet.angle = -self.angle - math.pi
        unDechet.accelerer()
        unDechet.derniereCollision = None



class Dechet(pygame.sprite.Sprite):

    VITESSE_MAX = 3*MULTIPLICATEUR
    VITESSE_MIN = 0.5*MULTIPLICATEUR

    def __init__(self, x, y, type=1, speed=0.5):
        super().__init__()

        self.type = str(type)

        self.width = 60
        self.height = self.width

        self.x = x
        self.y = y

        self.speed = speed
        self.angle = self.getBonAngle() + random.uniform(-math.pi/2,math.pi/2)

        self.image = pygame.image.load("image/dechet_" + self.type + ".png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, math.degrees(random.randint(0, 360)))
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.x, self.y)

        self.derniereCollision = None

    def getBonAngle(self):
        px = self.x
        py = self.y
        cptx = w / 2
        cpty = h / 2

        circN = pygame.math.Vector2(cptx - px, cpty - py)


        return math.atan2(circN[1], circN[0])

    def move(self):
        mvx = math.cos(self.angle) * self.speed
        mvy = math.sin(self.angle) * self.speed
        self.x += mvx
        self.y += mvy
        self.rect.x = self.x - self.width / 2
        self.rect.y = self.y - self.height / 2

    def draw(self, win):
        self.move()
        win.blit(self.image, self.rect)


    def ralentir(self):
        self.speed = max(Dechet.VITESSE_MIN, self.speed - 0.05)


    def accelerer(self):
        self.speed = Dechet.VITESSE_MAX
