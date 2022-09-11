# Kopiowanie i przetłumacznie stron internetowych z użyciem Selenium i Googletrans

# pip install -U selenium
# pip install googletrans
# pip install googletrans==3.1.0a0
# ChromeDriver z twoją wersją Chrome -> C:\ Program Files (x86)\chromedriver.exe

# IMPORTOWANIE MODUŁÓW
import contextlib
from distutils.command.build_scripts import first_line_re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from googletrans import Translator

# ----------------------------------------------
#                ZMIENNE GLOBALNE
# ----------------------------------------------
#            USTAWIENIA PRZEGLĄDARKI
# ----------------------------------------------

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# ----------------------------------------------
#     WYBÓR LINKÓW STRON DO PRZETŁUMACZENIA
# ----------------------------------------------
# 1 = Automatyczne numeracja - webs1
# 2 = Lista stron - webs2

# setWebsides = 1
setWebsides = 2

# ----------------------------------------------
#      lICZBA ROZDZIAŁÓW DO PRZETŁUMACZENIA
# ----------------------------------------------
# if setWebsides == 1:

fristChapter = 1
lastChapter = 51

# ----------------------------------------------
#    NAZWY KLAS Z KTÓRYCH POBIERZEMY TEKST
# ----------------------------------------------

classes = ["tit", "chapter", "txt"]

# ----------------------------------------------
#   PODZIAŁ - ILE ROZDZIAŁÓW W JEDNYM PLIKU
# ----------------------------------------------

ChaptersInFile = 25


# ----------------------------------------------
#           NAZWA PLIKU WYJŚCIOWEGO
# ----------------------------------------------

fileName = "nowy"

# ----------------------------------------------
# NUMER PLIKU WYJŚCIOWEGO I NUMERACJA ROZDZIAŁÓW
# ----------------------------------------------

fileNumber = 1

# ----------------------------------------------
#                 TYTUŁ KSIĄŻKI
# ----------------------------------------------

bookName = "I Was a Sword When I Reincarnated"
bookNamePL = "BYŁEM MIECZEM PODCZAS REINKARNACJI"

# ----------------------------------------------

# GŁÓWNA FUNKCJA


def main():
    print("-----------------------------")
    print("Pobiernie danych z linków...")
    selectWebs(setWebsides)

    print("-----------------------------")
    print("Tłumaczenie tekstu...")
    translate()

    print("-----------------------------")
    print("Usuwanie wybranych słów i znaków...")
    erasingWords()

    print("-----------------------------")
    print("Podział na pliki - ile rozdziałów w jednym pliku...")
    createFiles()

    print("-----------------------------")
    print("Poprawianie, nadawanie tytułów i numeracji...")
    bookTitle()

    print("Zakończono :)")
    driver.quit()


# WYBÓR LINKÓW STRON DO PRZETŁUMACZENIA


def selectWebs(num):
    match num:
        case 1:
            print("Wybrano 1 = Automatyczne numeracja - webs1.txt")
            webs1 = getWebs(num)
            getData1(webs1)
        case 2:
            print("Wybrano 2 = Lista stron - webs2.txt")
            webs2 = getWebs(num)
            getData2(webs2)
        case _:
            print("Nie ma takiej opcji")
            return 0

# POBRANIE LINKÓW STRON


def getWebs(num):
    with open("webs" + str(num) + ".txt", "r", encoding="utf-8") as f:
        web = f.readlines()
        f.close()
    return web

# POBRANIE DANYCH ZE STRON 1


def getData1(webs1):
    # Tworzenie pliku lub czyszczenie go
    with open("0.txt", "w", encoding="utf-8") as f:
        f.write("")
        f.close()

   # Pętla pobierająca dane
    for i in range(fristChapter, lastChapter + 1):
        driver.get(webs1[0] + str(i) + webs1[1])
        for i in classes:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, i))
            )
            with open("0.txt", "a", encoding="utf-8") as f:
                f.write(element.text)
                f.write("\n")
            f.close()

    driver.quit()

# POBRANIE DANYCH ZE STRON 2


