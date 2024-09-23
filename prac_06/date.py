class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02}/{self.month:02}/{self.year}"

    def add_days(self, n):
        days_in_month = [31, 28 + (1 if self.is_leap_year() else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        while n > 0:
            if self.day + n > days_in_month[self.month - 1]:
                n -= (days_in_month[self.month - 1] - self.day + 1)
                self.day = 1
                self.month += 1
                if self.month > 12:
                    self.month = 1
                    self.year += 1
            else:
                self.day += n
                n = 0

    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        return False


def main():
    date = Date(28, 2, 2020)  # Example date
    print(f"Original date: {date}")

    days_to_add = 5
    date.add_days(days_to_add)
    print(f"Date after adding {days_to_add} days: {date}")


if __name__ == "__main__":
    main()
