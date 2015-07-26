# coding: utf-8

"""
Weleber-Tobler Algorithm for Kinetic Visual Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An algorithm to compute the solid angle projected by a kinetic perimetric
visual field.

Basic usage:

    >>> from weleber_tobler import kineticfield
    >>> kineticfield.compute([(54.7, 1.0), (51, 14.9), ... ])

The result is a dictionary that contains the solid angle and the percent of
a sphere it occupies:

    {
        'percent_of_sphere': 12.368853569901212,
        'steradians': 1.5543159803411815
    }

:license: GPL v2.0

"""
