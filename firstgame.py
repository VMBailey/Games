##############################################################################
# Libraries
##############################################################################
import pygame

##############################################################################
# Variables
##############################################################################
screenSize = (700,500)
screenColor = (50,50,50)  # Color currently set to grey
platformColor = (209, 206, 25)  # Color currently set to Mustard yellow....

##############################################################################
# Player
##############################################################################
playerImage = pygame.image.load('D:/n3ku/Pictures/Game Sprites/Adventurer/adventurer-idle-01.png')

##############################################################################
# Platforms - The list below will keep track of our platforms.
##############################################################################
platforms = [
    # Middle platform
    pygame.Rect(100, 300, 400, 50),

    # Left platform
    pygame.Rect(100, 250, 50, 50),

    # Right Platform
    pygame.Rect(450, 250, 50, 50)
]

##############################################################################
# Start Game
##############################################################################

# This command initializes the entire game. Without it, the game will not launch.
pygame.init()

 # This line creates a pop-up window.
screen = pygame.display.set_mode(screenSize)

# Changes the window's title
pygame.display.set_caption('The Wranglers') 

# Main Game Loop
running = True
while running:
    ##############################################################################
    # Input
    ##############################################################################
    # Game exit
    # This if statement will close the game
    # if the player clicks the window's "X".
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False            

    # Player Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ...
    if keys[pygame.K_RIGHT]:
        ...
    
    # update

    ##############################################################################
    # Drawing
    ##############################################################################
    # Background
    screen.fill (screenColor)  # This line will fill the pop-up window with color; following the RGB number format.

    # Platform
    for p in platforms:
        pygame.draw.rect(screen, platformColor, p)

    # Player
    screen.blit(playerImage, (300, 100))  # This line will draw the player onto the screen. The coordinates dictate where the sprite will appear on screen.

    # Visible screen
    pygame.display.flip()

# Quit
pygame.quit()