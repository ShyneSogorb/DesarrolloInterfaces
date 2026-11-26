import re


class User:
    def __init__(self, id, name, number, mail):
        self._id = id
        self._name = name
        self._number = number
        self._mail = mail

    def validateId(id):
        return True

    def validateName(name: str):
        return bool(re.match(r"^[a-zA-Záéíóú\s]+$", name))

    def validateNumber(number: str):
        return bool(re.match(r"^\d{9}$", number.replace(" ", "")))

    def validateMail(mail: str):
        return bool(re.match(r"^[\w\d]+@[\w\d]+\.[\w\d]+$", mail))

    def __str__(self):
        comps = self.__dict__.values()
        return " - ".join(str(c) for c in comps)

    def format(self):
        comps = self.__dict__.items()
        
        return "\n".join(f"{k[1:].capitalize()} - {v}" for k, v in comps)