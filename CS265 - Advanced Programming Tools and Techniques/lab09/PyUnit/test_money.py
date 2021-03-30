#!/usr/bin/env python3
# test_money - Unit Test for Money class
#
# Kurt Schmidt
# 8/06
#
# JUnit 4 ?
#
# editor: tabstop=2, cols=120
#
# 12/16
#	- re-tooled for JUnit4
#

import sys
import unittest

from money import Money  # the class I wrote, that I wish to test

class MoneyTest( unittest.TestCase ) :
	'''Tests for Money class'''
	
	def setUp( self ) :
		'''Optional.  Run before for each test.'''
		self.u1 = Money( 13, 'USD' )
		self.u1copy = Money( 13, 'USD' )
		self.u2 = Money(  8, 'USD' )
		self.u2copy = Money(  8, 'USD' )
		self.p1 = Money( 13, 'PLN' )
		self.n1 = Money( -13, 'USD' )
		self.n2 = Money( -18, 'USD' )
		self.n2copy = Money( -18, 'USD' )
	
	def tearDown( self ) :
		'''Optional.  Called after each test (if setUp didn't fail)'''
		pass

	def test_equals( self ) :
		
		self.assertEqual( self.u1, self.u1, 'Money not equal to itself' )
		self.assertEqual( self.u1, self.u1copy, 'Money not equal to identical object' )
		self.assertEqual( self.n2, self.n2copy, 'Money not equal to identical object' )

		self.assertNotEqual( self.u1, self.u2, 'USD 13 == USD 8' )
		self.assertNotEqual( self.u1, self.p1, 'USD 13 == PLN 13' )
		self.assertNotEqual( self.u1, self.n1, 'USD 13 == USD  -13' )

	def test_add( self ) :
	
		r = self.u1 + self.u2

		self.assertEqual( self.u1, self.u1copy, 'Left operand changed after addition' )
		self.assertEqual( self.u2, self.u2copy, 'Right operand changed after addition' )
		self.assertEqual( r, Money( 21, 'USD' ), 'Addition failed' )

		r = self.u1 + self.n2
		self.assertEqual( r, Money( -5, 'USD' ), 'Addition of positive + negative failed' )

		r = self.n1 + self.n2
		self.assertEqual( r, Money( -31, 'USD' ), 'Addition of negative + negative failed' )

		self.assertRaises( Money.BadUnitsException, Money.__add__, self.u2, self.p1 )


if __name__ == '__main__' :
	sys.argv.append( '-v' )
	unittest.main()

