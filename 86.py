from typing import List, Dict

def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"

def average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

# Example Usage
print(add(5, 3))
print(greet("Alice"))
print(average([1.5, 2.5, 3.5]))

# Running mypy (command-line):
# Save this file as `type_hints.py`, then run: mypy type_hints.py