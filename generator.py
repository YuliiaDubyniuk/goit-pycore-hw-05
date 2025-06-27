from typing import Callable, Generator
import re


def generator_numbers(text: str) -> Generator[float, None, None]:
    """Find all real numbers and give one at the time"""
    pattern = r"[+-]?(?:\d*\.\d+|\d+)"
    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """Calculate sum of the numbers found in the text"""
    total = 0.0
    for number in func(text):
        total += number

    return total


text = "Total income of the employee consists of few parts: $1000.01 as main income, and additional revenue $27.45 and #324.00."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
