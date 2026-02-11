from pointplan.point_plan import PointPlan

class Point3d(PointPlan):

    def __init__(self, x=0, y=0, azimut=None):
        super().__init__(x, y)
        self.azimut = azimut

    @property
    def azimut(self):
        return self._azimut

    @classmethod
    def from_point(cls, p):
        return cls(p.abscisse, p.ordonnee, p.azimut)

    def __str__(self):
        return (
            "Point3D :\n"
            f"abscisse = {self.abscisse}, "
            f"ordonnee={self.ordonnee}"
            f"azimut={self.azimut}"
        )