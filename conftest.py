import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture()
def new_rectangle():
    r1 = Rectangle('rect1', 5, 10)

    yield r1

    del r1


@pytest.fixture()
def new_square():
    s1 = Square('square', 7)

    yield s1

    del s1


@pytest.fixture()
def new_circle():
    c1 = Circle('circle1', 10)

    yield c1

    del c1


@pytest.fixture()
def new_triangle():
    t1 = Triangle('triangle', 7, 10, 15)

    yield t1

    del t1