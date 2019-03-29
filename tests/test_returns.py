from returns import returns

__author__ = 'Michael'


def test_int():
    @returns(int)
    def parse_int(x):
        return x

    assert parse_int(1) == 1
    assert parse_int(1.5) == 1
    assert parse_int('1') == 1


def test_generator():
    @returns(tuple)
    def tuple_range(n):
        yield from range(n)

    assert tuple_range(5) == (0, 1, 2, 3, 4)
