import pytest
from triangle_app import *


p = Triangle()


@pytest.mark.parametrize("x", [3, 1, -1, 0, 250], ids=["positive", "positive", "negative", "zero", "too_much"])
@pytest.mark.parametrize("y", [4])
@pytest.mark.parametrize("z", [5])
def test_is_triangle(x, y, z):
    pytest.status, result = p.is_triangle()
    print("x:{0},y:{1},z:{2}".format(x, y, z))
    assert pytest.status == True
