class PointPlan:
    def __init__(self, x=0.0, y=0.0):
        self._abscisse= float(x)
        self._ordonnee= float(y)

    @classmethod
    def from_point(cls, p):
        return cls(p.abscisse, p.ordonnee)

    @property
    def abscisse(self):
        return self._abscisse

    @property
    def ordonnee(self):
        return self, abscisse

    def __str__(self):
        return f"\nabscisse = {self._abscisse} ordonnee = {self._ordonnee}"

