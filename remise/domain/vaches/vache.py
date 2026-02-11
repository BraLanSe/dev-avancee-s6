from domain.vaches.exceptions import InvalidVacheException


class Vache:
    def __init__(self, petitNom: str, age: int, poids: float):
        self.petitNom = petitNom
        self.age = age
        self.poids = poids
        self.panse = 0.0

    @property
    def petitNom(self):
        return self._petitNom

    def brouter(self, quantite: float):
        if quantite <=0:
            raise ValueError("Qauntité invalide")
        self._panse += quantite

    def ruminer(self):
        panse_avant = self._panse
        self._panse = 0
        return panse_avant
