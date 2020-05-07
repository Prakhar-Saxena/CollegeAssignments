
import grids
import diceland
import pygame
import random
from os import path


class MapGenerator(object):
    """
    Map with random map generation feature. Call create() to fill the map, if 
    you dont like the result you can call randomize() to generate a new map 
    layout.
    """
    
    def __init__(self):
        """
        
        """
        # public
        self.cells = {}         # {(cx, cy):Land} holds Land references
        self.grid = None       # grid used for this map
        
        # private
        # next time perhaps better using {landID:land}
        self._lands = []          # list of lands in this map
        self._islands = []        # [[lands],[lands],...] => len(islands)>=1
        
        self._land_factory = None # factory for lands
        
        self._num_filled_cells = 0 # how many cells should be filled
        self._num_cells_in_land = 0 # how many cells are in a land
        self._num_lands = 0 # how many lands are on the map
        
        
    def create(self, grid, land_factory, num_lands=30, \
                cells_in_land=None, percent_grid_fill = 0.8):
        """
        Creates a new map. You to call this function before you can use the 
        map. To tune you map there are some parameter that you can change:
        grid             : grid instance from grids.py (or any grid with same 
                           interface)
        land_factory      : LandFactory instance from landfactory.py
        num_lands         : number of Land this map must have
        cells_in_land     : there you can define how many cell a land has
                            if this is None the number of cells in a land is
                            calculated cells_in_land = numFilledCells/num_lands
        percent_grid_fill : percentage 0.0-1.0 of how many cell of the map 
                            should be occupied, only works 
                            if cells_in_land==None
        """
        self.grid = grid
        self._land_factory = land_factory
        numgrid_x, numgrid_y = grid.get_num_cells()
        self._num_filled_cells = int(numgrid_x*numgrid_y*percent_grid_fill)
        if cells_in_land:
            self._num_cells_in_land = cells_in_land
        else:
            self._num_cells_in_land = self._num_filled_cells/num_lands
        self._num_lands = num_lands
        
        # generate lands
        self._lands = []
        for i in range(self._num_lands):
            self._lands.append(self._land_factory.create())
        
        # finish creation by ramdomizing the cells
        self.randomize()
        
    def randomize(self):
        """
        Generates a new random layout of the map.
        """
        
        # remove old lands and links
        self._create()
        self._find_islands()
        n = 0
        while len(self._islands)>1:
            self._create()
            self._find_islands()
            n += 1
            print "map gen tries:", n
                    
        if len(self._islands)>1:
            # not all have been reached islands has been detected
            print len(self._islands), "island lands:"
            for island in self._islands:
                for node in island:
                    print node.get_id()
                print "------------------"
        
        
    def _create(self):
        self._clear()
        # set random cells for starting
        chosen_cells = random.sample(self.cells.keys(), self._num_lands)
        
        # add lands
        idx = 0
        for cell in chosen_cells:
            self.cells[cell] = self._lands[idx]
            self._lands[idx].add_cell(cell)
            idx += 1
        
        num_cells = self._num_cells_in_land
        for i in range(num_cells):
##        while num_cells: # not good, eventually endless loop!
            # for each land
            for land in random.sample(self._lands, len(self._lands)):
                # as long number of cells per land is not reached
                if len(land.cells)<self._num_cells_in_land:
                    growth = land.grow()
                    num_cells -= growth
                        
