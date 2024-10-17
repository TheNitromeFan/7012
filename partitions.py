import sys
import time


def partition_pentagonal(n):
    table = [1]
    for i in range(1, n + 1):
        result = 0
        k = 1
        sign = 1
        while True:
            pentagonal = (3 * k - 1) * k // 2
            if pentagonal > i:
                break
            result += sign * table[i - pentagonal]
            k += 1
            sign *= -1
        k = -1
        sign = 1
        while True:
            pentagonal = (3 * k - 1) * k // 2
            if pentagonal > i:
                break
            result += sign * table[i - pentagonal]
            k -= 1
            sign *= -1
        table.append(result)
    return table[-1]


def partition_ewell(n):
    table = [1]
    for i in range(1, n + 1):
        result = 0
        k = 0
        while True:
            m = i - k * (k + 1) // 2
            if m < 0:
                break
            elif m % 4 == 0:
                result += table[m // 4]
            k += 1
        k = 1
        sign = 1
        while True:
            m = i - 2 * k ** 2
            if m < 0:
                break
            result += 2 * sign * table[m]
            k += 1
            sign *= -1
        table.append(result)
    return table[-1]


def akn(k, n):
    # TODO: implement two version of this
    pass


def partition_hrr(n):
    # TODO: implement this
    pass


def main():
    n = 50000
    start = time.perf_counter()
    print(partition_pentagonal(n))
    end = time.perf_counter()
    sys.stdout.write(f'The pentagonal theorem gave {end - start:.3f} seconds to compute p({n}).\n')
    start = time.perf_counter()
    print(partition_ewell(n))
    end = time.perf_counter()
    sys.stdout.write(f'Ewell\'s formula gave {end - start:.3f} seconds to compute p({n}).\n')


if __name__ == '__main__':
    main()
