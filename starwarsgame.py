import pygame
import random

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('The Mandalorian: Journey')

bg = pygame.image.load('bg.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

tie = pygame.image.load('tiefighter.png').convert_alpha()
tie = pygame.transform.scale(tie, (50,50))

playerImg = pygame.image.load('razorcrest.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (50,50))#converte o tamanho da nave
playerImg = pygame.transform.rotate(playerImg, -90)

blaster = pygame.image.load('blaster.png').convert_alpha()
blaster = pygame.transform.scale(blaster, (50,50))

pos_tie_x = 500
pos_tie_y = 360

pos_player_x = 200
pos_player_y = 300

vel_blaster_x = 0
pos_blaster_x = 200
pos_blaster_y = 300

triggered = False

rodando = True

#funções
def respawn():
    x = 1350
    y = random.randint(1, 640)
    return [x,y]


while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0)) #cria background
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    #comandos
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -=1

        if not triggered:
            pos_blaster_y -=1

    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y +=1

        if not triggered:
            pos_blaster_y +=1

    if tecla[pygame.K_SPACE]:
        triggered = True

    #respawn
    if pos_tie_x == 5:
        pos_tie_x = respawn()[0]
        pos_tie_y = respawn()[1]

    #loop
    x-=0.5
    pos_tie_x -=1

    pos_blaster_x += vel_blaster_x

    #criar imagens
    screen.blit(tie, (pos_tie_x, pos_tie_y))
    screen.blit(blaster, (pos_blaster_x,pos_blaster_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))

    pygame.display.update()