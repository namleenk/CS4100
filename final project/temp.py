import pygame
import time
import random

pygame.init()

# colors for food and snake
green = (60, 179, 113)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
purple = (160, 32, 240)

# screen set-up
bkg_width = 600
bkg_height = 400
bkg=pygame.display.set_mode((bkg_width,bkg_height))
pygame.display.update()
pygame.display.set_caption('Snake')
font_style = pygame.font.SysFont(None, 20)

# snake set-up
snake_size = 10
snake_speed = 15

clock = pygame.time.Clock()

def score(score):
    value = font_style.render("Your score: " + str(score), True, purple)
    bkg.blit(value, [0, 0])

# function to display the given text in the given color, at the center of the screen
def message(text, color):
    output = font_style.render(text, True, color)
    # center the words
    text_rect = output.get_rect()
    text_rect.center = (bkg_width / 2, bkg_height / 2)
    # overlay the text onto the background
    bkg.blit(output, text_rect)

# Display snake as it gets longer
def build_snake(snake_size, snake_list):
    for s in snake_list:
        pygame.draw.rect(bkg, black, [s[0], s[1], snake_size, snake_size])


# game mechanics
def gameLoop():
    game_over = False
    game_close = False
    # starting location of snake
    x_loc = bkg_width / 2
    y_loc = bkg_height / 2

    # how much snake moves by
    delta_x = 0
    delta_y = 0

    # track snake's length
    snake_list = []
    snake_length = 1

    # random location for the food
    food_x = round(random.randrange(0, bkg_width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, bkg_height - snake_size) / 10.0) * 10.0

    while not game_over:
        
        # controls to play the game again
        while game_close == True:
            bkg.fill(green)
            message('You lost, Press q to quit or r to play again', red)
            score(snake_length - 1)
            
            pygame.display.update()

            # key logic for quitting or playing again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            # if the user wants to quit before the game is over, they should be able to click the red x on the window
            if event.type==pygame.QUIT:
                game_over=True
            # handle key presses by the user
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -(snake_size)
                    delta_y = 0
                elif event.key == pygame.K_RIGHT:
                    delta_x = snake_size
                    delta_y = 0
                elif event.key == pygame.K_UP:
                    delta_x = 0
                    delta_y = -(snake_size)
                elif event.key == pygame.K_DOWN:
                    delta_x = 0
                    delta_y = snake_size
        # if the snake goes out of bounds, the game is over
        if (x_loc >= bkg_width or x_loc < 0 or y_loc >= bkg_height or y_loc < 0):
            game_close = True
        # update the x and y locations of snake depending on the key that was pressed
        x_loc += delta_x
        y_loc += delta_y
        # set the background color
        bkg.fill(green)
        # draw the food on the screen
        pygame.draw.rect(bkg, red, [food_x, food_y, snake_size, snake_size])
        
        snake_head =[]
        snake_head.append(x_loc)
        snake_head.append(y_loc)
        snake_list.append(snake_head)

        # if the snake pieces get too long, delete the head
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        # for every piece of the snake in the list, if it collides with the rest of the snake it's game over
        for s in snake_list[:-1]:
            if s == snake_head:
                game_close = True

        build_snake(snake_size, snake_list)
        score(snake_length - 1)

        pygame.display.update()

        # generate a new piece of food once the current piece is eaten
        if x_loc == food_x and y_loc == food_y:
            food_x = round(random.randrange(0, bkg_width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, bkg_height - snake_size) / 10.0) * 10.0
            snake_length += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()