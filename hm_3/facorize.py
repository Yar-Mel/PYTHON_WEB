
import time
from multiprocessing import cpu_count, Pool


numbers_to_calc = 128, 255, 99999, 10651060


def factorize_number(num: int) -> list:
    return [x for x in range(1, num + 1) if x % 2 == 0]


def factorize_synch(*numbers) -> list:
    start_time = time.time()
    result = []
    for num in numbers:
        result.append(factorize_number(num))
    print(f'Synch process finished by {time.time() - start_time} sec.')
    return result


def factorize_parallel(*numbers) -> list:
    cpu_num = cpu_count()
    start_time = time.time()
    pool = Pool(cpu_num)
    result = pool.map(factorize_number, numbers)
    print(f'Parallel {cpu_num} process finished by {time.time() - start_time} sec.')
    return result


def main() -> None:
    factorize_synch(*numbers_to_calc)
    factorize_parallel(*numbers_to_calc)


if __name__ == '__main__':
    main()
