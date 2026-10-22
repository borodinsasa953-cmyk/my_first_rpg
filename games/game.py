import pygame
pygame.init()
screen = pygame.display.set_mode((900, 500))
running = True
pygame.display.set_caption('Рома лох')
icon = pygame.image.load('games/images/icon.png')
pygame.display.set_icon(icon)
square = pygame.Surface((50,170))
square.fill('Blue')

mufont = pygame.font.Font('SourceSansSchoolBold.tff', 40)
text_surface = mufont.render('ZETKA ZETKA', False, 'White')
while running:

    screen.blit(square,(100,100))
    screen.blit(text_surface,(300,100))
    pygame.draw.circle(screen,'Red', (7, 10,), 7)

    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit
        


            
    