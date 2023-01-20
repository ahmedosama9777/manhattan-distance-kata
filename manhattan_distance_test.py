from unittest import TestCase

from manhattan_distance import Point, manhattanDistance


class TestPoint(TestCase):
    def setUp(self) -> None:
        self.point = Point(1, 0)

    def test_creation_of_point(self):
        x = self.point._x

    def test_point_is_immutable(self):
        with self.assertRaises(AttributeError):
            self.point._x = 2

    def test_get_manhattan_distance(self):
        point_a = Point(3, 5)
        point_b = Point(1, 2)

        manhattan_distance = manhattanDistance(point_a, point_b)

        self.assertEqual(manhattan_distance, 5)