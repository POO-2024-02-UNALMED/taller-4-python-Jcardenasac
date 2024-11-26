class Asignatura:

    def _init_(self, nombre, salon="remoto"):
        self.nombre = nombre
        self.salon = salon

    def __str__(self):
        return self._nombre + " " + self._salon
