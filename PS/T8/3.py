"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 8
"""


def main() -> None:
    """
        ? Zadanie 3.
            Napisz program, aby znaleźć numer początkowy, poniżej dziesięciu tysięcy stworzy najdłuższy łańcuch.

        * This function finds the starting number, under ten thousand, that produces the longest chain according to the Collatz hypothesis.
    """
    def collatz_chain_length(n: int) -> int:
        length: int = 1
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            length += 1
        return length

    max_length: int = 0
    max_start: int = 0
    for i in range(1, 10000):
        length = collatz_chain_length(i)
        if length > max_length:
            max_length = length
            max_start = i
    print(
        f"Numer początkowy, poniżej dziesięciu tysięcy, który tworzy najdłuższy łańcuch: {max_start}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
