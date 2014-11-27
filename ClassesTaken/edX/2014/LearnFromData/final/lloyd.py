"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Marshall Farrier
@contact: marshalldfarrier@gmail.com
@since: 2014-11-30
@summary: Lloyd's algorithm
https://courses.edx.org/c4x/CaltechX/CS_1156x/asset/final2iejhd.pdf
"""

import numpy as np
import scipy.spatial
from scipy.spatial.distance import cdist

def centers(x, ncenters=None, **kwargs):
    """
    Find centers using Lloyd's algorithm.

    Parameters
    ---
    x : ndarray
        Data for which to find centers
    ncenters : int
        Number of centers to find. Can and should be
        omitted if the parameter `init` is provided.
    init : ndarray, optional
        Centers from which to begin the algorithm.
        Must be provided if ncenters is omitted.

    Return
    ---
    ndarray with ncenters rows or the same number
    of rows as `init` and the same number of columns as x.

    Raises
    ---
    ValueError if an empty cluster is found
    """
    if 'init' in kwargs:
        centers = kwargs['init']
        if centers.shape[1] != x.shape[1]:
            raise ValueError("different dimensions for data and initial centers")
    else:
        if ncenters == None:
            raise ValueError("initial centers or number of centers must be provided")
        perm = np.random.permutation(np.arange(x.shape[0]))
        centers = x[perm[:ncenters], :]
    closest = get_closest(x, centers)
    centers, closest1 = _run(x, centers, closest)
    while not np.array_equal(closest1, closest):
        closest = closest1
        centers, closest1 = _run(x, centers, closest)
    return centers

def get_closest(x, centers):
    distances = cdist(x, centers, 'euclidean')
    return np.argmin(distances, axis=1)

def get_empty_clusters(x, centers):
    empty_clusters = []
    closest = get_closest(x, centers)
    for i in range(centers.shape[0]):
        if np.count_nonzero(closest == i) == 0:
            empty_clusters.append(i)
    return empty_clusters

def _run(x, centers, closest):
    for i in range(centers.shape[0]):
        tmp = x[closest == i]
        if len(tmp) == 0:
            raise ValueError("empty cluster")
        centers[i] = np.average(x[closest == i], axis=0)
    closest = get_closest(x, centers)
    return centers, closest
