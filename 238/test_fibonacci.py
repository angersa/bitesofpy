import pytest

from fibonacci import fib

# write one or more pytest functions below, they need to start with test_

@pytest.mark.parametrize("n", [
    -1,
    -5,
])

def test_fib_value_error(n):
    with pytest.raises(ValueError):
        fib(n)

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (5, 5),
    (10, 55),
])
def test_fib_n(n, expected):
    assert fib(n) == expected
