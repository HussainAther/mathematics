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

        # Create two dicts to store triangle neighbours and circumcircles.
        self.triangles = {}
        self.circles = {}

        # Create two CCW triangles for the frame
        T1 = (0, 1, 3)
        T2 = (2, 3, 1)
        self.triangles[T1] = [T2, None, None]
        self.triangles[T2] = [T1, None, None]

        # Compute circumcenters and circumradius for each triangle
        for t in self.triangles:
            self.circles[t] = self.circumcenter(t)

    def circumcenter(self, tri):
        """
        Compute circumcenter and circumradius of a triangle tri in 2D.
        """
        pts = np.asarray([self.coords[v] for v in tri])
        pts2 = np.dot(pts, pts.T)
        A = np.bmat([[2 * pts2, [[1],
                                 [1],
                                 [1]]],
                      [[[1, 1, 1, 0]]]])

        b = np.hstack((np.sum(pts * pts, axis=1), [1]))
        x = np.linalg.solve(A, b)
        bary_coords = x[:-1]
        center = np.dot(bary_coords, pts)

        # radius = np.linalg.norm(pts[0] - center) # euclidean distance
        radius = np.sum(np.square(pts[0] - center))  # squared distance
        return (center, radius)
