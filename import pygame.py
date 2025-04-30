import pygame

pygame.init()


#ablak------------------------------------------------------------------------------------------------------------------------
ABLAK_HOSSZ, ABLAK_MAGASSAG = 1900, 900

pygame.display.set_caption("Battlebagoly 1.0")

ABLAK = pygame.display.set_mode((ABLAK_HOSSZ , ABLAK_MAGASSAG))
icon=pygame.image.load("assets\Icon.png")
pygame.display.set_icon(icon)
#FPS--------------------------------------------------------------------------------------------------------------------------
FPS=60
oratick=pygame.time.Clock()

BATTLEBAGOLY1_JOBB=pygame.image.load("assets\Battlebagoly.png")
BATTLEBAGOLY1_BAL=pygame.image.load("assets\Battlebagoly_bal.png")
BATTLEBAGOLY2_JOBB=pygame.image.load("assets\Battlebagoly2.png")
BATTLEBAGOLY2_BAL=pygame.image.load("assets\Battlebagoly2_bal.png")
    
BATTLEBAGOLY1_HOSSZ, BATTLEBAGOLY1_MAGASSAG=70,85
BATTLEBAGOLY2_HOSSZ, BATTLEBAGOLY2_MAGASSAG=70,85
    
BATTLEBAGOLY1_TRANSFORM_JOBB = pygame.transform.scale(BATTLEBAGOLY1_JOBB,(BATTLEBAGOLY1_HOSSZ,BATTLEBAGOLY1_MAGASSAG))
BATTLEBAGOLY1_TRANSFORM_BAL = pygame.transform.scale(BATTLEBAGOLY1_BAL,(BATTLEBAGOLY1_HOSSZ,BATTLEBAGOLY1_MAGASSAG))
BATTLEBAGOLY2_TRANSFORM_JOBB = pygame.transform.scale(BATTLEBAGOLY2_JOBB,(BATTLEBAGOLY2_HOSSZ,BATTLEBAGOLY2_MAGASSAG))
BATTLEBAGOLY2_TRANSFORM_BAL = pygame.transform.scale(BATTLEBAGOLY2_BAL,(BATTLEBAGOLY2_HOSSZ,BATTLEBAGOLY2_MAGASSAG))
    
jatekos1_x, jatekos1_y=560,615
jatekos2_x, jatekos2_y=700,615
fszin=(139,69,19)
foldy=700
    
    
jatekos1=pygame.Rect((jatekos1_x, jatekos1_y, BATTLEBAGOLY1_HOSSZ, BATTLEBAGOLY1_MAGASSAG))
jatekos2=pygame.Rect((jatekos2_x, jatekos2_y, BATTLEBAGOLY2_HOSSZ, BATTLEBAGOLY2_MAGASSAG))

platform1=pygame.Rect((200,400,500,50))
platform2=pygame.Rect((1200,400,500,50))
fold=pygame.Rect((0, foldy, ABLAK_HOSSZ, 300))

#fizika------------------------------------------------------------------------------------------------------------------------
GRAVITACIO = 0.5
ugrasmagassag1=19
ugrassebesseg1=ugrasmagassag1
ugrasmagassag2=19
ugrassebesseg2=ugrasmagassag2
GYORSULAS=5
ugrik1=False
ugrik2=False
jobb1=True
jobb2=False
platform1_jatekos1_vertical=False
platform1_jatekos1_esik=False
platform1_jatekos1_collide=False
collide1=False

jatekos1hp=200
jatekos2hp=200


    
#game loop----------------------------------------------------------------------------------------------------------------------
fut = True

while fut:
    oratick.tick(FPS)
    for input in pygame.event.get():
        if input.type == pygame.QUIT:
            fut = False
            
    KEK=(135,206,235)
    FEHER=(255,255,255)
    ABLAK.fill(KEK)
    if jobb1:
        ABLAK.blit(BATTLEBAGOLY1_TRANSFORM_JOBB, (jatekos1_x, jatekos1_y))
    else:
        ABLAK.blit(BATTLEBAGOLY1_TRANSFORM_BAL, (jatekos1_x, jatekos1_y))
    if jobb2:
        ABLAK.blit(BATTLEBAGOLY2_TRANSFORM_JOBB, (jatekos2_x, jatekos2_y))
    else:
        ABLAK.blit(BATTLEBAGOLY2_TRANSFORM_BAL, (jatekos2_x, jatekos2_y))
    
    pygame.draw.rect(ABLAK, fszin, fold)
         
    pygame.draw.rect(ABLAK,fszin,platform1)
    pygame.draw.rect(ABLAK,fszin,platform2)
    pygame.display.update()


    #if jatekos1_y+BATTLEBAGOLY1_MAGASSAG>foldy:
        #jatekos1_y+=GRAVITACIO


    #if jatekos2_y+BATTLEBAGOLY2_MAGASSAG>foldy:
        #jatekos2_y+=GRAVITACIO



    if jatekos1.colliderect(platform1):
        collide1=True
        print("yes")


        

    billenytu=pygame.key.get_pressed()  

    if billenytu[pygame.K_a] and jatekos1_x> 0:
        jatekos1_x-=GYORSULAS
        jobb1=False
    if billenytu[pygame.K_d] and jatekos1_x < ABLAK_HOSSZ-BATTLEBAGOLY1_HOSSZ:
        jatekos1_x +=GYORSULAS
        jobb1=True
    if  not ugrik1 and billenytu[pygame.K_w]:
        ugrik1=True
    if ugrik1:

        jatekos1_y-=ugrassebesseg1
        ugrassebesseg1 -=GRAVITACIO
        if ugrassebesseg1<0:
            platform1_jatekos1_esik=True
        else:
            platform1_jatekos1_esik=False

        if ugrassebesseg1 < -ugrasmagassag1:
            ugrik1=False
            ugrassebesseg1=ugrasmagassag1


    if billenytu[pygame.K_LEFT] and jatekos2_x> 0:
        jatekos2_x-=GYORSULAS
        jobb2=False
    if billenytu[pygame.K_RIGHT] and jatekos2_x < ABLAK_HOSSZ-BATTLEBAGOLY2_HOSSZ:
        jatekos2_x +=GYORSULAS
        jobb2=True
    if  not ugrik2 and billenytu[pygame.K_UP]:
        ugrik2=True
    if ugrik2:
        jatekos2_y-=ugrassebesseg2
        ugrassebesseg2 -=GRAVITACIO
        if ugrassebesseg2 < -ugrasmagassag2:
            ugrik2=False
            ugrassebesseg2=ugrasmagassag2

pygame.quit()
        