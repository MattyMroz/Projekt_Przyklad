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
        

    
    
    
    
# kopiowanie tekstu dopuki nie natrafi na daną fraze i zapisanie do pliku, jak natrafi na fraze to zapisuje do pliku o nazwie o 1 większą

def main():
    # zmienna do zwiększenia nazwy pliku
    i = 1
    # zmienna do zmiany frazy
    r = 26
    # fraza do wyszykiwania
    phrase = "Rozdział " + str(r)

    with open("0.1.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            if phrase in line:
                # zwiększenie nazwy pliku
                i += 1
                # zwiększenie frazy
                r += 25
                phrase = "Rozdział " + str(r)
                with open(str(i) + ".txt", "w", encoding="utf8") as f:
                    f.write(line)
            else:
                with open(str(i) + ".txt", "a", encoding="utf8") as f:
                    f.write(line)

main()




# Kopiowanie i przetłumacznie (bardziej powolne) stron internetowych z użyciem Selenium i Googletrans

# pip install -U selenium
# pip install googletrans
# pip install googletrans==3.1.0a0
# ChromeDriver -> C:\ Program Files (x86)\chromedriver.exe

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from googletrans import Translator

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


# Lista klas do przekopiowania
classes = ["tit", "chapter", "txt"]

# Lista rozdziałów
fristChapter = 1
lastChapter = 10

for i in range(fristChapter, lastChapter + 1):
    driver.get(
        "https://freewebnovel.com/i-was-a-sword-when-i-reincarnated/chapter-" + str(i) + ".html")

    for i in classes:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, i))
        )
        with open("1.txt", "a", encoding="utf-8") as f:
            f.write(element.text)
            f.write("\n")
        f.close()

driver.quit()

# # Przedmacz każdą linijkę tekstu odzielnie
# with open("1.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     f.close()

# with open("2.txt", "w", encoding="utf-8") as f:
#     for line in lines:
#         translator = Translator()
#         translation = translator.translate(line, dest="pl")
#         f.write(translation.text)
#         f.write("\n")
#     f.close()












# Projekt nowelki.py
# Kopiowanie i przetłumacznie stron internetowych z użyciem Selenium i Googletrans

# pip install -U selenium
# pip install googletrans
# pip install googletrans==3.1.0a0
# ChromeDriver -> C:\ Program Files (x86)\chromedriver.exe

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from googletrans import Translator


def main():
    print("Uruchamianie przeglądarki...")

main()


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


# Lista klas do przekopiowania
classes = ["tit", "chapter", "txt"]

# Lista rozdziałów w html
fristChapter = 1
lastChapter = 26


with open("0.txt", "w", encoding="utf-8") as f:
    f.write("")
    f.close()

for i in range(fristChapter, lastChapter + 1):
    driver.get(
        "https://freewebnovel.com/i-was-a-sword-when-i-reincarnated/chapter-" + str(i) + ".html")
    for i in classes:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, i))
        )
        with open("0.txt", "a", encoding="utf-8") as f:
            f.write(element.text)
            f.write("\n")
        f.close()

driver.quit()

# Przetłumaczanie tekstu 50 linijek na raz
with open("0.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    f.close()

with open("0.txt", "w", encoding="utf-8") as f:
    for i in range(0, len(lines), 50):
        translator = Translator()
        translation = translator.translate(
            "".join(lines[i:i + 50]), dest="pl")
        f.write(translation.text)
        f.write("\n")
    f.close()

# usuwanie danych zwrotów z pliku
words = ["(", ")", "[", "]", "<", ">", "{", "}", "\"", "『", "』",
         "…", "「", "」", "„", "”", "«", "»", "...", "*", "'", "〈", "〉"]
with open("0.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
with open("0.txt", "w", encoding="utf8") as f:
    for line in lines:
        for word in words:
            line = line.replace(word, "")
        f.write(line)

# kopiowanie tekstu dopuki nie natrafi na daną fraze i zapisanie do pliku, jak natrafi na fraze to zapisuje do pliku o nazwie o 1 większą

# zmienna do zwiększenia nazwy pliku
i = 1
# zmienna do zmiany frazy
r = 26
# fraza do wyszykiwania
phrase = "Rozdział " + str(r)

with open("0.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        if phrase in line:
            # zwiększenie nazwy pliku
            i += 1
            # zwiększenie frazy
            r += 25
            phrase = "Rozdział " + str(r)
            with open(str(i) + ".txt", "w", encoding="utf8") as f:
                f.write(line)
        else:
            with open(str(i) + ".txt", "a", encoding="utf8") as f:
                f.write(line)

# Usuwanie ostatniej linii z pliku opróćz ostatniego pliku
i = 1
while True:
    try:
        with open(str(i) + ".txt", "r", encoding="utf8") as f:
            lines = f.readlines()
            index = len(lines) - 1
            myException = lines[index]
            lines.pop()
            with open(str(i) + ".txt", "w", encoding="utf8") as f:
                f.writelines(lines)
    except FileNotFoundError:
        with open(str(i - 1) + ".txt", "a", encoding="utf8") as f:
            f.writelines(myException)
        break
    i += 1

# doanie na początek pliku tekstowego danej frazy z numeracją
i = 1
while True:
    try:
        phase = "I Was a Sword When I Reincarnated " + str(i)
        if i > 1:
            # po polsku ^ zmień na 0 by było dla plików od 1 do n
            phase += "\nBYŁEM MIECZEM PODCZAS REINKARNACJI"
        with open(str(i) + ".txt", "r", encoding="utf8") as f:
            # doanie na początek pliku tekstowego danej frazy
            lines = f.readlines()
            f.close()
        with open(str(i) + ".txt", "w", encoding="utf8") as f:
            f.write(phase)
            f.write("\n")
            f.writelines(lines)
            f.close()
    except FileNotFoundError:
        break
    i += 1
