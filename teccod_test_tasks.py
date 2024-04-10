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
            for i in range(p**2, max, p):
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
