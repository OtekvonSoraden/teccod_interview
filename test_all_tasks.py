from teccod_test_tasks import (task1, task2, task4, Point)


def test_task1():
    assert task1([1, 2, 3, 3, 7]) == [1, 2, 3, 7]


def test_task2():
    assert task2(13, 50) == [13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert task2(50, 13) == [13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert task2(13, 47) == [13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert task2(10, 50) == [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert task2(47, 47) == [47]
    assert task2(50, 50) == []


def test_task3():
    point_a = Point(77, 89, 'Pt_A')
    point_b = Point(81, 92, 'Pt_B')
    assert point_a.dist_to_point(point_b) == 5
    assert point_a.get_coords() == (77, 89)
    assert point_a.set_coords(100, 100) is True
    assert point_b.set_coords(110, 100) is True
    assert point_a.dist_to_point(point_b) == 10
    assert str(point_a) == "Pt_A: X=100 Y=100"
    assert point_a.set_coords(-100, -100) is True
    assert point_b.set_coords(-110, -110) is True
    assert point_a.dist_to_point(point_b) == 10*2**0.5
    assert point_a.set_coords(-100.1, 100.2) is True
    assert point_b.set_coords(-110.1, 110.2) is True
    assert point_a.dist_to_point(point_b) == 10*2**0.5


def test_task4():
    assert task4(['abc', 'ab', 'abcdef', 'a']) == ['a', 'ab', 'abc', 'abcdef']
    assert task4(['abc', 'ab', 'abcdef', 'a'], False) == [
        'abcdef', 'abc', 'ab', 'a']