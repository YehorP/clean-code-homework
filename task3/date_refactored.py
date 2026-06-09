from abc import ABC
from typing import Tuple

class DateHelper(ABC):
    MIN_YEAR = 1970

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def is_long_month(month: int) -> bool:
        return month in [1, 3, 5, 7, 8, 10, 12]

    @staticmethod
    def max_day_of_month(month: int, year: int) -> int:
        if month == 2:
            return 29 if DateHelper.is_leap_year(year) else 28
        return 31 if DateHelper.is_long_month(month) else 30

    @staticmethod
    def total_days_by_year(year: int) -> int:
        return 366 if DateHelper.is_leap_year(year) else 365

    @staticmethod
    def normalize_day(day, year) -> int:
        total_days = DateHelper.total_days_by_year(year)
        if day < 1:
            return 1
        elif day > total_days:
            return total_days
        return day

    @staticmethod
    def normalize(year, day) -> Tuple[int, int, bool]:
        normalized_year = DateHelper.normalize_year(year)
        normalized_day = DateHelper.normalize_day(day, year)
        return normalized_year, normalized_day, normalized_day != day or normalized_day != year

    @staticmethod
    def normalize_year(year: int) -> int:
        return DateHelper.MIN_YEAR if year < DateHelper.MIN_YEAR else year


class DateRefactored:
    mth : int
    year : int
    day : int

    def __init__(self, year: int, day: int) -> None:
        (self.year, self.day, self.normalized) = DateHelper.normalize(year, day)
        self.recalculate_date()

    @staticmethod
    def create(year: int, month: int) -> "DateRefactored":
        return DateRefactored(year, month)

    def __eq__(self, other) -> bool:
        return self.year == other.year and self.day == other.day

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        return self.year < other.year or ( self.year == other.year and  self.day < other.day )

    def __str__(self) -> str:
        return f"{self.year}-{self.mth:02d}"

    def recalculate_date(self) -> None:
        for mth in range(1, 13):
            days = DateHelper.max_day_of_month(mth, self.year)
            if self.day <= days:
                self.mth = mth
                return
            self.day -= days

    def to_tuple(self) -> Tuple[int, int, int]:
        return self.year, self.mth, self.day
