def task1(input_list):
    unique_list = list(set(input_list))
    print(unique_list)
    return unique_list


def task2(min, max):

    # swap inputs on error input
    if max < min:
        max, min = min, max
        print(f'Max & Min swaped. Now Max={max}>Min={min}')

    print(min, max)

    # to include max if it is prime
    max += 1

    # build sieve and fill in primes list
    erat_sieve = [False if i % 2 == 0 else True for i in range(max)]
    primes = []
    for p in range(2, max):
        if erat_sieve[p]:
            if p >= min:
                primes.append(p)
            for i in range(p * p, max, p):
                erat_sieve[i] = False

    print(primes)
    return primes

# TASK3
class Point():
    def __init__(self, x, y, name='Point'):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return f"{self.name}: X={self.x} Y={self.y}"

    def get_coords(self):
        return self.x, self.y

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        return True

    def dist_to_point(self, point):
        xp, yp = point.get_coords()
        return ((self.x-xp)**2+(self.y-yp)**2)**0.5
    

def task4(input_list, ascending=True):

    return sorted(input_list,
                  key=lambda x: len(x),
                  reverse=not ascending)

if __name__ == '__main__':

    print('TASK_1:')
    assert task1([1, 2, 3, 3, 7]) == [1, 2, 3, 7]

    print('\nTASK_2:')
    assert task2(13, 50) == [13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert task2(50, 13) == [13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert task2(13, 47) == [13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert task2(10, 50) == [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert task2(47, 47) == [47]
    assert task2(50, 50) == []

    print('\nTASK_3:')
    point_a = Point(77, 89, 'Pt_A')
    point_b = Point(81, 92, 'Pt_B')
    assert point_a.dist_to_point(point_b) == 5
    assert point_a.get_coords() == (77, 89)
    assert point_a.set_coords(100, 100) is True
    assert point_b.set_coords(110, 100) is True
    assert point_a.dist_to_point(point_b) == 10
    assert str(point_a) == "Pt_A: X=100 Y=100"

    print('\nTASK_4:')
    print(task4(['abc', 'ab', 'abcdef', 'a']))
    print(task4(['abc', 'ab', 'abcdef', 'a'], False))
    assert task4(['abc', 'ab', 'abcdef', 'a']) == ['a', 'ab', 'abc', 'abcdef']
    assert task4(['abc', 'ab', 'abcdef', 'a'], False) == ['abcdef', 'abc', 'ab', 'a']