# 5 principles
# 1. SRP - Single Responsibility Principle
# unlike the GOD class (anti pattern) the class has a single responsibility
# example:

from typing import Set


class BankAccount:
    def __init__(self):
        self.subaccounts: Set = set()

    def add_account_number(self, num: int):
        self.subaccounts.add(str(num))

    def remove_entry(self, idx: int):
        del self.subaccounts[idx]

    def __str__(self):
        return "\n".join(self.subaccounts)


class FileSaveManager:
    # static methods dont need to be instantiated, they know nothing about the class and just deal with the parameters
    # this makes them perfect for state management / serialization
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as f:
            f.write(str(journal))


if __name__ == "__main__":
    j = BankAccount()
    j.add_account_number(123)
    j.add_account_number(987)
    print(f"Sub account entries:\n{j}")

