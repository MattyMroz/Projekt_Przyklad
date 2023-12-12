import time


def current_datetime_with_nanoseconds():
    current_time_ns = time.time_ns()
    seconds = current_time_ns // 1000000000
    nanoseconds = current_time_ns % 1000000000

    current_date = time.localtime(seconds)
    current_time = time.strftime('%H:%M:%S', current_date)
    milliseconds = nanoseconds // 1000000
    microseconds = (nanoseconds % 1000000) // 1000

    return f"{current_date.tm_year}-{current_date.tm_mon:02d}-{current_date.tm_mday:02d} {current_time} :{milliseconds:03d}:{microseconds:03d}:{nanoseconds % 1000:03d}"


current_datetime = current_datetime_with_nanoseconds()
print('YYYY-MM-DD HH:MM:SS :ms :µs :ns')
print(current_datetime)




# print(Timer.__doc__)


# Powyższa dokumentacja opisuje klasę `Timer`, która jest menedżerem kontekstu do pomiaru czasu wykonania bloku kodu. Opisuje również funkcję `calculate_sum()`, która oblicza sumę liczb od 1 do `n`, oraz funkcję `main()`, która wykonuje blok kodu z użyciem menedżera kontekstu `Timer()`.


# from datetime import datetime
# from time import perf_counter_ns, sleep
# from dataclasses import dataclass


# @dataclass(init=True)
# class Timer:
#     start_date: datetime = None
#     end_date: datetime = None
#     start_time_ns: int = None
#     end_time_ns: int = None

#     def __post_init__(self):
#         self.start_date = datetime.now()
#         self.start_time_ns = perf_counter_ns()

#     def __enter__(self) -> 'Timer':
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         try:
#             self.end_date = datetime.now()
#             self.end_time_ns = perf_counter_ns()
#             self.display_time()
#         except Exception as e:
#             print(f'An error occurred: {e}')

#     def current_datetime(self, date: datetime) -> str:
#         return f'{date.year}-{date.month:02d}-{date.day:02d} {date.hour:02d}:{date.minute:02d}:{date.second:02d}'

#     def calculate_duration(self) -> tuple[int]:
#         duration_ns = self.end_time_ns - self.start_time_ns
#         duration_s, duration_ns = divmod(duration_ns, 1_000_000_000)
#         duration_ms, duration_ns = divmod(duration_ns, 1_000_000)
#         duration_us, duration_ns = divmod(duration_ns, 1_000)

#         hours, remainder = divmod(duration_s, 3600)
#         minutes, seconds = divmod(remainder, 60)

#         return hours, minutes, seconds, duration_ms, duration_us, duration_ns

#     def calculate_duration_alt(self) -> tuple[float, float, float]:
#         duration_ns = self.end_time_ns - self.start_time_ns
#         hours_alt = duration_ns / 1_000_000_000 / 3600
#         minutes_alt = duration_ns / 1_000_000_000 / 60
#         seconds_alt = duration_ns / 1_000_000_000

#         return hours_alt, minutes_alt, seconds_alt

#     def display_time(self):
#         start_date_str = self.current_datetime(self.start_date)
#         end_date_str = self.current_datetime(self.end_date)
#         hours, minutes, seconds, duration_ms, duration_us, duration_ns = self.calculate_duration()
#         hours_alt, minutes_alt, seconds_alt = self.calculate_duration_alt()

#         print('        YYYY-MM-DD HH:MM:SS:ms :µs :ns')
#         print(f'[START] {start_date_str}')
#         print(f'[END]   {end_date_str}')
#         print(
#             f'[TIME]  YYYY-MM-DD {hours:02d}:{minutes:02d}:{seconds:02d}:{duration_ms:03d}:{duration_us:03d}:{duration_ns:03d}')
#         print()

#         print(f'[TIME]  {hours_alt:.10f} hours')
#         print(f'[TIME]  {minutes_alt:.10f} minutes')
#         print(f'[TIME]  {seconds_alt} seconds')


