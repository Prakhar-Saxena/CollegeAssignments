#!/usr/bin/env python3
#
# Money - trivial class, to demonstrate pyUnit testing
#
# Kurt Schmidt
# 4/2018
#
# Note: intended to store only whole units (no change)
#

class Money :

	class BadUnitsException( Exception ) :
		'''TODO: msg?  Something?'''
		pass
	
	
	def __init__( self, amt, curr ) :
		'''amt - an integer
		curr - string (TODO)'''
		self.amt = amt
		self.curr = curr

	def __eq__( self, other ) :
		if not isinstance( self, other.__class__ ) :
			return False
		return self.amt == other.amt and self.curr == other.curr

	def __add__( self, rhs ) :
		'''Returns new Money object, sum of 2 inputs'''
		
		if not isinstance( rhs, Money ) :
			raise TypeError( "rhs must be of type Money" )
		
		if self.curr != rhs.curr :
			raise Money.BadUnitsException( "Different currency types" )
		
		return Money( self.amt+rhs.amt, self.curr ) 
	
	def __str__( self ) :
		return self.curr + ' ' + str( self.amt )


u1 = Money( 13, 'USD' )
u2 = Money(  8, 'USD' )
p1 = Money( 27, 'PLN' )

