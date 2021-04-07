class Volunteers:
    def __init__(self, name: str, surname: str, city: str, status: str):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status

    def getinfo(self):
        return "\033[92m {}\033[00m" .format(f"{self.name} {self.surname}, ") + \
               f"{self.city}," + \
               "\033[91m {}\033[00m" .format("status: ") + \
               "\033[21m {}\033[00m" .format(f"{self.status}")
