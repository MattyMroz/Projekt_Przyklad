import threading

counter = 0
lock = threading.Lock()

lock.acquire()
lock.release()
lock.locked()
def increment():
    global counter
    with lock:
        counter += 1

def worker():
    for _ in range(100000):
        increment()

# Tworzenie wątków
threads = []
for _ in range(10):
    t = threading.Thread(target=worker)
    threads.append(t)

# Uruchamianie wątków
for t in threads:
    t.start()

# Oczekiwanie na zakończenie wątków
for t in threads:
    t.join()

print("Wartość licznika:", counter)


# import datetime
# import time


# def current_datetime_with_nanoseconds():
#     current_date = datetime.datetime.now()
#     current_time = current_date.strftime('%H:%M:%S')
#     milliseconds = current_date.strftime('%f')[:3]
#     microseconds = current_date.strftime('%f')[3:6]
#     nanoseconds = time.perf_counter_ns() % 1000

#     return f"{current_date.year}-{current_date.month:02d}-{current_date.day:02d} {current_time}:{milliseconds}:{microseconds}:{nanoseconds:03d}"


# current_datetime = current_datetime_with_nanoseconds()
# print(current_datetime)


# import datetime
# import time
# from dataclasses import dataclass


# @dataclass(init=True)
# class ExecutionTime:
#     start_time: int = None
#     start_date: str = None
#     end_time: int = None
#     end_date: str = None

#     def __post_init__(self):
#         self.start_time = time.perf_counter_ns()
#         self.start_date = self.current_datetime_with_nanoseconds()

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.end_time = time.perf_counter_ns()
#         self.end_date = self.current_datetime_with_nanoseconds()

#         self.display_time()

#     def current_datetime_with_nanoseconds(self) -> str:
#         current_date = datetime.datetime.now()
#         current_time = current_date.strftime('%H:%M:%S')
#         milliseconds = current_date.strftime('%f')[:3]
#         microseconds = current_date.strftime('%f')[3:6]
#         nanoseconds = self.start_time % 1000

#         return f"{current_date.year}-{current_date.month:02d}-{current_date.day:02d} {current_time}:{milliseconds}:{microseconds}:{nanoseconds:03d}"

#     def calculate_duration(self) -> str:
#         duration_ns = self.end_time - self.start_time
#         duration_s, duration_ns = divmod(duration_ns, 1_000_000_000)
#         duration_ms, duration_ns = divmod(duration_ns, 1_000_000)
#         duration_us, duration_ns = divmod(duration_ns, 1_000)

#         hours, remainder = divmod(duration_s, 3600)
#         minutes, seconds = divmod(remainder, 60)

#         return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{duration_ms:03d}:{duration_us:03d}:{duration_ns:03d}"

#     def display_time(self):
#         print()
#         print(f"[START] {self.start_date}")
#         print(f"[END]   {self.end_date}")
#         print("[TIME]  hh:mm:ss:ms:us:ns")
#         print(f"        {self.calculate_duration()}")
#         print()


# def calculate_sum(n: int) -> int:
#     sum_result: int = 0
#     for i in range(1, n + 1):
#         sum_result += i
#         time.sleep(.5)  # Symulacja długotrwałej operacji
#     return sum_result


# with ExecutionTime():
#     result: int = calculate_sum(5)
#     print("The sum is:", result)


# import datetime
# import time
# from dataclasses import dataclass


# @dataclass(init=True)
# class ExecutionTime:
#     start_time: int = None
#     start_date: datetime.datetime = None
#     end_time: int = None
#     end_date: datetime.datetime = None

#     def __post_init__(self):
#         self.start_time = time.perf_counter_ns()
#         self.start_date = datetime.datetime.now()

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.end_time = time.perf_counter_ns()
#         self.end_date = datetime.datetime.now()

#         self.display_time()

#     def calculate_duration(self) -> str:
#         duration_ns = self.end_time - self.start_time
#         duration_s, duration_ns = divmod(duration_ns, 1_000_000_000)
#         duration_ms, duration_ns = divmod(duration_ns, 1_000_000)
#         duration_us, duration_ns = divmod(duration_ns, 1_000)

#         hours, remainder = divmod(duration_s, 3600)
#         minutes, seconds = divmod(remainder, 60)

#         return f"{hours:02}:{minutes:02}:{seconds:02}:{duration_ms:03}:{duration_us:03}:{duration_ns:03}"

#     def display_time(self):
#         print()
#         print(f"[START] {self.start_date.strftime('%Y-%m-%d %H:%M:%S:%f')[:-3]}")
#         print(f"[END]   {self.end_date.strftime('%Y-%m-%d %H:%M:%S:%f')[:-3]}")
#         print("[TIME]  hh:mm:ss:ms:us:ns")
#         print(f"        {self.calculate_duration()}")
#         print()


# def calculate_sum(n: int) -> int:
#     sum_result: int = 0
#     for i in range(1, n + 1):
#         sum_result += i
#         time.sleep(.5)  # Symulacja długotrwałej operacji
#     return sum_result


# with ExecutionTime():
#     result: int = calculate_sum(5)
#     print("The sum is:", result)


# from rich import print
# from rich.layout import Layout

