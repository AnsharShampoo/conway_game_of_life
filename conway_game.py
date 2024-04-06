from conway_colors import conway_colors
import pygame
import sys
clock = pygame.time.Clock()

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

def event_manager(screen, squares, size):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            pygame.draw.rect(screen,conway_colors.WHITE,(mouse_x-(mouse_x%10),mouse_y-(mouse_y%10),10,10))
            print(f"{int((mouse_x-(mouse_x%10))/10)}:::{int((mouse_y-(mouse_y%10))/10)}")
            squares[int((mouse_x-(mouse_x%10))/10)][int((mouse_y-(mouse_y%10))/10)] = 1 if squares[int((mouse_x-(mouse_x%10))/10)][int((mouse_y-(mouse_y%10))/10)]==0 else 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_simulation(screen,squares,size)

def conway_grid(squares, new_squares,size):
    for x in range(size[0]):
            for y in range(size[1]):
                alive_neighbours = check_neighbours(x,y,squares,size)
                if(squares[x][y]==1 and (alive_neighbours==2 or alive_neighbours==3)):
                    new_squares[x][y]=1
                elif(squares[x][y]==0 and alive_neighbours==3):
                    new_squares[x][y]=1
    return new_squares

def start_simulation(screen,squares,size):
    #RULES
    #Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    #Any live cell with two or three live neighbors lives on to the next generation.
    #Any live cell with more than three live neighbors dies, as if by overpopulation.
    #Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    running = True
    new_squares = [[0 for i in range(size[1])] for j in range(size[0])]
    while running:
        conway_grid(squares,new_squares,size)
        for x in range(size[0]):
            for y in range(size[1]):
                squares[x][y] = new_squares[x][y]
        get_squares(screen,new_squares,size)
        for x in range(size[0]):
            for y in range(size[1]):
                new_squares[x][y] = 0
        print_grid(screen,size)
        simulation_event_manager(screen, new_squares, size)
        pygame.display.flip()
        clock.tick(60)

def check_neighbours(x, y, squares, size):
    alive_cells = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                # Skip the cell itself
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < size[0] and 0 <= ny < size[1]:
                alive_cells += squares[nx][ny]
    return alive_cells

def simulation_event_manager(screen, squares, size):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                main_event(screen,squares,size)

def main_event(screen,squares,size):
    while True:
        get_squares(screen,squares,size)
        print_grid(screen,size)
        event_manager(screen, squares, size)
        pygame.display.flip()
        clock.tick(60)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    size = (500,500)
    screen = pygame.display.set_mode(size)
    squares = [[0 for i in range(size[1])] for j in range(size[0])]
    main_event(screen,squares,size)

if __name__ == '__main__':
    main()