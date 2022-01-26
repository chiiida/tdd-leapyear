class LeapYear:
    year: int

    def __init__(self,  year: int):
        self.year = year

    def is_leap_year(self) -> bool:
        if self.year % 4 == 0:
            return True
        return False
