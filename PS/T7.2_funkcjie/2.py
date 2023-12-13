"""
    ! Mateusz Mróz
    ! Informatyka, grupa 1I05
    ! Numer albumu: 251190

    * Temat 7.2: Funkcje
"""


def main() -> None:
    """
        ? Zadanie 2.
            Napisz program do generowania (z podaniem liczby całkowitej n) kwadratowej macierzy wypełnionej elementami od 1 do n2 w kolejności spiralnej.

        * This function generates a square matrix filled with elements from 1 to n^2 in a spiral order.
    """
    try:
        n: int = int(input("Podaj liczbę całkowitą n: "))
        dx, dy = 0, 1
        x, y = 0, 0
        matrix: list = [[None]*n for _ in range(n)]  # Inicjalizacja macierzy
        for i in range(1, n**2+1):  # Dla każdego elementu od 1 do n^2
            matrix[x][y] = i  # Wypełniamy macierz
            nx, ny = x+dx, y+dy  # Obliczamy następny element
            # Jeśli potencjalny następny element jest w macierzy i jest pusty
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == None:
                x, y = nx, ny  # To przesuwamy się do niego
            else:
                # W przeciwnym razie zmieniamy kierunek i przesuwamy się o jeden element w nowym kierunku
                dx, dy = dy, -dx  # Obrót o 90 stopni w prawo
                x, y = x+dx, y+dy

        for x in matrix:
            for y in x:
                print(y, end=' ')
            print()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
