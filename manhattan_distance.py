class Point:
    def __init__(self, x: int, y: int):
        super(Point, self).__setattr__("__x", x)
        super(Point, self).__setattr__("__y", y)

    def __setattr__(self, name, value):
        raise AttributeError
