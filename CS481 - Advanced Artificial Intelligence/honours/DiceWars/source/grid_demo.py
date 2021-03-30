import grids
import pygame
import os.path as path

pygame.font.init()
FONT = pygame.font.Font(None, 20)

def draw_string(screen, text, where):
    i = FONT.render(text, 2, (200, 200, 200, 200))
    screen.blit(i, where)


def main():
    
    # setup pygame
    pygame.init()
    pygame.display.set_caption("Keys: g, n, l, space, esc")
    screen = pygame.display.set_mode((1024, 768))
    # load imaged needed
    hextile = pygame.image.load(\
            path.join('data', 'images', 'grid', 'hextile.PNG')).convert()
    hextile.set_colorkey((0x80, 0x00, 0x80)) 
    odd_loc  = pygame.image.load(\
            path.join('data', 'images', 'grid', 'oddRowLocator.PNG')).convert()
    even_loc = pygame.image.load(\
           path.join('data', 'images', 'grid', 'evenRowLocator.PNG')).convert()
    cursor_tile = pygame.image.load(\
            path.join('data', 'images', 'grid', 'cursorhextile.PNG')).convert()
    cursor_tile.set_colorkey((0x80, 0x00, 0x80))
    
    # define size of the grid
    size = (33, 27)
    offset = (20, 50)
    
    # grids
    hgrid = grids.HexagonGrid(size, odd_loc, even_loc, offset)
    rgrid = grids.RectGrid(size, tuple(odd_loc.get_size()), offset)
    grid = hgrid
    print "grid nums: "+str(grid._num_cell_x)+"/"+str(grid._num_cell_y)
    
    # variables
    show = 0 # if 1 show rect
    show_locator = 0
    running = True
    
    # main loop
    while running:
        # draw grid
        for xpos in range(size[0]):
            for ypos in range(size[1]):
                pos = grid.grid_to_abs((xpos, ypos))
                screen.blit(hextile, pos)
        # eventhandling
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            # show neighbour
            adj_cells = grid.get_adj_cells(\
                            grid.abs_to_grid( (pygame.mouse.get_pos()) ), True)
            for cell in adj_cells:
                screen.blit(cursor_tile, grid.grid_to_abs(cell))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            # change grid hexagon<->rectangular
            if grid == hgrid:
                grid = rgrid
            else:
                grid = hgrid
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # switch rect on/off
            show ^= 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            # switch rect on/off
            show_locator ^= 1
            
        # draw enlightened tile
        pos = pygame.mouse.get_pos()
        screen.blit(cursor_tile, grid.grid_to_abs(grid.abs_to_grid(pos)))
        
        # calculate the rectangular grid offset (only neede for rectangle 
        # an Locator drawing)
        xpos, ypos = pos
        xpos = ((xpos-grid._offset_x)/grid._cell_width)*grid._cell_width + \
                                                                grid._offset_x
        ypos = (ypos-grid._offset_y)/grid._cell_height*grid._cell_height+\
                                                                grid._offset_y
        
        # draw Locator
        if show_locator:
            yrow = (ypos-grid._offset_y)/grid._cell_height
            if yrow&1: # odd row
                screen.blit(odd_loc, (xpos, ypos))
            else: 
                screen.blit(even_loc, (xpos, ypos))
            
        # draw rect if needed
        if show:
            pygame.draw.rect(screen, (255, 0, 0), \
               pygame.Rect(xpos, ypos, grid._cell_width, grid._cell_height), 2)
            
        # draw info
        pos = pygame.mouse.get_pos()
        draw_string(screen, "abs pos: "+str(pos), (50, 20))
        draw_string(screen, "grid pos: "+str(grid.abs_to_grid(pos)), (200, 20))
        draw_string(screen, "inside the grid: "+\
                            str(grid.abs_coord_in_grid(pos)), (350, 20))
        
        # update screen
        pygame.display.flip()
        screen.fill((0, 0, 0))
    
    # clean up
    pygame.quit()


if __name__ == '__main__':
    main()
