from src.Triangle import Triangle


def test_check_area(new_triangle):
    assert new_triangle.area() == 29.393876913398138


def test_check_perimeter(new_triangle):
    assert new_triangle.perimeter() == 32


def test_check_name(new_triangle):
    assert new_triangle.name == 'triangle'


def test_create_rectangle(new_triangle):
    assert isinstance(new_triangle, Triangle)


def test_check_add_area(new_triangle, new_square):
    assert new_triangle.add_area(new_square) == 78.39387691339815




