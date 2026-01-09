import pygame
import random
import sys 
import os

# Initialize Pygame
pygame.init()

# clock and frames per second (fps)
clock = pygame.time.Clock()
fps = 60

# screen dimensions
screen_width = 855
screen_height = 936

# make a game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FlapDash")

# define fonts and colors
font1 = pygame.font.SysFont('Bauhaus 93', 60)
font2 = pygame.font.SysFont('Bauhaus 93', 30)
font3 = pygame.font.SysFont('Silkscreen', 60)

white = (255, 255, 255)
dark_red = (200, 0, 0)

# initialize variables for game elements and state
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
game_started = False
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
high_score = 0
pass_pipe = False
died_sound_played = False

# load game assets (images, buttons, etc.)
bg = pygame.image.load('bg.png').convert_alpha()
ground_img = pygame.image.load('ground.png').convert_alpha()
button1_img = pygame.image.load('restart1.png').convert_alpha()
button2_img= pygame.image.load('exit.png').convert_alpha()
button3_img= pygame.image.load('play.png').convert_alpha()


# function to draw text with an outline
def draw_text_with_outline(text, font, text_col, outline_col, x, y):
    # text to create the outline
    outline_text = font.render(text, True, outline_col)
    
    # text in the desired color
    main_text = font.render(text, True, text_col)
    
    # blit the outline text with a slight offset
    screen.blit(outline_text, (x - 2, y - 2))  # Adjust the offset as needed
    screen.blit(outline_text, (x + 2, y - 2))  # Adjust the offset as needed
    screen.blit(outline_text, (x - 2, y + 2))  # Adjust the offset as needed
    screen.blit(outline_text, (x + 2, y + 2))  # Adjust the offset as needed
    
  # blit the main text in the desired color
    screen.blit(main_text, (x, y))

# function to display the game title
def show_game_title():
    dark_red = (200, 0, 0) 
    black = (0, 0, 0) 

    # game title with an outline
    draw_text_with_outline("FlapDash", font3, dark_red, black, float(screen_width / 3.2), int(screen_height / 4))

# function to draw text on the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# function for the main menu loop
def main_menu():
    while True:
        screen.blit(bg, (0, 0))
        show_game_title()
        play_button.draw()

# function to reset the game state
def reset_game():
        global score, pipe_frequency, scroll_speed
        pipe_group.empty()
        flappy .rect.x = 100
        flappy.rect.y = int(screen_height / 2)
        score = 0
        pipe_frequency = 1500
        scroll_speed = 4
        return score

# class for the player character
class Ibon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.blue_bird_images = []
        self.green_bird_images = []
        self.red_bird_images = []
        self.yellow_bird_images = []
        
        # Load birdie images
        for num in range(1, 5):
            img = pygame.image.load(f'blue_bird{num}.png')
            self.blue_bird_images.append(img)
        
        for num in range(1, 5):
            img = pygame.image.load(f'green_bird{num}.png')
            self.green_bird_images.append(img)

        for num in range(1, 5):
            img = pygame.image.load(f'red_bird{num}.png')
            self.red_bird_images.append(img)

        for num in range(1, 5):
            img = pygame.image.load(f'yellow_bird{num}.png')
            self.yellow_bird_images.append(img)
        
        # randomly select a bird image type ( feature no.3 - randomized bird)
        bird_type = random.choice(['blue_bird', 'green_bird', 'red_bird', 'yellow_bird'  ])
        
        if bird_type == 'blue_bird':
            self.images = self.blue_bird_images
        elif bird_type == 'green_bird':
            self.images = self.green_bird_images
        elif bird_type == 'red_bird':
            self.images = self.red_bird_images
        elif bird_type == 'yellow_bird':
            self.images = self.yellow_bird_images
        
        self.index = 0
        self.counter = 0
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False
        self.flying_sound = pygame.mixer.Sound('flying_sound.mp3')
        self.flying_sound.set_volume(0.5)


    def update(self):
        global flying  

        if flying:  
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        keys = pygame.key.get_pressed()  # check for keyboard input

        if game_over == False:
            # jump motion
            if keys[pygame.K_SPACE] and self.clicked == False:
                self.clicked = True
                self.vel = -10
                self.flying_sound.play()    

            if not keys[pygame.K_SPACE]:
                self.clicked = False

                self.counter += 1
                flap_cooldown = 5

                if self.counter > flap_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images):
                        self.index = 0
                self.image = self.images[self.index]
                self.image = pygame.transform.rotate(self.images[self.index], self.vel * -3)
        else: 
            self.image = pygame.transform.rotate(self.images[self.index], -90)


