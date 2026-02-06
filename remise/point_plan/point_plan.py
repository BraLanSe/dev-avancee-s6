class PointPlan:
    def __init__(self, x=None, y=None):
        self._abscisse = x
        self._ordonnee = y

    @classmethod
    def from_point(cls, p):
        return cls(p.abscisse, p.ordonnee)

    @property
    def abscisse(self):
        return self._abscisse

    @abscisse.setter
    def abscisse(self, value):
        self._abscisse = value

    @property
    def ordonnee(self):
        return self._ordonnee

    @ordonnee.setter
    def ordonnee(self, value):
        self._ordonnee = value

    def __str__(self):
        return f"\nabscisse = {self._abscisse}, ordonnee={self._ordonnee}"
