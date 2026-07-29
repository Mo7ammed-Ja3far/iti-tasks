# Fantasy Battle Game (OOP Concepts)

A simple CLI battle system written in Python to demonstrate core Object-Oriented Programming principles.

## OOP Principles Applied

- **Classes & Objects:** Created a base `Character` class and instantiated hero objects.
- **Inheritance:** `Warrior`, `Wizard`, and `Archer` inherit common attributes (`name`, `health`) and methods from `Character`.
- **Method Overriding:** Each child class overrides the base `attack()` method to implement unique damage logic and messages.
- **Polymorphism:** Iterated through a list of different character types and called `attack()` without checking their specific class type.

## How to Run

```bash
python main.py
```
