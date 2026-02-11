from domain.vaches.vache import Vache
from domain.vaches.exceptions import InvalidVacheException

class VacheALait(Vache):
    PANSE_MAX = 50.0
    PRODUCTION_LAIT_MAX = 50.0
    RENDEMENT_LAIT=1.1

    def __init__(self, petitNom, age, poids):
        super().__init__(petitNom, poids, age)
        self.panse=0.0
        self.lait_disponible=0.0
        self.lait_total_produit=0.0
        self.lait_total_traite=0.0

    def _calculer_lait(self, panse_avant):
        return self.RENDEMENT_LAIT * panse_avant

    def stocker_lait(self, lait):
        self.lait_disponible +=lait
        self.lait_total_produit +=lait

    def traire(self, litres):
        if litres <= 0 or litres > self.lait_disponible:
            raise InvalidVacheException("Traite invalide")
        self.lait_disponible -= litres
        self.lait_total_traite +=litres
        return litres


