from src.Rectangle import Rectangle


def test_check_area(new_rectangle):
    assert new_rectangle.area() == 50


def test_check_perimeter(new_rectangle):
    assert new_rectangle.perimeter() == 30


def test_check_name(new_rectangle):
    assert new_rectangle.name == 'rect1'


def test_create_rectangle(new_rectangle):
    assert isinstance(new_rectangle, Rectangle)


def test_check_add_area(new_rectangle, new_square):
    assert new_rectangle.add_area(new_square) == 99




