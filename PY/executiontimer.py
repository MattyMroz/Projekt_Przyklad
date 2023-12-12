"""
Module executiontimer provides a ExecutionTimer class to measure the execution time of a code block.
"""

from datetime import datetime
from time import perf_counter_ns, sleep
from dataclasses import dataclass


@dataclass(slots=True)
class ExecutionTimer:
    """
    Timer is a context manager that measures the execution time of a code block.
    It captures the start time, end time, and duration of the code block.
    """

    start_date: datetime = None
    end_date: datetime = None
    start_time_ns: int = None
    end_time_ns: int = None

    def __post_init__(self):
        self.start_date = datetime.now()
        self.start_time_ns = perf_counter_ns()

    def __enter__(self) -> 'ExecutionTimer':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.end_date = datetime.now()
            self.end_time_ns = perf_counter_ns()
            self.display_time()
        except AttributeError:
            print('An error occurred: __exit__')

    def current_datetime(self, date: datetime) -> str:
        """
        Formats a datetime object as a string in the format 'YYYY-MM-DD HH:MM:SS'.
        """

        return f'{date.year}-{date.month:02d}-{date.day:02d}' \
            f' {date.hour:02d}:{date.minute:02d}:{date.second:02d}'

    def calculate_duration(self) -> str:
        """
        Calculates the duration of the code block in hours, minutes, seconds, milliseconds,
        microseconds, and nanoseconds.
        """

        duration_ns: int = self.end_time_ns - self.start_time_ns
        duration_s, duration_ns = map(int, divmod(duration_ns, 1_000_000_000))
        duration_ms, duration_ns = map(int, divmod(duration_ns, 1_000_000))
        duration_us, duration_ns = map(int, divmod(duration_ns, 1_000))

        hours, remainder = map(int, divmod(duration_s, 3600))
        minutes, seconds = map(int, divmod(remainder, 60))

        return f'{hours:02d}:{minutes:02d}:{seconds:02d}:' \
            f'{duration_ms:03d}:{duration_us:03d}:{duration_ns:03d}'

    def calculate_duration_alt(self) -> tuple[float, ...]:
        """
        Calculates the duration of the code block in hours, minutes, and seconds
        using an alternative method.
        """

        duration_ns: int = self.end_time_ns - self.start_time_ns
        hours_alt: float = duration_ns / 1_000_000_000 / 60 / 60
        minutes_alt: float = duration_ns / 1_000_000_000 / 60
        seconds_alt: float = duration_ns / 1_000_000_000

        return hours_alt, minutes_alt, seconds_alt

    def display_time(self):
        """
        Displays the start date, end date, and duration of the code block execution.
        """

        start_date_str: str = self.current_datetime(self.start_date)
        end_date_str: str = self.current_datetime(self.end_date)
        duration: str = self.calculate_duration()
        hours_alt, minutes_alt, seconds_alt = map(
            float, self.calculate_duration_alt())

        print('        YYYY-MM-DD HH:MM:SS:ms :µs :ns')
        print(f'[START] {start_date_str}')
        print(f'[END]   {end_date_str}')
        print(f'[TIME]  YYYY-MM-DD {duration}')
        print(f'[TIME]  {hours_alt:.10f} hours')
        print(f'[TIME]  {minutes_alt:.10f} minutes')
        print(f'[TIME]  {seconds_alt} seconds')


def calculate_sum(upper_limit: int) -> int:
    """
    Calculates the sum of integers from 1 to n.
    """

    sum_result = 0
    for i in range(1, upper_limit + 1):
        sum_result += i
        sleep(.5)  # Simulating a time-consuming operation
    return sum_result


def main():
    """
    Main function to execute the code block with the Timer context manager.
    """

    sum_result = calculate_sum(1)
    print(f'Sum of 1..1000 = {sum_result}')


if __name__ == '__main__':
    with ExecutionTimer():
        main()