# old land generation code, first try
##        num_cells = self._num_cells_in_land
##        for i in range(num_cells):
##            # for each land
##            for land in self._lands:
##                # 0 get cells of land
##                cells = list(land.cells)
##                # 1 if num_cells>=cellperLand -> quit
##                if len(cells)<self._num_cells_in_land:
##                    for dumy in cells:
##                        # 2 chose a cell
##                        c = random.choice(cells)
##                        # 3 get adjectants
##                        adjCells = self.grid.getAdjCells(c)
##                        # 4 remove all taken ones
##                        for ac in list(adjCells):
##                            if self.cells[ac]!=None:
##                                self.cells[c].link(self.cells[ac])
##                                adjCells.remove(ac)
##                        # 5 if non left remove chosen cell and goto 2
##                        if len(adjCells):
##                            # 6 chose one of adjlist
##                            ac = random.choice(adjCells)
##                            # 7 occupi it
##                            self.cells[ac] = land
##                            land.addCell(ac)
##                            break;
##                        else:
##                            num_cells += 1
                            
        # TODO: check for not reachable (*) lands and do something against
        # like move it, put an additional land between, ...
        # (*): graph algo that check if every node is reachable!
        
        # link the lands
        for land in self._lands:
            for adj_land in land.get_adj_lands():
                land.link(adj_land)
###            if len(land._links)<2: #TODO: parameter
##            if len(land.get_linked_lands())<2: # does not guarantee that no island exists
##                print "Warning: land not Linked!"
##                num = 1000
##                while len(land.get_linked_lands())<2 and num:
##                    land.grow()
##                    for adjl in land.get_adj_lands():
##                        land.link(adjl)
##                    num -= 1
                    
    
    def _clear(self):
        # generate all cells-land connection
        numgrid_x, numgrid_y = self.grid.get_num_cells()
        # TODO: why not self.cells = {} ??
        for gridx in range(numgrid_x):
            for gridy in range(numgrid_y):
                self.cells[ (gridx, gridy) ] = None
                
        # remove all cells from the lands
        for land in self._lands:
            land._cells = []
            land._links = []
            # TODO: remove all direct access to private members
    
    def _find_islands(self):
        """
        
        """
        # DepthFirstSearch algo
        # to find out if there are islands
        islands = []
        nodes = list(self._lands)
        while len(nodes):
            visited = []
            stack = [] # use append() and pop()
            start_node = nodes.pop()
            visited.append(start_node)
            stack.append(start_node)
            while len(stack):
                current_node = stack.pop()
##                print "node:", current_node.get_id()
                for adj_node in current_node._links:
                    if adj_node not in visited:
                        stack.append(adj_node)
                        visited.append(adj_node)
                        if adj_node in nodes:
                            nodes.remove(adj_node)
##            print "--------------- new island"
            islands.append(visited)
        self._islands = islands
        
        
        
    def get_land_from_abs(self, pos):
        """
        Returns the Land at absPos or None if there isnt one.
        """
        gpos = self.grid.abs_to_grid(pos)
        if self.grid.grid_coord_in_grid(gpos):
            return self.cells[gpos]
        return None
    
    def get_land_by_id(self, land_id):
        """
        Returns the Land or None if no land exists with that land_id.
        """
        for land in self._lands:
            if land._land_id == land_id:
                return land
        return None
        
    def get_lands(self):
        """
        Returns a list of lands.
        """
        return self._lands
        
    def save_map_to_dict(self):
        """
        Returns a dict of this map. Format: (size, {landID:[cells]})
        """
        # TODO: save number of dices in dict too
        store = {}
        for land in self._lands:
            store[land._land_id] = land.cells
        return (self.grid.get_num_cells(), store)
    
    def restore_map_from_dict(self, store):
        """
        Reconstructs the map from the dict.
        """
        # delete old values
        for land in self._lands:
            land.destroy
        self._lands = []
        self.cells = {}
        
        # build new map up
        size, store = store
        self.grid.set_num_cells(size)
        for xnum in range(size[0]):
            for ynum in range(size[1]):
                self.cells[(xnum, ynum)] = None
        for land_id, cell_list in store.items():
            land = diceland.DiceLand(self, land_id)
            self._lands.append(land)
            for cell in cell_list:
                land.add_cell(cell)
        self._num_lands = len(self._lands)
                    
        # link the lands
        for land in self._lands:
            for adjland in land.get_adj_lands():
                land.link(adjland)
        
    def save_to_file(self, filename):
        """
        Not implemented yet.
        """
        # TODO: implement saveToFile
        raise NotImplementedError
    
    def load_from_file(self, filename):
        """
        Not implemented yet.
        """
        # TODO: implement saveToFile
        raise NotImplementedError
        
