"""
Classic snake game in python. Code was generated following the
tutorial at: https://www.edureka.co/blog/snake-game-with-pygame/
"""

# import required packages
import pygame # game development framework
import random # used to put food in random places on the screen
from snake import Snake, snake

# initialize the game
pygame.init()

# set the screen size
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))

# draw the screen
pygame.display.update()

# set a caption on the screen
pygame.display.set_caption('Snake game by Edureka and ISAT 252')

# variables to hold different colors
# TODO: remove unused colors
blue = (0,0,255)
red = (255,0,0)
yellow = (255,255,0)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)

# Game clock: controls the speed of the game loop
clock = pygame.time.Clock()
snake_speed = 10 # higher number = faster snake = harder game
snake_color = green
snake_block = 20 

# create a snake
snake = Snake(green, dis.width / 2, dis.height / 2)

# setup for messages to be displayed on the screen
font_style = pygame.font.SysFont(None, 50)

def display_score(score):
    '''Draws the score for the game on the screen'''
    value = font_style.render("Your Score: " + str(score), True, blue)
    dis.blit(value, [10, 10])

def draw_snake(segment_size, snake_list):
    '''Draws the segments of the snake'''
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], segment_size, segment_size])

def message(msg,color):
    '''Displays a message 'msg' in a 'color' on the screen, anchored in the middle'''
    mesg = font_style.render(msg, True, color)
    # TODO: figure out how to center the message on the screen and warp if it's too long
    dis.blit(mesg, [dis_width / 2, dis_height / 2])

def game_loop(): 
    '''Sets up and controls the main game loop'''
    # create a variable to keep track of whether or not the game is over
    game_over = False
    game_close = False  

    # variables to control the x/y coordinates and size of the snake head
    x1 = dis_width / 2
    y1 = dis_height / 2  
    x1_change = 0 
    y1_change = 0
    snake_list = []
    snake_length = 1 

        # get random x/y coordinates for the food
    foodx = (
            round(random.randrange(0, dis_width - snake_block) / snake_block)
            * snake_block
        )
    foody = (
            round(random.randrange(0, dis_height - snake_block) / snake_block)
            * snake_block
        )

    # the main game loop. this loop will run infinitely until the value
    # of 'game_over' changes from 'False' to 'True'
    while not game_over:
        while game_close == True:
                dis.fill(white)
                message("You Lost! Press Q-Quit or C-Play Again", blue)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # if someone clicks a key on the keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # left arrow key
                    snake.move('left')
                elif event.key == pygame.K_RIGHT: # right arrow key
                    snake.move('right')
                elif event.key == pygame.K_UP: # up arrow key
                    snake.move('up')
                elif event.key == pygame.K_DOWN: # down arrow key
                    snake.move('down')
        
        # set 'game_close' to True if the snake goes outside of the screen boundary
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        # draws red rectangle to represent the food
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        # estalish the location of the snake's head
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # makes sure we don't have a "phantom" or "extra" 
        if len(snake.segments) > snake.length:
                del snake.segments[0]
        
        # chech to see if the snake's head intersects with any of the snake body parts
        for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

        snake.draw(dis)
        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)

        # updates the surface (display area) with whatever changes
        # have been specified in this iteration through the game loop
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            # get random x/y coordinates for the food
            foodx = (
                round(random.randrange(0, dis_width - snake_block) / snake_block)
                * snake_block
            )
            foody = (
                round(random.randrange(0, dis_height - snake_block) / snake_block)
                * snake_block
            )
            snake_length += 1

        # sets clock speed; higher number = faster game (and more difficult!)
        clock.tick(snake_speed)

    # quit the game
    pygame.quit()
    quit()

game_loop()