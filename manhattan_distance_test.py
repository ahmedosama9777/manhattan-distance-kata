from unittest import TestCase

from manhattan_distance import Point


class TestPoint(TestCase):
    def setUp(self) -> None:
        self.point = Point(1, 0)

    def test_creation_of_point(self):
        self.assertEqual(self.point.x, 1)
        self.assertEqual(self.point.y, 0)

    def test_point_is_immutable(self):
        with self.assertRaises(AttributeError):
            self.point.x = 2
