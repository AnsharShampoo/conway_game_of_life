from conway_colors import conway_colors
import pygame
import sys
def print_grid(screen,size):
        #set grid
    for x in range(0,size[0],10):
        pygame.draw.line(screen,conway_colors.GRAY, [x,0], [x,size[1]])
    for y in range(0,size[1],10):
        pygame.draw.line(screen,conway_colors.GRAY, [0,y],[size[0],y])

def get_squares(screen,squares,size):
    for x in range(size[0]):
        for y in range(size[1]):
            pygame.draw.rect(screen,conway_colors.BLACK,(x*10,y*10,10,10)) if squares[x][y]==0 else pygame.draw.rect(screen,conway_colors.WHITE,(x*10,y*10,10,10))

def event_manager(screen, squares):
    for event in pygame.event.get():
        if event.type == pygame.K_q or event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            pygame.draw.rect(screen,conway_colors.WHITE,(mouse_x-(mouse_x%10),mouse_y-(mouse_y%10),10,10))
            print(f"{int((mouse_x-(mouse_x%10))/10)}:::{int((mouse_y-(mouse_y%10))/10)}")
            squares[int((mouse_x-(mouse_x%10))/10)][int((mouse_y-(mouse_y%10))/10)] = 1 if squares[int((mouse_x-(mouse_x%10))/10)][int((mouse_y-(mouse_y%10))/10)]==0 else 0

def main():
    pygame.init()
    size = (100,200)
    screen = pygame.display.set_mode(size)
    squares = [[0 for i in range(size[1])] for j in range(size[0])]
    while True:
        get_squares(screen,squares,size)
        print_grid(screen,size)
        event_manager(screen, squares)
        pygame.display.flip()

if __name__ == '__main__':
    main()