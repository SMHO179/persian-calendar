# pcal

A Persian (Jalali) calendar for your terminal. `pcal` prints a month of the
Shamsi calendar as a Rich table, starting the week on Saturday (شنبه) and
highlighting today.

## Requirements

- Python 3.10 or newer
- [rich](https://github.com/Textualize/rich) and
  [jdatetime](https://github.com/BehnamSadeghi/jdatetime) (installed automatically)

## Install

```sh
git clone git@github.com:SMHO179/persian-calendar.git
cd persian-calendar

python -m venv .venv
source .venv/bin/activate

pip install -e .
```

## Usage

Current month, highlighting today:

```sh
pcal
```

A specific month:

```sh
pcal -y 1405 -m 7
```

```
مهر 1405
┏━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┓
┃  شنبه  ┃  یکشنبه   ┃  دوشنبه   ┃  سه‌شنبه   ┃  چهارشنبه   ┃  پنجشنبه  ┃ جمعه  ┃
┡━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━┩
│        │           │           │           │      1      │     2     │   3   │
│   4    │     5     │     6     │     7     │      8      │     9     │  10   │
│   11   │    12     │    13     │    14     │     15      │    16     │  17   │
│   18   │    19     │    20     │    21     │     22      │    23     │  24   │
│   25   │    26     │    27     │    28     │     29      │    30     │       │
└────────┴───────────┴───────────┴───────────┴─────────────┴───────────┴───────┘
```

Both options are optional and default to the current Persian month and year. A
month outside 1–12 exits with an error.

### Options

| Option | Description |
| --- | --- |
| `-y`, `--year` | Persian year (defaults to the current one) |
| `-m`, `--month` | Persian month, 1–12 (defaults to the current one) |
| `-h`, `--help` | Show the help message and exit |

The module can also be run without installing the console script:

```sh
python -m pcal -m 1 -y 1405
```

## Month lengths

| Months | Days |
| --- | --- |
| فروردین – شهریور (1–6) | 31 |
| مهر – بهمن (7–11) | 30 |
| اسفند (12) | 30 in a leap year, otherwise 29 |

## Layout

```
src/pcal/
├── __init__.py
├── __main__.py   # argument parsing
├── calendar.py   # PersianCalendar: month length and week rows
└── cli.py        # Rich table rendering
```

## License

MIT — see [LICENSE](LICENSE).