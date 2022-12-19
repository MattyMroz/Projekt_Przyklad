# otwórz plik liczby.txt
# 27
# 13
# 131
# 15
# 19
# 115
# 41
# 91
# 741
# 25
# 27

def zadanie4_1():
    with open('liczby.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if int(line[::-1]) % 17 == 0:
                print(line[::-1])


# zadanie4_1()


def zadanie4_2():
    with open('przyklad.txt', 'r') as f:
        max = 0
        max_wb = 0
        for line in f:
            line = line.strip()
            wb = abs(int(line) - int(line[::-1]))
            if wb > max:
                max = int(line)
                max_wb = abs(int(line) - int(line[::-1]))

        print(max, max_wb)


# zadanie4_2()


def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True
# print(czy_pierwsza(3))

def zadanie4_3():
    with open('przyklad.txt', 'r') as f:
        liczba = 0
        odbicie = 0
        for line in f:
            line = line.strip()
            liczba = int(line)
            odbicie = int(line[::-1])
            if (czy_pierwsza(liczba) and czy_pierwsza(odbicie)):
                print(liczba)

# zadanie4_3()


def zadanie4_4_1():
    with open('przyklad.txt', 'r') as f:
        tab = []
        for line in f:
            line = line.strip()
            tab.append(int(line))

        s = set(tab)
        print(len(s))

zadanie4_4_1()



def zadanie4_4_2():
    with open('przyklad.txt', 'r') as f:
        tab = []
        tab2 = []
        for line in f:
            line = line.strip()
            tab.append(int(line))

        for x in tab:
            if  tab.count(x) == 2:
                tab2.append(x)

        print(len(set(tab2)))

zadanie4_4_2()



def zadanie4_4_3():
    with open('przyklad.txt', 'r') as f:
        tab = []
        tab2 = []
        for line in f:
            line = line.strip()
            tab.append(int(line))

        for x in tab:
            if  tab.count(x) == 3:
                tab2.append(x)

        print(len(set(tab2)))

zadanie4_4_3()





