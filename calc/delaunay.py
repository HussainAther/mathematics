import numpy as np

"""
In mathematics and computational geometry, a Delaunay triangulation (also known as a Delone triangulation) 
for a given set P of discrete points in a plane is a triangulation DT(P) 
such that no point in P is inside the circumcircle of any triangle in DT(P).
This methods uses the Bowyer-Watson algorithm in two dimensions (2-D).
"""

class Delaunay2D:
    """
    Class to compute a Delaunay triangulation in 2D
    """
    def __init__(self, center=(0, 0), radius=10):
        """
        Init and create a new frame to contain the triangulation
        center is the position for the center of the frame. Default (0,0)
        radius is the distance from corners to the center.
        """
        center = np.asarray(center)
        # Create coordinates for the corners of the frame
        self.coords = [center+radius*np.array((-1, -1)),
                       center+radius*np.array((+1, -1)),
                       center+radius*np.array((+1, +1)),
                       center+radius*np.array((-1, +1))]
