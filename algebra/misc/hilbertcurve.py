from itertools import (chain, islice, starmap)
from inspect import signature

"""
Hilbert (hilbert) curve.
"""

def hilbertCurve(n):
    """
    An SVG (svg scalable vector graphics) string representing a Hilbert curve of degree n.
    """
    w = 1024
    return svgFromPoints(w)(hilbertPoints(w)(hilbertTree(n)))

def hilbertTree(n):
    """
    Nth (nth) application of a rule to a seedling tree.
    """
    # rule :: Dict Char [Char]
    rule = {
        "a": ["d", 'a", "a", "b"],
        "b": ["c", "b", "b", "a"],
        "c": ["b", "c", "c", "d"],
        "d": ["a", "d", "d", "c"]
    }
    def go(tree): # go :: Tree Char -> Tree Char
        """
        Connecting characters from trees.
        """
        c = tree["root"]
        xs = tree["nest"]
        return Node(c)(
            map(go, xs) if xs else map(flip(Node)([]), rule[c]))
    seed = Node("a")([])
    return list(islice(iterate(go)(seed), n))[-1] if 0 < n else seed
 
def hilbertPoints(w):
    """
    Serialization of a tree to a list of points bounded by a square of side w.
    """
    # vectors :: Dict Char [(Int, Int)]
    vectors = {
        "a": [(-1, 1), (-1, -1), (1, -1), (1, 1)],
        "b": [(1, -1), (-1, -1), (-1, 1), (1, 1)],
        "c": [(1, -1), (1, 1), (-1, 1), (-1, -1)],
        "D": [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    }
    # points :: Int -> ((Int, Int), Tree Char) -> [(Int, Int)]
    def points(d):
        """
        Size -> Centre of a Hilbert subtree -> All subtree points
        """
        def go(xy, tree):
            """
            go but with xy.
            """
            r = d // 2
            centres = map(
                lambda v: (xy[0] + (r * v[0]), xy[1] + (r * v[1])), vectors[tree["root"]])
            return chain.from_iterable(starmap(points(r), zip(centres, tree["nest"]))) if tree['nest'] else centres
        return lambda xy, tree: go(xy, tree)
    d = w // 2
    return lambda tree: list(points(d)((d, d), tree))
 
def svgFromPoints(w):
    """
    Width of square canvas -> Point list -> SVG string.
    svgFromPoints :: Int -> [(Int, Int)] -> SVG String
    """
    def go(w, xys):
        xs = " ".join(map(lambda xy: str(xy[0]) + " " + str(xy[1]), xys))
        return "\n".join(
            ["<svg xmlns='http://www.w3.org/2000/svg'",
             f"width='512' height='512' viewBox='5 5 {w} {w}'>",
             f"<path d='M{xs}' ",
             "stroke-width="2" stroke='red' fill='transparent'/>',
             "</svg>"])
    return lambda xys: go(w, xys) 
