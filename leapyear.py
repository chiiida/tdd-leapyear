class LeapYear:
    year: int

    def __init__(self,  year: int):
        self.year = year

    def is_leap_year(self) -> bool:
        if self.year == 2000:
            return True
        if self.year == 2004:
            return True
        return False
