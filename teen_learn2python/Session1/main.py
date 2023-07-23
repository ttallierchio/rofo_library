import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
circle_vector = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
adjust_x = -300
adjust_y = -300
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    if circle_vector.x <=0 or circle_vector.x >= screen.get_width():
        adjust_x *= -1
    if circle_vector.y <= 0 or circle_vector.y >= screen.get_height():
        adjust_y *= -1
    pygame.draw.circle(screen,"red",circle_vector,12)
    circle_vector.x -= adjust_x * dt
    circle_vector.y -= adjust_y * dt 
    # flip() the display to put your work on screen
    pygame.display.flip()    
    dt = clock.tick(60)/1000  # limits FPS to 60
    print(dt,circle_vector)

pygame.quit()