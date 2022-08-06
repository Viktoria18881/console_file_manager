# В модуле написать тесты для встроенных функций filter, map, sorted,
# а также для функций из библиотеки math: pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше
import math

def test_math_pi():
    assert round(math.pi, 2) == 3.14, 'Test failed!!!'

def test_math_sqrt():
    assert math.sqrt(2) == 2**(0.5), 'Test failed!!!'
    assert math.sqrt(4) == 2, 'Test failed!!!'

def test_math_pow():
    assert math.pow(2, 0.5) == 2 ** 0.5, 'Test failed!!!'
    assert math.pow(2, 3) == 8, 'Test failed!!!'
    assert math.pow(4, -1) == 0.25, 'Test failed!!!'
    assert math.pow(4, -0.5) == 0.5, 'Test failed!!!'


def test_math_hypot():
    assert math.hypot(2, 4) == (2 ** 2 + 4 ** 2) ** 0.5, 'Test failed!!!'
    assert math.hypot(-2, 0) == 2, 'Test failed!!!'
    assert math.hypot(0, 2) == 2, 'Test failed!!!'


def test_sorted():
    assert sorted([4, 3, 2]) == [2, 3, 4], 'Test failed!!!'
    assert sorted([3, 4, 2], reverse=True) == [4, 3, 2], 'Test failed!!!'


def test_map():
    assert list(map(lambda x: x**2, [1, 2, 3])) == [1, 4, 9], 'Test failed!!!'
    assert list(map(int, ['1', '2', '3'])) == [1, 2, 3], 'Test failed!!!'


def test_filter():
    assert list(filter(lambda x: x > 0, [-2, -1, 0, 1, 2])) == [1, 2], 'Test failed!!!'
    assert list(filter(lambda x: -1 < x < 1, [-2, -1, 0, 1, 2])) == [0], 'Test failed!!!'