""" vector.py
Library of vector math functions for vectors as lists
"""

import math

def vector_add(vect1, vect2):
    """ Adds corresponding elements of 2 vectors """
    return [v1_i + v2_i for v1_i, v2_i in zip(vect1, vect2)]

def vector_subtract(vect1, vect2):
    """ Subtracts corresponding elements of 2 vectors """
    return [v1_i - v2_i for v1_i, v2_i in zip(vect1, vect2)]

def vector_sum(vector_list):
    """ Add all vectors in vector_list """
    return reduce(vector_add, vector_list)

def scalar_multiply(scalar, vect):
    """ Multiply components by scalar """
    return [scalar * v_i for v_i in vect]

def vector_mean(vectors):
    """ Calculate a mean vector """
    return scalar_multiply(1/len(vectors), vector_sum(vectors))

def dot(vect1, vect2):
    """ Calculate dot product of vect1 and vect2 """
    return sum(v1_i * v2_i
               for v1_i, v2_i in zip(vect1, vect2))

def magnitude(vect):
    """ Calculate the magnitude of a vector """
    return math.sqrt(dot(vect, vect))

def distance(vect1, vect2):
    """ Calculate the distance between 2 vectors """
    return magnitude(vector_subtract(vect1, vect2))
