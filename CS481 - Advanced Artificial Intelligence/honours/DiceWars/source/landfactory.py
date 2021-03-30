#!/usr/bin/env python


import random


class LandFactory(object):
    """
    As the name says, this class it for creating new Regions.
    """
    _land_id = -1  # let it start at 0
    
    def __init__(self, mapref):
        """
        map because a Region needs a reference to the map it belongs.
        """
        object.__init__(self)
        self._world = mapref
        
    def _get_id(self):
        """
        Private method to get a new, unique id for new Land.
        """
        self._land_id += 1
        return self._land_id
        
    def create(self):
        """
        -> Land 
        Creates a new Land-instance.
        """
        return Land( self._world,  self._get_id() )


class Land(object):
    """
    A Land is a conjunction of some cells on the map. This class has usefull 
    functions to perform operations.
    The Lands form a graph when thy are linked together.
    """
    
    def __init__(self, mapref, land_id):
        """
        map reference to the map it belongs
        id  unique id for that land.
        """
        object.__init__(self)
        self._world    = mapref # pointer to the world this Land belongs
        self._land_id  = land_id# unique ID of Land
        self._links    = []     # adjectant Lands, next time better using LandID
        self._player   = None   # whom this Land belongs
        self._cells    = []     # [(x,y),...] cells owned by this land
        self._selected = False  # if it is selected
        self.dirty = 1
    
    def _set_select(self, value):
        self.dirty = 1
        self._selected = value
        
    def _get_selected(self):
        return self._selected
    
    selected = property(_get_selected, _set_select)
    
    def get_id(self):
        """
        Returns the land id.
        """
        return self._land_id
    
    def _get_cells(self):
        """
        Returns a copy of the cells list of this Land.
        """
        return list(self._cells)
    cells   = property(_get_cells, None, None, \
                                "a copy of cells used by this land, read only")
    
    def link(self, other_land):
        """
        Connects this Land to the other and vice versa to form a graph (double
        linked nodes).
        """
        if other_land not in self._links and other_land != self:
            self._links.append(other_land)
            other_land.link(self)
            
    def unlink(self, other):
        """
        Deletes the link between this and the other Land.
        """
        if other in self._links:
            self._links.remove(other)
            other.unlink(self)
    
    def set_player(self, player):
        """
        Set the player this Land belongs to.
        Player must implement follwing methods:
            removeLand(land)
            addLand(land)   
        """
        if self._player != player:
            if self._player:
                self._player.remove_land(self)
                    
            self._player = player
            if player:
                player.add_land(self)
        self.dirty = 1
                
    def get_player(self):
        """
        Returns the player this land belongs to.
        """
        return self._player
    
    def add_cell(self, cell):
        """
        Add a cell of the map grid to belong to this land.
        """
        self._cells.append(cell)
        if self._world.cells.has_key(cell):
            land = self._world.cells[cell]
            if land and land != self:
                land.removeCell(cell)
            self._world.cells[cell] = self
    
    def remove_cell(self, cell):
        """
        Removes a cell from this Land.
        """
        if cell in self._cells:
            self._cells.remove(cell)
            self._world.cells[cell] = None
    
    def grow(self, num_cells=1):
        """
        This will let the Land grow about the number of cells you provide.
        Default growth is 1 cell. It will chose an adjectant cell randomly and
        add it if the cell is not taken yet.
        """
        added_cells = 0
##        for i in range(num_cells):
        while num_cells > 0:
            num_cells -= 1
            cells = self.get_empty_adj_cells()
            if len(cells):
                self.add_cell(random.choice(cells))
                added_cells += 1
        return added_cells
    
    def get_adj_cells(self, diag=False):
        """
        -> [(),()]
        Returns a list of any adjectant cells on the map grid (empty and taken 
        cells). Could be an empty list (then this Land would occupy the whole 
        map).
        """
        adj_cells = []
        for cell in self._cells:
            for adjcell in self._world.grid.get_adj_cells(cell, diag):
                if adjcell not in self._cells:
                    adj_cells.append(adjcell)
        return adj_cells
    
    def get_empty_adj_cells(self):
        """
        ->[(),()]
        Returns a list of empty, adjectand cells. This list could be empty.
        """
        empty = []
        for adjcell in self.get_adj_cells():
            if self._world.cells[adjcell] == None:#not ac:# == None:
                empty.append(adjcell)
        return empty
    
    def get_adj_lands(self):
        """
        Returns the Land that are adjectant on the map. This are not 
        necesairely the lands this land is linked with.
        """
        adj_lands = []
        for cell in self.get_adj_cells():
            land = self._world.cells[cell]
            if land:
                adj_lands.append(land)
        return adj_lands
    
    def get_linked_lands(self):
        """
        This returns the lands which has been linked with this land. These 
        lands dont need to bee the adjectant ones.
        """
        return list(self._links)
    
    def destroy(self):
        """
        Destroys this object, actually delete all references so garbage 
        collector can remove it.
        """
        for other in self._links:
            self.unlink(other)
        self.setPlayer(None)
        self._world = None
        
        
    
#------testing---------------#FF0000#FFFF---------------
## see: Schwerpunk-Flaeche.png, no because center of mass can be outside!
    def get_center_cell(self):
        """
        Returns the cell witch is in the center of the land.
        """
        xsum = 15
        ysum = 15
        for cell in self._cells:
##            xcoord, ycoord = cell
            xcoord, ycoord = self._world.grid.grid_to_abs(cell)
            xsum += xcoord
            ysum += ycoord
        num_cells = len(self._cells)
        xsum /= num_cells
        ysum /= num_cells
##        xsum = int(round(xsum))
##        ysum = int(round(ysum))
##        center_cell = (xsum, ysum)
        center_cell = self._world.grid.abs_to_grid((xsum, ysum))
        if not center_cell in self._cells:
            for cell in self._world.grid.get_adj_cells(center_cell):
                if cell in self._cells:
                    center_cell = cell
                    break;
        return center_cell
                    
            
    def get_center_cell_tmp2(self):
        """
        Returns the cell witch is in the center of the land.
        """
        xmax = 0
        xmin = 10000000
        ymax = 0
        ymin = 10000000
        for cell in self._cells:
##            xcoord, ycoord = cell
            xcoord, ycoord = self._world.grid.grid_to_abs(cell)
            if xcoord > xmax:
                xmax = xcoord
            if ycoord > ymax:
                ymax = ycoord
            
            if xcoord < xmin:
                xmin = xcoord
            if ycoord < ymin:
                ymin = ycoord
        
        centerx = (xmin+xmax)/2+1
        centery = (ymin+ymax)/2+1
            
##        center_cell = (xsum, ysum)
        center_cell = self._world.grid.abs_to_grid((centerx, centery))
        if not center_cell in self._cells:
            for cell in self._world.grid.get_adj_cells(center_cell):
                if cell in self._cells:
                    center_cell = cell
                    break;
        return center_cell

