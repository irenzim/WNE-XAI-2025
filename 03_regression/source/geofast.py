import math

import numpy as np


def _dist(lon1, lat1, lon2, lat2):
    """
    Very fast computation for distance between (lon1,lat1)
    and (lon2,lat2) providing the locations are not so far
    away, i.e. in one city.

    Parameters:
        lon1 : float
            Longitude of the first point
        lat1 : float
            Latitude of the first point
        lon2 : float
            Longitude of the second point
        lat2 : float
            Latitude of the second point

    Returns: int
        Distance in meters between (lon1,lat1) and (lon2,lat2)

    """
    dy = 111134 * (lat2 - lat1)
    dx = 111317 * (lon2 - lon1) * math.cos((lat1 + lat2) / 2)

    return int(math.sqrt(dx**2 + dy**2))


distance = np.vectorize(_dist)
""" Vectorized _dist function over lon2,lat2.
    Very fast computation for distance between a point (lon1,lat1) 
    and Series lon2,lat2  providing the locations are not so far
    away, i.e. in one city.
    
    Parameters:
        lon1 : float
            Longitude of the first point
        lat1 : float
            Latitude of the first point
        lon2 : float or Series
            Longitude of the second point(s)
        lat2 : float or Series
            Latitude of the second point(s)
            
    Returns : series of ints
        Distances between starting point (lon1,lat1) and ending point (lat2,lon2). Length of return matches length of series lon2,lat2.
"""