# class for the pipes
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):  
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pipe.jpg')
        self.rect = self.image.get_rect()
        self.pipe_gap = pipe_gap

        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]  
        elif position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

# class for the buttons
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):  
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

# to check if the 'score.text' file exists
if os.path.exists('score.text'):
    with open('score.text', 'r') as file:
        file_content = file.read().strip()
        if file_content:
            high_score = int(file_content)
        else:
             high_score = 0
else:
    high_score = 0

# sprite groups for game elements
ibon_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

# player character (ibon)
flappy = Ibon(100, int(screen_height / 2))  
ibon_group.add(flappy)

# buttons for the game
button1 = Button(screen_width // 2 - 100, screen_height // 2, button1_img)
button2 = Button(screen_width // 2 + 100, screen_height // 2, button2_img)
button3 = Button(screen_width // 2 , screen_height // 2, button3_img)

# main game loop
run = True
while run:
    clock.tick(fps)

    # score and game difficulty ( feature no.2 - whimsical levels)
    if score == 5:
        scroll_speed += 0.01
        pipe_frequency -= 2
    elif score == 10:
        scroll_speed += 0.012
        pipe_frequency -= 2
    elif score == 20:
        scroll_speed += 0.014
        pipe_frequency -= 2
    elif score == 30:
        scroll_speed += 0.016
        pipe_frequency -= 3
    elif score == 40:
        scroll_speed += 0.018
        pipe_frequency -= 3
    elif score == 50:
        scroll_speed += 0.020
        pipe_frequency -= 3
    elif score == 60:
        scroll_speed += 0.022
        pipe_frequency -= 4
    elif score == 70:
        scroll_speed += 0.024
        pipe_frequency -= 4
    elif score == 80:
        scroll_speed += 0.026
        pipe_frequency -= 4
    elif score == 90:
        scroll_speed += 0.028
        pipe_frequency -= 5
    elif score == 100:
        scroll_speed += 0.030
        pipe_frequency -= 5
    
    # handle game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and game_started and not flying and not game_over:
            flying = True

        mouse_pos = pygame.mouse.get_pos()
            
        if button1.rect.collidepoint(mouse_pos):
                game_started = True

# background and game elements
    screen.blit(bg, (0, 0))
    ibon_group.draw(screen)
    ibon_group.update()
    pipe_group.draw(screen)
    screen.blit(ground_img, (ground_scroll, 768))

# to display scores and high score if the game has started
    if game_started:
        draw_text(str(score), font1 ,white, float(screen_width / 2.1),150)
        draw_text(f"High Score: {high_score}", font2, white, 50, 150)

# logic for scoring and collision detection
    if len(pipe_group) > 0:
        if ibon_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
             and ibon_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
             and pass_pipe == False:
             pass_pipe = True
        if pass_pipe == True:
              if ibon_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                    score += 1
                    pass_pipe = False
                    score_sound = pygame.mixer.Sound('score_sound.mp3')
                    score_sound.set_volume(0.5)
                    score_sound.play()

# high score can be updated in the 'score.text' file
    if score > high_score:
            high_score = score
            with open('score.text', 'w') as file:
                file.write(str(high_score))
    
# handle collision and game over conditions
    died_sound = pygame.mixer.Sound('died_sound.mp3')
    died_sound.set_volume(0.5)
    if pygame.sprite.groupcollide(ibon_group, pipe_group, False, False) or flappy.rect.top < 0 or flappy.rect.bottom >= 768:
           game_over = True
           flying = False

    # play died sound if it hasn't been played ye
    if died_sound_played == False :
                died_sound.play()
                died_sound_played = True
   
    # logic for ongoing gameplay
    if game_over == False and flying == True:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)

            bottom_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
            top_pipe = Pipe(screen_width, int(screen_height / 2)+ pipe_height, 1)
            pipe_group.add(bottom_pipe)  
            pipe_group.add(top_pipe)
            last_pipe = time_now    
            ground_scroll -= scroll_speed
            
        if abs(ground_scroll) > 35:
            ground_scroll = 0
            
        pipe_group.update()

# display game title and play button if the game hasn't started yet
    if not game_started:
        show_game_title()
        play_button = Button(screen_width // 2, screen_height // 2, button3_img)
        play_button.draw()
    
    # to check if the play button is clicked before the game start
    if  game_started == True:
        play_button.draw

    if event.type == pygame.MOUSEBUTTONDOWN:
        if play_button.rect.collidepoint(event.pos):
            game_started = True

 # to check if buttons are clicked for restart or exit
    if game_over == True: 
        if button1.draw() == True:
            game_over = False
            score = reset_game()
            died_sound_played = False
        if button2.draw() == True:
            sys.exit()
        
    pygame.display.update()

pygame.quit()