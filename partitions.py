import math
import numpy
import sys
import time
import tracemalloc


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
    if k <= 1:
        return k
    elif k == 2:
        return -1 if n % 2 else 1
    s, r, m = 0, 2, n % k
    for l in range(2 * k):
        if m == 0:
            s += (-1 if l % 2 else 1) * math.cos(math.pi * (6 * l - 1) / (6 * k))
        m += r
        if m >= k:
            m -= k
        r = r + 3
        if r >= k:
            r -= k
        return math.sqrt(k / 3) * s


def U(x):
    return math.cosh(x) - math.sinh(x) / x


def C(n):
    return math.pi / 6 * math.sqrt(24 * n - 1)


def partition_hrr(n):
    N = int(math.sqrt(n)) + 1
    answer = 0.0
    for k in range(1, N + 1):
        answer += (math.sqrt(3 / k) * (4 / (24 * n - 1))) * akn(k, n) * U(C(n) / k)
    return int(answer + 0.5)


def main():
    n = 10 ** 4
    start = time.perf_counter()
    tracemalloc.start()
    sys.stdout.write(f'p({n}) = {partition_pentagonal(n)}\n')
    end = time.perf_counter()
    sys.stdout.write(f'Memory used: {tracemalloc.get_traced_memory()[1] / 1024} KiB\n')
    sys.stdout.write(f'The pentagonal theorem gave {end - start:.8f} seconds to compute p({n}).\n')
    tracemalloc.stop()
    start = time.perf_counter()
    tracemalloc.start()
    sys.stdout.write(f'p({n}) = {partition_ewell(n)}\n')
    end = time.perf_counter()
    sys.stdout.write(f'Memory used: {tracemalloc.get_traced_memory()[1] / 1024} KiB\n')
    sys.stdout.write(f'Ewell\'s formula gave {end - start:.8f} seconds to compute p({n}).\n')
    tracemalloc.stop()
    start = time.perf_counter()
    tracemalloc.start()
    sys.stdout.write(f'p({n}) = {partition_hrr(n)}\n')
    end = time.perf_counter()
    sys.stdout.write(f'Memory used: {tracemalloc.get_traced_memory()[1] / 1024} KiB\n')
    sys.stdout.write(f'Johansson\'s formula gave {end - start:.8f} seconds to compute p({n}).\n')
    tracemalloc.stop()


if __name__ == '__main__':
    main()
