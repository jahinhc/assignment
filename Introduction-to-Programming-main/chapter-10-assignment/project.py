# Welcome to your final project! In this project, you will create a two-player game called "Pong Invaders!".
# Most of the code has been provided for you. You will need to complete the code by adding the missing parts.
# Only add or modify the code where you are instructed to do so. Those instructions will be marked with TODO.
# The game will have two players, each controlling a spaceship. The goal of the game is to shoot the other player's spaceship.
# The game will have a maximum of 3 bullets for each player. The game will end when one of the players' health reaches 0.
# The game will display the winner and the health of each player at the top left and top right of the screen.
# The game will also play a sound when a bullet is fired and when a bullet hits a spaceship.
import pygame
import os
pygame.font.init()
pygame.mixer.init()

# Set the screen width and height
screen_width, screen_height = 900, 500

# TODO 1:
# Initialize the screen with the given width and height. Set the caption of the window to "Pong Invaders!"
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Invaders!")

# Define colors for the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Create a border for the middle of the screen
BORDER = pygame.Rect(screen_width//2 - 5, 0, 10, screen_height)

# Load the bullet hit and fire sounds
BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

# Set the font for the health and winner text
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# Set the frames per second, velocity of the spaceship and bullet, and the maximum number of bullets
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# Load the spaceship images and scale them to the given width and height
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# Load the space background and scale it to the screen width and height
SPACE_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (screen_width, screen_height))


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health, color):
        # TODO 2: Call the inherited class __init__ method
        super().__init__()
        
        
        self.color = color
        if self.color == 'red':
            self.image = RED_SPACESHIP
        if self.color == 'yellow':
            self.image = YELLOW_SPACESHIP
            
        # TODO 3:
        # Get the bounding rectangle of the image
        self.rect = self.image.get_rect()
        # TODO 4:
        # Assign the center of the rectangle to the given x and y coordinates
        self.rect.center = (x, y)
        # TODO 5:
        # Set the health of the spaceship
        self.health = health
        
    def update(self):
        keys = pygame.key.get_pressed()
        if self.color == 'red':
            # Red spaceship movement:
            # Up - K_w, Down - K_s, Left - K_a, Right - K_d
            # Implement the movement of the spaceship, check for the boundaries of the screen
            if keys[pygame.K_a] and self.rect.left > 0: self.rect.x -= VEL
            if keys[pygame.K_d] and self.rect.right < screen_width//2: self.rect.x += VEL
            if keys[pygame.K_w] and self.rect.top > 0: self.rect.y -= VEL
            if keys[pygame.K_s] and self.rect.bottom < screen_height: self.rect.y += VEL
        if self.color == 'yellow':
            # Yellow spaceship movement:
            # Up - K_UP, Down - K_DOWN, Left - K_LEFT, Right - K_RIGHT
            # TODO 6: Complete the movement of the yellow spaceship
            # This is similar to the red spaceship movement, but the keys and boundaries are different
        if keys[pygame.K_LEFT] and self.rect.left > screen_width // 2:
            self.rect.x -= VEL
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += VEL
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= VEL
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += VEL

            pass
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 5))
        self.color = color
        self.image.fill(color)
        
        # TODO 7: Compute the bounding rectangle of the image
        seself.rect = self.image.get_rect()
        # TODO 8: Assign the center of the rectangle to the given x and y coordinates
        self.rect.center = (x, y)
        
    def update(self):
        if self.color == RED:
            # For red bullets, move the bullet to the right. Use the BULLET_VEL to control the speed of the bullet
            # Check if the bullet collides with the yellow spaceship
            # If so, reduce the health of the yellow spaceship by 1, kill the bullet and play the BULLET_HIT_SOUND
            self.rect.x += BULLET_VEL
            if self.rect.colliderect(yellow):
                yellow.health -= 1
                self.kill()
                BULLET_HIT_SOUND.play()
        if self.color == YELLOW:
            # TODO 9: Do the same for the yellow bullets, but move the bullet to the left
            # For yellow bullets, move the bullet to the left (opposite direction from red bullets)
            # TODO 9: Implement the behavior for yellow bullets
            self.rect.x -= BULLET_VEL  # Example: Move left
            if self.rect.colliderect(red):
                red.health -= 1
                self.kill()
                BULLET_HIT_SOUND.play()
            pass
        
        # If the bullet goes off the screen, kill the bullet
        if self.rect.right < 0 or self.rect.left > screen_width:
            self.kill()