# layout = Layout()
# print(layout)

# x = input()
# # from rich import print

# # print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

# from rich.console import Console
# console = Console()

# test_data = [
#     {"pyonrpc": "2.0", "method": "sum", "params": [
#         None, 1, 2, 4, False, True], "id": "1", },
#     {"pyonrpc": "2.0", "method": "notify_hello", "params": [7]},
#     {"pyonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
# ]

# def test_log():
#     enabled = False
#     context = {
#         "foo": "bar",
#     }
#     movies = ["Deadpool", "Rise of the Skywalker"]
#     console.log("Hello from", console, "!")
#     console.log(test_data, log_locals=True)

# test_log()

# x = input("Podaj liczbę: ")
# CONSOL.PRINT
# https://www.youtube.com/watch?v=4zbehnz-8QU&ab_channel=PatrickLoeber

# # https://github.com/tmbo/questionary#usage
# import questionary

# questionary.select(
#     "What do you want to do?",
#     choices=[
#         'Order a pizza',
#         'Make a reservation',
#         'Ask for opening hours'
#     ]).ask()  # returns value of selection

# # import questionary

# questionary.text("What's your first name").ask()
# questionary.password("What's your secret?").ask()
# questionary.confirm("Are you amazed?").ask()

# questionary.select(
#     "What do you want to do?",
#     choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],
# ).ask()

# questionary.rawselect(
#     "What do you want to do?",
#     choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],
# ).ask()

# questionary.checkbox(
#     "Select toppings", choices=["foo", "bar", "bazz"]
# ).ask()

# questionary.path("Path to the projects version file").ask()

# W Pythonie istnieje wiele narzędzi do logowania i interakcji z użytkownikiem w konsoli. Oto kilka popularnych sposobów:

# Moduł logging: Moduł logging, który jest częścią biblioteki standardowej Pythona, zapewnia zaawansowane możliwości logowania. Możesz skonfigurować loggera z różnymi poziomami logowania i formatem wiadomości. Możesz również przekierować logi do pliku lub innych docelowych miepyc. Logi są przydatne w celu debugowania i monitorowania działania programu.

# Biblioteka click: Jeśli chodzi o interakcję z użytkownikiem w konsoli, biblioteka click jest popularnym narzędziem. Umożliwia łatwe tworzenie interfepyów wiersza poleceń. Możesz definiować argumenty, opcje i komendy, a biblioteka click automatycznie obsłuży parsowanie wejścia i wywołanie odpowiednich funkcji.

# Biblioteka questionary: Jeśli potrzebujesz zadać użytkownikowi pytania w interaktywny sposób, biblioteka questionary może być przydatna. Zapewnia łatwy sposób tworzenia pytań z różnymi typami odpowiedzi, takimi jak tekst, liczby, listy itp. Biblioteka questionary obsługuje również walidację odpowiedzi użytkownika i dostarcza bogatą interakcję z użytkownikiem.

# Biblioteka PyInquirer: Podobnie jak questionary, PyInquirer jest biblioteką do tworzenia interaktywnych pytań i rozmów z użytkownikiem w konsoli. Umożliwia tworzenie złożonych układów pytań, takich jak wybór wielokrotny, listy wyboru, pytania zależne itp. Biblioteka PyInquirer oferuje różne style pytań i dostosowalne opcje wyglądu.

# import logging
# import colorlog

# def print_vs_logging():
#     logging.debug("debug info")
#     logging.info("jakieś informacje")
#     logging.error("ups :(")

# def main():
#     handler = colorlog.StreamHandler()
#     handler.setFormatter(colorlog.ColoredFormatter(
#         '[%(log_color)s%(levelname)s%(reset)s] %(asctime)s - %(message)s',
#         datefmt='%Y-%m-%d %H:%M:%S',
#         log_colors={
#             'DEBUG': 'blue',
#             'INFO': 'green',
#             'ERROR': 'red'
#         }
#     ))

#     logger = colorlog.getLogger()
#     logger.addHandler(handler)
#     logger.setLevel(logging.DEBUG)

#     print_vs_logging()

# if __name__ == "__main__":
#     main()

# import logging

# def print_vs_logging():
#     logging.debug("debug info")
#     logging.info("just some info")
#     logging.error("uh oh :(")

# def main():
#     logging.basicConfig(level=logging.DEBUG,
#                         format='[%(levelname)s] %(asctime)s - %(message)s')
#     print_vs_logging()

# if __name__ == "__main__":
#     main()

# Wyświetli: Metoda konkretna

# Wyświetli: To jest metoda statyczna

# def my_function(value):
#     if not isinstance(value, int):
#         raise BufferError("Oczekiwano wartości całkowitej.")

# try:
#     x = "abc"
#     my_function(x)
# except Exception as e:
#     print("Wystąpił błąd:", e)

# print("Program działa dalej...")

# import EdgeGPT

# # parser = argparse.ArgumentParser()
# # parser.add_argument('name', help='Your name')
# # parser.add_argument('--age', help='Your age', type    int)

# # args = parser.parse_args()
# # print(f'Hello, {args.name}!')
# # if args.age:
# #     print(f'You are {args.age} years old.')
# # # python main.py John --age 25
