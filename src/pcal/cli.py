from datetime import date

import jdatetime
from rich.console import Console
from rich.table import Table
from rich.text import Text

from .calendar import (
    PERSIAN_WEEKDAYS,
    PersianCalendar,
)


console = Console()


def render_calendar(year: int, month: int) -> None:
    today = jdatetime.date.today()

    calendar = PersianCalendar(year, month)

    table = Table(
        title=f"{calendar.month_name} {year}",
        show_header=True,
        header_style="bold cyan",
        expand=True,
        padding=(0, 1),
    )

    for weekday in PERSIAN_WEEKDAYS:
        table.add_column(
            weekday,
            justify="center",
        )

    for week in calendar.weeks():
        cells = []

        for day in week:
            if day is None:
                cells.append("")
                continue

            if (
                year == today.year
                and month == today.month
                and day == today.day
            ):
                cells.append(
                    Text(f" {day} ", style="bold black on cyan")
                )
            else:
                cells.append(str(day))

        table.add_row(*cells)

    console.print()
    console.print(table)
    console.print()