# TODO 10: Create a group for the spaceships, red bullets and yellow bullets
spaceship_group = pygame.sprite.Group()
red_bullet_group = pygame.sprite.Group()
yellow_bullet_group = pygame.sprite.Group()
# TODO 11: Initialize the red spaceship at (100, 300) with 10 health and color red
red = Spaceship(100, 300, 10, 'red')
# TODO 12: Initialize the yellow spaceship at (700, 300) with 10 health and color yellow
yellow = Spaceship(700, 300, 10, 'yellow')
# Add the red and yellow spaceships to the spaceship_group
spaceship_group.add(red)
spaceship_group.add(yellow)

clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    pygame.display.update()
    
    # TODO 13: Draw the background at (0, 0)
    screen.blit(SPACE_BG, (0, 0))
    
    # Draw the middle border
    pygame.draw.rect(screen, BLACK, BORDER)

    
    red_health_text = HEALTH_FONT.render("Health: " + str(red.health), 1, RED)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow.health), 1, YELLOW)
    
    # Display health for the yellow spaceship at the top right of the screen
    screen.blit(yellow_health_text, (screen_width - red_health_text.get_width() - 10, 10))
    
    # TODO 14: Display health for the red spaceship at the top left (10, 10) of the screen
    screen.blit(red_health_text, (10, 10))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # TODO 15: If the user clicks the close button, quit the game
            pass
    
        if event.type == pygame.KEYDOWN:
            # If the user presses the left control key (K_LCTRL) and the number of red bullets is less than MAX_BULLETS,
            # create a bullet at the center of the red spaceship and add it to the red_bullet_group
            # Play the BULLET_FIRE_SOUND
            if event.key == pygame.K_LCTRL and len(red_bullet_group) < MAX_BULLETS:
                bullet = Bullet(red.rect.centerx, red.rect.centery, RED)
                red_bullet_group.add(bullet)
                BULLET_FIRE_SOUND.play()
            # TODO 16: Do the same for the yellow spaceship, but use the right control key (K_RCTRL)
            if event.key == pygame.K_RCTRL and len(yellow_bullet_group) < MAX_BULLETS:
                bullet = Bullet(yellow.rect.centerx, yellow.rect.centery, YELLOW)
                yellow_bullet_group.add(bullet)
                BULLET_FIRE_SOUND.play()

                
    
    winner_text = ""
    if red.health <= 0:
        winner_text = "Yellow Wins!"
    if yellow.health <= 0:
        winner_text = "Red Wins!"
    if winner_text != "":
        # TODO 17: If there is a winner, display the winner text and continue the loop
    if winner_text != "":
        winner_surface = WINNER_FONT.render(winner_text, True, YELLOW if winner_text == "Red Wins!" else RED)
        screen.blit(winner_surface, (screen_width // 2 - winner_surface.get_width() // 2, screen_height // 2 - winner_surface.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(2000)
        continue

        pass
        continue

    # TODO 18: Draw the spaceships, red bullets and yellow bullets
# Draw the spaceships
screen.blit(red.image, red.rect)
screen.blit(yellow.image, yellow.rect)

# Draw the red bullets
for bullet in red_bullet_group:
    screen.blit(bullet.image, bullet.rect)

# Draw the yellow bullets
for bullet in yellow_bullet_group:
    screen.blit(bullet.image, bullet.rect)

    
# TODO 19: Update the spaceships, red bullets and yellow bullets
# Update the spaceships
spaceship_group.update()

# Update the red bullets
red_bullet_group.update()

# Update the yellow bullets
yellow_bullet_group.update()

    
    
