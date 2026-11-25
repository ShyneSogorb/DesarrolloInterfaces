

class User:
    def __init__(self, id, name, number, mail):
        self._id = id
        self._name = name
        self._number = number
        self._mail = mail

    def validateId(id):
        return True

    def validateName(name):
        return True

    def validateNumber(number):
        return True

    def validateMail(mail):
        return True

    def __str__(self):
        comps = self.__dict__.values()
        return " - ".join(str(c) for c in comps)