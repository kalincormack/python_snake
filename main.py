"""
Classic snake game in python. Code was generated following the
tutorial at: https://www.edureka.co/blog/snake-game-with-pygame/
"""

# import required packages
import pygame # game development framework
import random # used to put food in random places on the screen
from snake import Snake, snake
from colors import blue, green, red, white

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

# Game clock: controls the speed of the game loop
clock = pygame.time.Clock()
snake_speed = 10 # higher number = faster snake = harder game
snake_color = green
snake_block = 20 

# setup for messages to be displayed on the screen
font_style = pygame.font.SysFont(None, 50)

def display_score(score):
    '''Draws the score for the game on the screen'''
    value = font_style.render("Your Score: " + str(score), True, blue)
    dis.blit(value, [10, 10])

# def draw_snake(segment_size, snake_list):
#     '''Draws the segments of the snake'''
#     for x in snake_list:
#         pygame.draw.rect(dis, snake_color, [x[0], x[1], segment_size, segment_size])

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

    # create a snake
    snake = Snake(green, dis_width / 2, dis_height / 2)

        # get random x/y coordinates for the food
    foodx = (
            round(random.randrange(0, dis_width - snake.head_size) / snake.head_size)
            * snake.head_size
        )
    foody = (
            round(random.randrange(0, dis_height - snake.head_size) / snake.head_size)
            * snake.head_size
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
        if snake.x >= dis_width or snake.x < 0 or snake.y >= dis_height or snake.y < 0:
            game_over = True
        
        snake.move()
        dis.fill(white)

        # draws red rectangle to represent the food
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        # chech to see if the snake's head intersects with any of the snake body parts
        game_close = snake.has_crashed()

        snake.draw(dis)
        # draw_snake(snake_block, snake_list)
        display_score(snake.length - 1)

        # updates the surface (display area) with whatever changes
        # have been specified in this iteration through the game loop
        pygame.display.update()

        if snake.x == foodx and snake.y == foody:
            # get random x/y coordinates for the food
            foodx = (
                round(random.randrange(0, dis_width - snake_block) / snake_block)
                * snake_block
            )
            foody = (
                round(random.randrange(0, dis_height - snake_block) / snake_block)
                * snake_block
            )
            snake.grow()

        # sets clock speed; higher number = faster game (and more difficult!)
        clock.tick(snake_speed)

    # quit the game
    pygame.quit()
    quit()

game_loop()