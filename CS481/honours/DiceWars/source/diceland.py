#!/usr/bin/env python


from landfactory import Land
from landfactory import LandFactory

import dice


# TODO: perhaps I should move this out to a own file
class DiceLandFactory(LandFactory):
    """
    A DiceLand factory for the Dicegame. Creates DiceLands.
    """
    def __init__(self, world):
        """
        Same as for Land.
        """
        LandFactory.__init__(self, world)
        
    def create(self):
        """
        -> DiceLand instance.
        Returns a DiceLand instance.
        """
        return DiceLand( self._world, self._get_id() )


class DiceLand(Land):
    """
    Specialist version of the Land. It can hold a number of Dices and provides
    a method to roll them.
    """
    def __init__(self, world, land_id):
        """
        Same as for Land.
        """
        Land.__init__(self, world, land_id)
        self._dices    = []    # list of dice object on this land
        
    def _get_num_dices(self):
        """
        Returns the number of dices.
        """
        return len(self._dices)
    num_dice = property(_get_num_dices, doc="number of dices, read only")
    
    def roll_dice(self):
        """
        rollDice() -> (pips1, pips2, ...,), sumOfPips
        Returns a list of all Results of the dices and at the end the Sum of 
        all pips.
        """
        pips_sum = 0
        res = []
        for mdice in self._dices:
            pips = mdice.roll()
            pips_sum += pips
            res.append(pips)
        return res, pips_sum
        
    def add_dice(self):
        """
        Adds a Dice to this Land.
        """
        self._dices.append(dice.Dice())
        
    def remove_dice(self):
        """
        Removes a Dice from this Land.
        Returns the number of left dices.
        """
        try:
            self._dices.pop()
        except:
            pass
        return len(self._dices)
    
    def set_num_dice(self, num = 1):
        """
        Set the number of dices to num. Default to 1.
        """
        self._dices = []
        for k in range(num):
            self._dices.append(dice.Dice())
            
        
        