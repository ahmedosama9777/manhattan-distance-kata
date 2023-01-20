class Point:
    
    def __init__(self, x: int, y: int):
        super(Point, self).__setattr__("_x", x)
        super(Point, self).__setattr__("_y", y)

    def __setattr__(self, name, value):
        raise AttributeError
    
    def distanceFrom(self, point_b):
        return abs(self._x - point_b._x) + abs(self._y - point_b._y)

def manhattanDistance(point_a: Point, point_b: Point) -> int:
    return point_a.distanceFrom(point_b)
