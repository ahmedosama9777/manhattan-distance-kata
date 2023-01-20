from unittest import TestCase

from manhattan_distance import Point

class TestPoint(TestCase):
    def test_creation_of_point(self):
        point = Point(0, 0)

        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 0)