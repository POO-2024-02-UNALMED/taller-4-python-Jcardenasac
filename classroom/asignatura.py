class Asignatura:

    def _init_(self, nombre, salon="remoto"):
        self.nombre = nombre
        self.salon = salon

    def _str_(self):
        return f"{self.nombre} {self.salon}"
