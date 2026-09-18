import sys
from decimal import Decimal


def main():
    coords_file_path = sys.argv[1]
    points_file_path = sys.argv[2]

    with open(coords_file_path, mode="r", encoding="utf8") as f:
        center_x, center_y = [Decimal(v) for v in f.readline().split()]
        radius_x, radius_y = [Decimal(v) for v in f.readline().split()]

    with open(points_file_path, mode="r", encoding="utf8") as f:
        for point in f:
            x, y = point.split()

            res = (Decimal(x) - center_x)**2 / radius_x**2 + (Decimal(y) - center_y)**2 / radius_y**2

            if res > 1:
                # снаружи
                print(2)
            elif res < 1:
                # внутри
                print(1)
            else:
                # на окружности
                print(0)


if __name__ == "__main__":
    main()