# def calculate_sum(n: int) -> int:
#     sum_result = 0
#     for i in range(1, n + 1):
#         sum_result += i
#         sleep(.5)  # Symulacja długotrwałej operacji
#     return sum_result


# # with Timer():
# #     for i in range(1000):
# #         print(i)


# def main():
#     sum_result = calculate_sum(1)
#     print(f'Sum of 1..1000 = {sum_result}')


# with Timer():
#     main()


# from datetime import datetime
# from time import perf_counter_ns, sleep
# from dataclasses import dataclass


# @dataclass(init=True)
# class ExecutionTime:
#     start_date: datetime = None
#     end_date: datetime = None
#     start_time: int = None
#     end_time: int = None

#     def __post_init__(self):
#         self.start_date: datetime = datetime.now()
#         self.start_time: int = perf_counter_ns()

#     def __enter__(self) -> 'ExecutionTime':
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.end_date: datetime = datetime.now()
#         self.end_time: int = perf_counter_ns()
#         self.display_time()

#     def current_datetime_with_nanoseconds(self, start_end_date, start_end_time: int) -> str:
#         current_date: datetime = start_end_date
#         current_time: str = current_date.strftime('%H:%M:%S')
#         milliseconds: str = current_date.strftime('%f')[:3]
#         microseconds: str = current_date.strftime('%f')[3:6]
#         nanoseconds: int = start_end_time % 1000

#         return f'{current_date.year}-{current_date.month:02d}-{current_date.day:02d} {current_time}:{milliseconds}:{microseconds}:{nanoseconds:03d}'

#     def calculate_duration(self) -> tuple[int]:
#         duration_ns: int = self.end_time - self.start_time
#         duration_s, duration_ns = divmod(duration_ns, 1_000_000_000)
#         duration_ms, duration_ns = divmod(duration_ns, 1_000_000)
#         duration_us, duration_ns = divmod(duration_ns, 1_000)

#         hours, remainder = divmod(duration_s, 3600)
#         minutes, seconds = divmod(remainder, 60)

#         return hours, minutes, seconds, duration_ms, duration_us, duration_ns

#     def calculate_duration_alt(self) -> tuple[float, float, float]:
#         duration_ns: int = self.end_time - self.start_time
#         hours_alt: float = duration_ns / 1_000_000_000 / 3600
#         minutes_alt: float = duration_ns / 1_000_000_000 / 60
#         seconds_alt: float = duration_ns / 1_000_000_000

#         return hours_alt, minutes_alt, seconds_alt

#     def display_time(self):
#         start_date: str = self.current_datetime_with_nanoseconds(
#             self.start_date, self.start_time)
#         end_date: str = self.current_datetime_with_nanoseconds(
#             self.end_date, self.end_time)
#         hours, minutes, seconds, duration_ms, duration_us, duration_ns = self.calculate_duration()
#         hours_alt, minutes_alt, seconds_alt = self.calculate_duration_alt()

#         print('        YYYY-MM-DD HH:MM:SS:ms :µs :ns')
#         print(f'[START] {start_date}')
#         print(f'[END]   {end_date}')
#         print(
#             f'[TIME]  YYYY-MM-DD {hours:02d}:{minutes:02d}:{seconds:02d}:{duration_ms:03d}:{duration_us:03d}:{duration_ns:03d}')
#         print()

#         print(f'[TIME]  {hours_alt} hours')
#         print(f'[TIME]  {minutes_alt} minutes')
#         print(f'[TIME]  {seconds_alt} seconds')


# def calculate_sum(n: int) -> int:
#     sum_result: int = 0
#     for i in range(1, n + 1):
#         sum_result += i
#         sleep(.5)  # Symulacja długotrwałej operacji
#     return sum_result


# with ExecutionTime() as ex_time:
#     result: int = calculate_sum(10)
#     print('The sum is:', result)
