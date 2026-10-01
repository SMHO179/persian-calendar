import calendar
from dataclasses import dataclass

import jdatetime


PERSIAN_MONTHS = [
    "فروردین",
    "اردیبهشت",
    "خرداد",
    "تیر",
    "مرداد",
    "شهریور",
    "مهر",
    "آبان",
    "آذر",
    "دی",
    "بهمن",
    "اسفند",
]

PERSIAN_WEEKDAYS = [
    "شنبه",
    "یکشنبه",
    "دوشنبه",
    "سه‌شنبه",
    "چهارشنبه",
    "پنجشنبه",
    "جمعه",
]


@dataclass
class PersianCalendar:
    year: int
    month: int

    @property
    def month_name(self) -> str:
        return PERSIAN_MONTHS[self.month - 1]

    @property
    def days_in_month(self) -> int:
        if self.month <= 6:
            return 31

        if self.month <= 11:
            return 30

        return 30 if jdatetime.j_isleap(self.year) else 29

    def weeks(self):
        """
        Return calendar weeks.

        Python's calendar starts on Monday.
        We rotate it so Saturday becomes the first day.
        """
        first_day = jdatetime.date(self.year, self.month, 1).togregorian()

        # Monday = 0 ... Sunday = 6
        first_weekday = first_day.weekday()

        # Convert to Saturday = 0 ... Friday = 6
        first_weekday = (first_weekday + 2) % 7

        days = list(range(1, self.days_in_month + 1))

        week = [None] * first_weekday

        for day in days:
            week.append(day)

            if len(week) == 7:
                yield week
                week = []

        if week:
            week.extend([None] * (7 - len(week)))
            yield week
