class Trash:
    type = ""

    def data_setter(self, p1):
        self.type = p1

    def __str__(self):
        return f"{self.type}"