def test():
    """
    test code to show that it is working
    dirty hacks in here, so dont look at the code!
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    odd_loc = pygame.image.load(\
                    path.join('data', 'images', 'oddLocator.PNG')).convert()
    even_loc = pygame.image.load(\
                    path.join('data', 'images', 'evenLocator.PNG')).convert()

    world = MapGenerator()
    grid = grids.HexagonGrid((31, 27), odd_loc, even_loc, offset=(100, 0))
    world.create(grid, diceland.DiceLandFactory(world), \
                                    cells_in_land=20, percent_grid_fill=0.3)
    
    numgrid_x, numgrid_y = grid.get_num_cells()
    print "grid has", numgrid_x*numgrid_y, "cells"
                        
    num = 0
    for cell, land in world.cells.items():
        if land:
            num += 1
    print "occupied cells: ", \
            num, \
            float(num)/(numgrid_x*numgrid_y), \
            world._num_filled_cells, \
            float(world._num_filled_cells)/(numgrid_x*numgrid_y)
    
    
    tile = pygame.image.load(\
                        path.join('data', 'images', 'hextile.PNG')).convert()
    tile.set_colorkey((0x80, 0x00, 0x80))
    curtile = pygame.image.load(\
                    path.join('data', 'images', 'cursorhextile.PNG')).convert()
    curtile.set_colorkey((0x80, 0x00, 0x80))
    adjtile = pygame.image.load(\
                      path.join('data', 'images', 'adjhextile.PNG')).convert()
    adjtile.set_colorkey((0x80, 0x00, 0x80))
    pos = pygame.mouse.get_pos()
    
    running = True
    storedmap = None
    while running:
        # event handling
        event = pygame.event.wait()
        if event.type == pygame.QUIT or \
                (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                world.randomize()
            elif event.key == pygame.K_s:
                storedmap = world.save_map_to_dict()
                print ">>>>>>>>>>>>>>>>>>>>map saved!!"
                print storedmap
            elif event.key == pygame.K_r:
                if storedmap:
                    world.restore_map_from_dict(storedmap)
                    print ">>>>>>>>>>>>>map restored!!"
##        else:
##            print event
            
        # draw tile ons screen
        for land in world._lands:
##            color = world.testcolors[land._id]
##            i.fill(color)
            for cell in land.cells:
##                screen.blit(i, world.grid.gridToAbs(c))
                screen.blit(tile, world.grid.grid_to_abs(cell))
        
        # draw highlighted land
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
##            print "cell:", world.grid.abs_to_grid(pos)
        land = world.get_land_from_abs(pos)
        if land:
##            i.fill((255, 0, 0))
            for cell in land.cells:
##                screen.blit(i, world.grid.gridToAbs(c))
                screen.blit(curtile, world.grid.grid_to_abs(cell))
        # draw adjectand lands if mouse button is pressed
        if pygame.mouse.get_pressed()!=(0, 0, 0):
            land = world.get_land_from_abs(pygame.mouse.get_pos())
            if land:
                i.fill((255, 0, 255))
                for adjland in land._links:
                    for cell in adjland.cells:
##                        screen.blit(i, world.grid.gridToAbs(c))
                        screen.blit(adjtile, world.grid.grid_to_abs(cell))
                        
        # draw origin cell
        i = pygame.Surface((15, 15))
        i.fill((255, 255, 0))
        for land in world._lands:
            screen.blit(i, world.grid.grid_to_abs(land._cells[0]))
        #-----testing ----#FF0000#FFFF00----
        # draw center cell
        i = pygame.Surface((10, 10))
        i.fill((0, 255, 0))
        for land in world._lands:
            screen.blit(i, world.grid.grid_to_abs(land.get_center_cell()))
            
        
        pygame.display.flip()
        screen.fill((0, )*3)
        
    pygame.quit()
    
        
        
if __name__ == '__main__':
    test()
