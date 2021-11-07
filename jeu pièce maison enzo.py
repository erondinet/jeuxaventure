"""
Programme Réalisé par RONDINET,Enzo,1G2

"""
import time

print("Le but de ce jeu est de trouver et de rentrer dans le grenier. Bonne chance !")

cle=0

import pygame
pygame.init()
fenetre = pygame.display.set_mode((640, 360))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)
image1=pygame.image.load("vestibule.jpg")
image2=pygame.image.load("salle-a-manger.jpg")
image3=pygame.image.load("Garage.jpg")
image4=pygame.image.load("Salon.jpg")
image5=pygame.image.load("cuisine.jpg")
image6=pygame.image.load("Piscine.jpg")
image7=pygame.image.load("Terrasse.jpg")
image8=pygame.image.load("Jardin est.jpg")
image10=pygame.image.load("Jardin ouest.jpg")
image9=pygame.image.load("Grenier.jpg")
text1 = font.render("Vous vous trouvez dans le vestibule", True, (0, 255, 0))
text2 = font.render("Vous vous trouvez dans la salle à manger", True, (0, 255, 0))
text3 = font.render("Vous vous trouvez dans le garage", True, (255, 0, 255))
text4 = font.render("Vous vous trouvez dans le salon", True, (225, 0, 255))
text5 = font.render("Vous vous trouvez dans la cuisine", True, (162, 0, 255))
text6 = font.render("Vous vous trouvez dans la piscine", True, (150, 0, 255))
text7 = font.render("Vous vous trouvez dans la terrasse", True, (200, 0, 255))
text8 = font.render("Vous vous trouvez dans le jardin est", True, (180, 0, 255))
text10 = font.render("Vous vous trouvez dans le jardin ouest", True, (205, 0, 255))
text11 = font.render("vous vous trouvez dans la cuisine et vous venez de prendre la clé du grenier", True, (255, 0, 255))
text12 = font.render("vous vous trouvez dans la cuisine et vous avez déjà trouvé la clé", True, (255, 0, 255))
text13 = font.render("BRAVO!! Vous Venez de Reussir à pénétrer dans le Grenier", True, (255, 0, 255))

dansQuellePierceEstLePersonnage=1

def decrireLaPiece(piece):
    global cle
    if piece==1:
        fenetre.blit(image1,(0,0)) #afficher l'image à la prochaine actualisation
        fenetre.blit(text1,(0,300)) #afficher le texte à la prochaine actualisation
    elif piece==2:
        fenetre.blit(image2,(0,0)) #afficher l'image à la prochaine actualisation
        fenetre.blit(text2,(0,300)) #afficher le texte à la prochaine actualisation
    elif piece==3:
        fenetre.blit(image3,(0,0)) #afficher l'image à la prochaine actualisation
        fenetre.blit(text3,(0,300)) #afficher le texte à la prochaine actualisation
    elif piece==4:
        fenetre.blit(image4,(0,0)) #afficher l'image à la prochaine actualisation
        fenetre.blit(text4,(0,300)) #afficher le texte à la prochaine actualisation
    elif piece==5:
        fenetre.blit(image5,(0,0)) #afficher l'image à la prochaine actualisation
        fenetre.blit(text5,(0,300)) #afficher le texte à la prochaine actualisation
        fenetre.blit(text11,(0,320)) #afficher le texte à la prochaine actualisation
        cle=1
    elif piece==6:
        fenetre.blit(image6,(0,0)) #afficher l'image à la prochaine actualisation
        fenetre.blit(text6,(0,300)) #afficher le texte à la prochaine actualisation
    elif piece==7:
        fenetre.blit(image7,(0,0)) #afficher l'image à la prochaine actualisation
        fenetre.blit(text7,(0,300)) #afficher le texte à la prochaine actualisation
    elif piece==8:
        fenetre.blit(image8,(0,0)) #afficher l'image à la prochaine actualisation
        fenetre.blit(text8,(0,300)) #afficher le texte à la prochaine actualisation
    elif piece==9:
        fenetre.blit(image9,(0,0)) #afficher l'image à la prochaine actualisation
        fenetre.blit(text13,(0,320))
    elif piece==10:
        fenetre.blit(image10,(0,0)) #afficher l'image à la prochaine actualisation
        fenetre.blit(text10,(0,300)) #afficher le texte à la prochaine actualisation

def decision(direction,piece):
    global cle
    print("Vous désirez allez au",direction)
    memorisePiece=piece
    if direction=='n':
        if piece==1:
            piece=2
        elif piece==2:
            piece=4
        elif piece==3:
            piece=5
        elif piece==4:
            piece=6
        elif piece==5:
            piece=7
    elif direction=='s':
        if piece==6:
            piece=4
        elif piece==7:
            piece=5
        elif piece==4:
            piece=2
        elif piece==5:
            piece=3
        elif piece==2:
            piece=1
        elif piece==3:
            if cle==1:
                piece=9
            else:
                print("Il y a une trappe menant au grenier...seulement elle est fermée à clé !")
                time.sleep(2)
    elif direction=='e':
        if piece==10:
            piece=6
        elif piece==6:
            piece=7
        elif piece==7:
            piece=8
        elif piece==4:
            piece=5
        elif piece==2:
            piece=3
    elif direction=='o':
        if piece==8:
            piece=7
        elif piece==7:
            piece=6
        elif piece==6:
            piece=10
        elif piece==5:
            piece=4
        elif piece==3:
            piece=2
    if memorisePiece==piece:
        print("Déplacement impossible")
    return piece


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN: #lecture du clavier
            dansQuellePierceEstLePersonnage=decision(event.unicode,dansQuellePierceEstLePersonnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
    decrireLaPiece(dansQuellePierceEstLePersonnage)
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()







