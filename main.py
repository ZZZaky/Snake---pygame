import pygame
import sys
from pygame.math import Vector2
import random

class Snake:
    def __init__(self):
        self.body = [Vector2(3, 2), Vector2(2, 2), Vector2(1, 2)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        
        self.head_up = pygame.image.load('assets/snake_head_up.png').convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up, (cell_size, cell_size))
        #
        self.head_down = pygame.image.load('assets/snake_head_down.png').convert_alpha()
        self.head_down = pygame.transform.scale(self.head_down, (cell_size, cell_size))
        #
        self.head_left = pygame.image.load('assets/snake_head_left.png').convert_alpha()
        self.head_left = pygame.transform.scale(self.head_left, (cell_size, cell_size))
        #
        self.head_right = pygame.image.load('assets/snake_head_right.png').convert_alpha()
        self.head_right = pygame.transform.scale(self.head_right, (cell_size, cell_size))
        
        
        self.tail_up = pygame.image.load('assets/snake_tail_up.png').convert_alpha()
        self.tail_up = pygame.transform.scale(self.tail_up, (cell_size, cell_size))
        #
        self.tail_down = pygame.image.load('assets/snake_tail_down.png').convert_alpha()
        self.tail_down = pygame.transform.scale(self.tail_down, (cell_size, cell_size))
        #
        self.tail_left = pygame.image.load('assets/snake_tail_left.png').convert_alpha()
        self.tail_left = pygame.transform.scale(self.tail_left, (cell_size, cell_size))
        #
        self.tail_right = pygame.image.load('assets/snake_tail_right.png').convert_alpha()
        self.tail_right = pygame.transform.scale(self.tail_right, (cell_size, cell_size))
        
        
        self.turn_upleft = pygame.image.load('assets/snake_turn_up-left.png').convert_alpha()
        self.turn_upleft = pygame.transform.scale(self.turn_upleft, (cell_size, cell_size))
        #
        self.turn_upright = pygame.image.load('assets/snake_turn_up-right.png').convert_alpha()
        self.turn_upright = pygame.transform.scale(self.turn_upright, (cell_size, cell_size))
        #
        self.turn_downleft = pygame.image.load('assets/snake_turn_down-left.png').convert_alpha()
        self.turn_downleft = pygame.transform.scale(self.turn_downleft, (cell_size, cell_size))
        #
        self.turn_downright = pygame.image.load('assets/snake_turn_down-right.png').convert_alpha()
        self.turn_downright = pygame.transform.scale(self.turn_downright, (cell_size, cell_size))
        
        
        self.body_vertical = pygame.image.load('assets/snake_body_vertical.png').convert_alpha()
        self.body_vertical = pygame.transform.scale(self.body_vertical, (cell_size, cell_size))
        #
        self.body_horizontal = pygame.image.load('assets/snake_body_horizontal.png').convert_alpha()
        self.body_horizontal = pygame.transform.scale(self.body_horizontal, (cell_size, cell_size))
        
        self.crunch_sound = pygame.mixer.Sound('assets/crunch.wav')
    
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            
            if index == 0: #head
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1: #tail
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.turn_upleft, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.turn_downleft, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.turn_upright, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.turn_downright, block_rect)
    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): 
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0): 
            self.head = self.head_right
        elif head_relation == Vector2(0, 1): 
            self.head = self.head_up
        elif head_relation == Vector2(0, -1): 
            self.head = self.head_down
    
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_up
    
    def move_snake(self):
        if self.new_block == True:
            _body = self.body[:]
            _body.insert(0, _body[0] + self.direction)
            self.body = _body[:]
            self.new_block = False
        else:
            _body = self.body[:-1]
            _body.insert(0, _body[0] + self.direction)
            self.body = _body[:]
    
    def add_block(self):
        self.new_block = True
    
    def play_crunch_sound(self):
        self.crunch_sound.play()
    
    def reset(self):
        self.body = [Vector2(3, 2), Vector2(2, 2), Vector2(1, 2)]
        self.direction = Vector2(0, 0)

class Fruit:
    def __init__(self):
        self.randomize()
    
    def draw_fruit(self):
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        fruit_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        screen.blit(apple, fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
        
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
    
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        self.snake.reset()
    
    def draw_grass(self):
        grass_color = (27, 204, 27)
        for row in range(cell_number):
            for column in range(cell_number):
                if column % 2 == row % 2:
                    grass_rect = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)
    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (1, 4, 18))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        
        screen.blit(score_surface, score_rect)


pygame.init()

cell_size = 100
cell_number = 10

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

apple = pygame.image.load('assets/apple.png').convert_alpha()
apple = pygame.transform.scale(apple, (cell_size, cell_size))

game_font = pygame.font.Font('assets/font.ttf', int(cell_size / 2))

fruit = Fruit()
snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            
            if event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)
            
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)
            
            if event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)
    
    screen.fill((61, 245, 61))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(150)