def getData2(webs2):
    # Tworzenie pliku lub czyszczenie go
    with open("0.txt", "w", encoding="utf-8") as f:
        f.write("")
        f.close()

   # Pętla pobierająca dane
    for i in webs2:
        driver.get(i)
        for i in classes:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, i))
            )
            with open("0.txt", "a", encoding="utf-8") as f:
                f.write(element.text)
                f.write("\n")
            f.close()

    driver.quit()

# TŁUMACZENIE TEKSTU NA POLSKI


def translate():

    with open("0.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()

    # 50 linijek tekstu na raz
    with open("0.txt", "w", encoding="utf-8") as f:
        for i in range(0, len(lines), 50):
            translator = Translator()
            translation = translator.translate(
                "".join(lines[i:i + 50]), dest="pl")
            f.write(translation.text)
            f.write("\n")
        f.close()


# USUWANIE WYBRANYCH SŁOWÓW I ZNAKÓW


def erasingWords():
    words = ["(", ")", "[", "]", "<", ">", "{", "}", "\"", "『", "』",
             "…", "「", "」", "„", "”", "«", "»", "...", "*", "'", "〈", "〉"]
    with open("0.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
    with open("0.txt", "w", encoding="utf8") as f:
        for line in lines:
            for word in words:
                line = line.replace(word, "")
            f.write(line)

# PODZIAŁ NA PLIKI - ILE ROZDZIAŁÓW W JEDNYM PLIKU


def createFiles():
    # Numer pliku wyjściowego
    fNum = fileNumber
    # zmienna do zmiany frazy
    chapter = ChaptersInFile + 1
    # fraza do wyszykiwania
    phrase = "Rozdział " + str(chapter)

    with open("0.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            if phrase in line:
                # zwiększenie nazwy pliku
                if chapter == fristChapter:
                    fNum = fileNumber
                else:
                    fNum += 1
                # zwiększenie frazy
                chapter += ChaptersInFile
                phrase = "Rozdział " + str(chapter)
                with open(fileName + " " + str(fNum) + ".txt", "w", encoding="utf8") as f:
                    f.write(line)
            else:
                with open(fileName + " " + str(fNum) + ".txt", "a", encoding="utf8") as f:
                    f.write(line)


# POPRAWIANIE, NADAWANIE TYTUŁÓW I NUMERACJI


def bookTitle():
    i = fileNumber
    while True:
        try:
            with open(fileName + " " + str(i) + ".txt", "r", encoding="utf8") as f:
                lines = f.readlines()
                index = len(lines) - 1
                myException = lines[index]
                lines.pop()
                with open(fileName + " " + str(i) + ".txt", "w", encoding="utf8") as f:
                    f.writelines(lines)
        except FileNotFoundError:
            with open(fileName + " " + str(i - 1) + ".txt", "a", encoding="utf8") as f:
                with contextlib.suppress(NameError):
                    f.writelines(myException)
            break
        i += 1
    i = fileNumber
    while True:
        try:
            phase = bookName + " " + str(i)
            if fileNumber > 1 and (i <= fileNumber - 1 and i > fileNumber or i > fileNumber - 1):
                phase += "\n" + bookNamePL
            # if fileNumber > 1:
            #     if i > fileNumber - 1:
            #         phase += "\n" + bookNamePL
            #     else:
            #         if i > fileNumber:
            #             phase += "\n" + bookNamePL
            with open(fileName + " " + str(i) + ".txt", "r", encoding="utf8") as f:
                lines = f.readlines()
                f.close()
            with open(fileName + " " + str(i) + ".txt", "w", encoding="utf8") as f:
                f.write(phase)
                f.write("\n")
                f.writelines(lines)
                f.close()
        except FileNotFoundError:
            break
        i += 1


main()









































# Kopiowanie i przetłumacznie stron internetowych z użyciem Selenium i Googletrans

# pip install -U selenium
# pip install googletrans
# pip install googletrans==3.1.0a0
# ChromeDriver z twoją wersją Chrome -> C:\ Program Files (x86)\chromedriver.exe

# IMPORTOWANIE MODUŁÓW
import contextlib
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from googletrans import Translator

# ----------------------------------------------
#                ZMIENNE GLOBALNE
# ----------------------------------------------
#            USTAWIENIA PRZEGLĄDARKI
# ----------------------------------------------

# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

# ----------------------------------------------
#     WYBÓR LINKÓW STRON DO PRZETŁUMACZENIA
# ----------------------------------------------
# 1 = Automatyczne numeracja - webs1
# 2 = Lista stron - webs2

setWebsides = 1
# setWebsides = 2

# ----------------------------------------------
#      lICZBA ROZDZIAŁÓW DO PRZETŁUMACZENIA
# ----------------------------------------------
# if setWebsides == 1:

fristChapter = 976
lastChapter = 1100

# ----------------------------------------------
#    NAZWY KLAS Z KTÓRYCH POBIERZEMY TEKST
# ----------------------------------------------

classes = ["tit", "chapter", "txt"]

# ----------------------------------------------
#   PODZIAŁ - ILE ROZDZIAŁÓW W JEDNYM PLIKU
# ----------------------------------------------

ChaptersInFile = 25


# ----------------------------------------------
#           NAZWA PLIKU WYJŚCIOWEGO
# ----------------------------------------------

fileName = "nowy"

# ----------------------------------------------
# NUMER PLIKU WYJŚCIOWEGO I NUMERACJA ROZDZIAŁÓW
# ----------------------------------------------

fileNumber = 40

# ----------------------------------------------
#                 TYTUŁ KSIĄŻKI
# ----------------------------------------------

bookName = "Earth's Greatest Magus"
bookNamePL = "Największy Mag Ziemi"

# ----------------------------------------------

# GŁÓWNA FUNKCJA


def main():
    print("-----------------------------")
    print("Pobiernie danych z linków...")
    selectWebs(setWebsides)

    print("-----------------------------")
    print("Tłumaczenie tekstu...")
    translate()

    print("-----------------------------")
    print("Usuwanie wybranych słów i znaków...")
    erasingWords()

    print("-----------------------------")
    print("Podział na pliki - ile rozdziałów w jednym pliku...")
    createFiles()

    print("-----------------------------")
    print("Poprawianie, nadawanie tytułów i numeracji...")
    bookTitle()

    print("Zakończono :)")


# WYBÓR LINKÓW STRON DO PRZETŁUMACZENIA


def selectWebs(num):
    match num:
        case 1:
            print("Wybrano 1 = Automatyczne numeracja - webs1.txt")
            webs1 = getWebs(num)
            getData1(webs1)
        case 2:
            print("Wybrano 2 = Lista stron - webs2.txt")
            webs2 = getWebs(num)
            getData2(webs2)
        case _:
            print("Nie ma takiej opcji")
            return 0

# POBRANIE LINKÓW STRON


def getWebs(num):
    with open("webs" + str(num) + ".txt", "r", encoding="utf-8") as f:
        web = f.readlines()
        f.close()
    return web

# POBRANIE DANYCH ZE STRON 1


def getData1(webs1):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # Tworzenie pliku lub czyszczenie go
    with open("0.txt", "w", encoding="utf-8") as f:
        f.write("")
        f.close()

   # Pętla pobierająca dane
    for i in range(fristChapter, lastChapter + 1):
        driver.get(webs1[0] + str(i) + webs1[1])
        for i in classes:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, i))
            )
            with open("0.txt", "a", encoding="utf-8") as f:
                f.write(element.text)
                f.write("\n")
            f.close()

    driver.quit()

