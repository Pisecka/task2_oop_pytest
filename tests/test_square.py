from src.Square import Square


def test_check_area(new_square):
    assert new_square.area() == 49


def test_check_perimeter(new_square):
    assert new_square.perimeter() == 28


def test_check_name(new_square):
    assert new_square.name == 'square'


def test_create_rectangle(new_square):
    assert isinstance(new_square, Square)


def test_check_add_area(new_square, new_triangle):
    assert new_square.add_area(new_triangle) == 78.39387691339815




