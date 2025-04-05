import pytest 

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def test_square():
    assert square(2) == 4, "Test failed: square(2) should be 4"
    assert square(3) == 9, "Test failed: square(3) should be 9"

def test_cube():
    assert cube(2) == 8, "Test failed: cube(2) should be 8"
    assert cube(3) == 27, "Test failed: cube(3) should be 27"

def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")