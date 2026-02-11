from domain.vaches.vache_a_lait import VacheALait
from domain.vaches.exceptions import InvalidVacheException
from domain.nourriture.TypeNourriture import TypeNourriture


class PieNoire(VacheALait):

    COEFFICIENT_LAIT_PAR_NOURRITURE = {
        TypeNourriture.MARGUERITE: 1.1,
        TypeNourriture.HERBE: 1.0,
        TypeNourriture.FOIN: 0.9,
        TypeNourriture.PAILLE: 0.4,
        TypeNourriture.CEREALES: 1.3,
    }

    def __init__(self, petitNom, age, poids):
        super().__init__(petitNom=petitNom, age=age, poids=poids)
        self._ration = {}

    def brouter(self, quantite, type_nourriture=None):
        super().brouter(quantite)

        if type_nourriture is not None:
            if not isinstance(type_nourriture, TypeNourriture):
                raise InvalidVacheException("Type de nourriture invalide")

            self._ration[type_nourriture] = (
                    self._ration.get(type_nourriture, 0.0) + quantite
            )

    def _calculer_lait(self, panse_avant):
        if not self._ration:
            return super()._calculer_lait(panse_avant)

        lait = 0.0
        for nourriture, quantite in self._ration.items():
            coef = self.COEFFICIENT_LAIT_PAR_NOURRITURE[nourriture]
            lait += quantite * coef * self.RENDEMENT_LAIT

        return lait

    def _post_rumination(self):
        self._ration.clear()