# POBRANIE DANYCH ZE STRON 2


def getData2(webs2):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # Tworzenie pliku lub czyszczenie go
    with open("0.txt", "w", encoding="utf-8") as f:
        f.write("")
        f.close()

   # Pętla pobierająca dane
    for i in webs2:
        driver.get(i)
        for i in classes:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, i))
            )
            with open("0.txt", "a", encoding="utf-8") as f:
                f.write(element.text)
                f.write("\n")
            f.close()

    driver.quit()

# TŁUMACZENIE TEKSTU NA POLSKI


def translate():
    with open("0.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()

    # 50 linijek tekstu na raz
    with open("0.txt", "w", encoding="utf-8") as f:
        for i in range(0, len(lines), 50):
            translator = Translator()
            translation = translator.translate(
                "".join(lines[i:i + 50]), dest="pl")
            f.write(translation.text)
            f.write("\n")
        f.close()


# USUWANIE WYBRANYCH SŁOWÓW I ZNAKÓW


def erasingWords():
    words = ["(", ")", "[", "]", "<", ">", "{", "}", "\"", "『", "』",
             "…", "「", "」", "„", "”", "«", "»", "...", "*", "'", "〈", "〉", "﻿"]
    with open("0.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
    with open("0.txt", "w", encoding="utf8") as f:
        for line in lines:
            for word in words:
                line = line.replace(word, "")
            f.write(line)

# PODZIAŁ NA PLIKI - ILE ROZDZIAŁÓW W JEDNYM PLIKU


def createFiles():
    # Numer pliku wyjściowego
    fNum = fileNumber
    # zmienna do zmiany frazy
    chapter = fristChapter
    # fraza do wyszykiwania
    phrase = "Rozdział " + str(chapter)

    with open("0.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            if phrase in line:
                # zwiększenie nazwy pliku
                if chapter == fristChapter:
                    fNum = fileNumber
                else:
                    fNum += 1
                # zwiększenie frazy
                chapter += ChaptersInFile
                phrase = "Rozdział " + str(chapter)
                with open(fileName + " " + str(fNum) + ".txt", "w", encoding="utf8") as f:
                    f.write(line)
            else:
                with open(fileName + " " + str(fNum) + ".txt", "a", encoding="utf8") as f:
                    f.write(line)


# POPRAWIANIE, NADAWANIE TYTUŁÓW I NUMERACJI


def bookTitle():
    i = fileNumber
    while True:
        try:
            with open(fileName + " " + str(i) + ".txt", "r", encoding="utf8") as f:
                lines = f.readlines()
                index = len(lines) - 1
                myException = lines[index]
                lines.pop()
                with open(fileName + " " + str(i) + ".txt", "w", encoding="utf8") as f:
                    f.writelines(lines)
        except FileNotFoundError:
            with open(fileName + " " + str(i - 1) + ".txt", "a", encoding="utf8") as f:
                with contextlib.suppress(NameError):
                    f.writelines(myException)
            break
        i += 1
    i = fileNumber
    while True:
        try:
            phase = bookName + " " + str(i)
            if fileNumber > 1 and (i <= fileNumber - 1 and i > fileNumber or i > fileNumber - 1):
                phase += "\n" + bookNamePL
            # if fileNumber > 1:
            #     if i > fileNumber - 1:
            #         phase += "\n" + bookNamePL
            #     else:
            #         if i > fileNumber:
            #             phase += "\n" + bookNamePL
            with open(fileName + " " + str(i) + ".txt", "r", encoding="utf8") as f:
                lines = f.readlines()
                f.close()
            with open(fileName + " " + str(i) + ".txt", "w", encoding="utf8") as f:
                f.write(phase)
                f.write("\n")
                f.writelines(lines)
                f.close()
        except FileNotFoundError:
            break
        i += 1


main()
















































# łączenie 2 linii w 1 linię i zapis do pliku
def main():
    with open('1.1.txt', 'r') as f:
        for line in f:
            with open('1.1_out.txt', 'a') as f2:
                line = line.strip() + ' = ' + next(f).strip()
                f2.write(line + '\n')


main()

# zamiana słów za i przed zankiem występującym w tej linii
def main():
    with open('1.1_out.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            if '=' in line:
                before = line.split('=')[0]
                after = line.split('=')[1]
                with open('1.1_out2.txt', 'a') as f2:
                    f2.write(after + ' = ' + before + '\n')


main()


# usuwanie numeracji stron z pliku tekstowego
a = open('3.txt', 'r', encoding="utf8")
b = open('t3.txt', 'w', encoding="utf8")

for line in a:
    if line[0] in '0123456789':
        continue
    else:
        b.write(line)


# usuwanie danych zwrotów z pliku
def main():
    words = ["(",")","[","]","<",">","{","}","\"","『","』","…","「","」","„","”","«","»","..."]
    # usuń words z pliku 3.txt i zapisz do 3.txt
    with open("1.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
    with open("1.txt", "w", encoding="utf8") as f:
        for line in lines:
            for word in words:
                line = line.replace(word, "")
            f.write(line)

main()

