#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:04:12 2020

@author: neelappagouda
"""


def const_violation( Cmx ):
    
    """ 
    This module will check the constraint violation 
    and also in this module, "0.01" is the penalty
    of factor 10 times the objective value( CD).

    """
    
    gp = 0.01 * ( Cmx - 0.1069 )
    
    phi = max( 0 , gp)
    
    return phi