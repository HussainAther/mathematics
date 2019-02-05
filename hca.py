"""
General algorithm for hierchical clustering analysis.
"""

# Returns minimum difference between any pair
def findMinDiff(arr, m):
  
    # Sort array in non-decreasing order
    arr = sorted(arr)
  
    # Initialize difference as infinite
    diff = 10**20
  
    # Find the min diff by comparing adjacent
    # pairs in sorted array
    min_pair = []
    for i in range(m-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]
            min_pair = arr[i+1] - arr[i]
  
    # Return min diff
    return diff, min_pair

# Construct a graph T by assigning an isolated vertex to ecah cluster
def hca(d, n): # n is the number of clusters to form. # d is the data itself in list form.
    T = [] # graph to consctruct and output
    while n > 1:
        diff, closest = findMinDiff(d, len(d))




HIERARCHICALCLUSTERING(d, n)
1 Form n clusters, each with 1 element
2 Construct a graph T by assigning an isolated vertex to each cluster
3 while there is more than 1 cluster
4 Find the two closest clusters C1 and C2
5 Merge C1 and C2 into new cluster C with |C1| + |C2| elements
6 Compute distance from C to all other clusters
7 Add a new vertex C to T and connect to vertices C1 and C2
8 Remove rows and columns of d corresponding to C1 and C2
9 Add a row and column to d for the new cluster C
10 return T
