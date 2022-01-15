from src.Circle import Circle
import math

def test_check_area(new_circle):
    assert new_circle.area() == math.pi * 10 * 10


def test_check_perimeter(new_circle):
    assert new_circle.perimeter() == 2 * math.pi * 10


def test_check_name(new_circle):
    assert new_circle.name == 'circle1'


def test_create_rectangle(new_circle):
    assert isinstance(new_circle, Circle)


def test_check_add_area(new_circle, new_square):
    assert new_circle.add_area(new_square) == math.pi * 10 * 10 + 49




