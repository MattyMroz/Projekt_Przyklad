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
    words = ["(",")","[","]","<",">","{","}","\"","『","』","…","「","」","„","”","«","»"]
    # usuń words z pliku 3.txt i zapisz do 3.txt
    with open("1.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
    with open("1.txt", "w", encoding="utf8") as f:
        for line in lines:
            for word in words:
                line = line.replace(word, "")
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
