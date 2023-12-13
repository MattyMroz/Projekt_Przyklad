"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 8
"""


def main() -> None:
    """
        ? Zadanie 5.
            Napisz program, aby znaleźć maksymalną sumę od góry do dołu trójkąta pokazanego poniżej.

        * This function finds the maximum sum from top to bottom of the triangle shown below.

        ! NOTATKA:
        [3],
        [4, 6],
        [2, 7, 6],
        [8, 5, 9, 3] <- tu zanczymay

        np dla 2 bierzemt max(8, 5) i dodajemy do 2 => 10
        np dla 7 bierzemy max(5, 9) i dodajemy do 7 => 16
        np  dla 6 bierzemy max(9, 3) i dodajemy do 6 => 15
        [3],
        [4, 6],
        [10, 16, 15], <- tu zanczymay
        [8, 5, 9, 3]

        [25], <- wynik
        [20, 21], <- tu zanczymay
        [10, 16, 15],
        [8, 5, 9, 3]
    """
    triangle: list = [
        # [3],
        # [4, 6],
        # [2, 7, 6],
        # [8, 5, 9, 3]

        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    ]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # print(
            #     f"{triangle[i][j]} + max({triangle[i+1][j]}, {triangle[i+1][j+1]})")
            # Maximum sumy dwóch sąsiednich liczb w kolejnym rzędzie
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    print(f"Maksymalna suma od góry do dołu trójkąta: {triangle[0][0]}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
