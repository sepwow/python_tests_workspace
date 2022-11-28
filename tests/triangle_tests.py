import pytest
from triangle_app import*


p = triangle()
@pytest.mark.parametrize(“a”, [3, 1, -1, 0, 250], ids=["positive", "positive", "negative", "zero", "too_much"])
@pytest.mark.parametrize(“b”, [4])
@pytest.mark.parametrize(“c”, [5])
def test_triangle():
    print()
    assert True