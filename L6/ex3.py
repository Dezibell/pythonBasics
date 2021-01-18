class Worker:
    name = ''
    surname = ''
    position = ''
    _income = dict()

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus,
        }


class Position(Worker):
    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def get_total_income(self) -> int:
        return self._income["wage"] + self._income["bonus"]


pos = Position("Иван", "Васильевич", "просто хороший человек", 60000, 5000)
print(pos.get_full_name())
print(pos.get_total_income())
