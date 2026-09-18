import sys
from concurrent.futures import ProcessPoolExecutor


def create_path(n, m):
    path = []

    interval_cur = 1
    current_num = 1
    while True:
        if current_num == 1 and interval_cur == 1 and len(path) > 0:
            break

        if interval_cur == 1:
            path.append(str(current_num))

        interval_cur += 1
        current_num += 1

        if interval_cur == m:
            interval_cur = 1
        if current_num > n:
            current_num = 1

    return "".join(path)


def main():
    args = sys.argv[1:]
    assert len(args) == 4, "Неправильно переданы аргументы"

    n1, m1, n2, m2 = [int(v) for v in args]

    with ProcessPoolExecutor(max_workers=2) as executor:
        t1 = executor.submit(create_path, n1, m1)
        t2 = executor.submit(create_path, n2, m2)

        p1, p2 = t1.result(), t2.result()
        print(p1 + p2)


if __name__ == "__main__":
    main()
