from matplotlib.pyplot import grid
import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block , play_width and play_height represent the red square box (border for the game)
play_height = 600  # meaning 600 // 20 = 30 height per block, The numbers divided 10 & 20 are because Tetris is played on a 10 (width) x 20 (height) grid
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# SHAPE FORMATS

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object): # *
	def __init__(self, x, y, shape):
            self.x = x
            self.y = y
            self.shape = shape
            self.color = shape_colors(shapes.index(shape))
            self.rotation = 0

def create_grid(locked_positions={}):
	grid = [[(0,0,0)for x in range(10)] for x in range(20)] #There are 10 blocks in each row and 20 rows total

      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  if (j, i) in locked_pos:       #Rows are represented by i and columns by j
                        c = locked_pos[(j,i)]
                        grid[i][j] = c
      return grid

def convert_shape_format(shape):
	pass

def valid_space(shape, grid):
	pass

def check_lost(positions):
	pass

def get_shape():
	return random.choice(shapes)

def draw_text_middle(text, size, color, surface):
	pass
   
def draw_grid(surface):
	
      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0) #block_size replaces 30, the 0 at the end designates filling in
      
      pygame.draw.rect(surface, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 4) #These variables have already been defined, 4 is the border size
      
def clear_rows(grid, locked):


def draw_next_shape(shape, surface):


def draw_window(surface, grid):
	surface.fill((0,0,0))

      pygame.font.init()
      font = pygame.font.SysFont('bookantiqua', 60)
      label = font.render('Tetris', 1, (255,255,255))

      surface.blit(label, (top_left_x + play_width/2 - (label.get.width()/2), 30))
      draw_grid(surface, grid)
      pygame.display.update()

def main():
	pass

def main_menu():
	pass

main_menu()  # start game

