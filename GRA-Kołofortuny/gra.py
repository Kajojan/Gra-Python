import pygame
import os
pygame.init()
pygame.display.set_caption("Koło Fortuny")
okno = pygame.display.set_mode((765,435))
run = True
FPS=60
clock = pygame.time.Clock()
Start= pygame.image.load(os.path.join('Pliki','start.jpg'))
guzik=pygame.rect.Rect(0,0,300,100)
square = pygame.Rect((330,350), (100,32))

font = pygame.font.SysFont(None, 30)

def ms(msg,color):
    okno_text= font.render(msg, True, color)
    okno.blit(okno_text, [330,350])



while run:
    clock.tick(FPS)
    okno.blit(Start, (0, 0))
    pygame.draw.rect(okno, (100, 200, 250), square)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.:
            ms("Koniec", (255,255,255))
            pygame.display.update()


pygame.quit()