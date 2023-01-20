class Point:
    def __init__(self, x: int, y: int):
        super(Point, self).__setattr__("x", x)
        super(Point, self).__setattr__("y", y)

    def __setattr__(self, name, value):
        raise AttributeError
