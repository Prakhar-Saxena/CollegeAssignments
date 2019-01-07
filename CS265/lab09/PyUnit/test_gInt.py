#!/usr/bin/env python3
#
# Prakhar Saxena
# 2018-05-01
#


import sys
import unittest

from gInt import gInt

class gIntTest( unittest.TestCase ) :
        '''Tests for Money class'''

        def setUp( self ) :
                '''Optional.  Run before for each test.'''
                self.g1 = gInt( 1, 2)
		self.g1copy = gInt( 1, 2)
		self.g2 = gInt( 2, 3)
		self.g2copy = gInt( 2, 3)
		self.g3 = gInt( 3, 4)
		self.g3copy = gInt( 3, 4)
		self.g4 = gInt( 4, 5)
		self.g4copy = gInt( 4, 5)
		self.g5 = gInt( 5, 6)
                self.g5copy = gInt( 5, 6)

        def tearDown( self ) :
                '''Optional.  Called after each test (if setUp didn't fail)'''
                pass

        def test_add( self ) :

                r = self.g1 + self.g2

                self.assertEqual( self.g1, self.g1copy, 'Left operand changed after addition' )
                self.assertEqual( self.g2, self.g2copy, 'Right operand changed after addition' )
                self.assertEqual( r, gInt( 3, 5), 'Addition failed' )

	def test_mul( self ) :
		
		r = self.g3 * self.g4
		
		self.assertEqual( self.g3, self.g3copy, 'Left operand changed after addition' )
                self.assertEqual( self.g4, self.g4copy, 'Right operand changed after addition' )
                self.assertEqual( r, gInt( -8, 31), 'Multiplication failed' )

	def test_norm( self ) :
		
		r = self.g5.norm()
		
		self.assertEqual( self.g5, self.g5copy, 'arguement changed after calling the function' )
		self.assertEqual( r, 61)

if __name__ == '__main__' :
        sys.argv.append( '-v' )
        unittest.main()


