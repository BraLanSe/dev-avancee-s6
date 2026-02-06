from domain.vaches.exceptions import InvalidVacheException


class Vache:
    AGE_MAX = 25
    POIDS_MAX = 1200.0
    PANSE_MAX = 200.0
    RENDEMENT_RUMINATION = 0.25

    def __init__(self, petitNom, age, poids):
        if not petitNom or petitNom.strip() == "":
            raise InvalidVacheException("Nom invalide")

        if not (0 <= age <= self.AGE_MAX):
            raise InvalidVacheException("Âge invalide")

        if poids < 0 or poids > self.POIDS_MAX:
            raise InvalidVacheException("Poids invalide")

        self.petitNom = petitNom
        self.age = age
        self.poids = poids
        self.panse = 0.0

    # -------------------------
    # BROUTER
    # -------------------------
    def brouter(self, quantite, nourriture=None):
        if nourriture is not None:
            raise InvalidVacheException("Nourriture invalide")

        if quantite <= 0:
            raise InvalidVacheException("Quantité invalide")

        if self.panse + quantite > self.PANSE_MAX:
            raise InvalidVacheException("Panse pleine")

        self.panse += quantite

    # -------------------------
    # TEMPLATE METHOD
    # -------------------------
    def ruminer(self):
        if self.panse <= 0:
            raise InvalidVacheException("Rien à ruminer")

        panse_avant = self.panse

        gain = self.RENDEMENT_RUMINATION * panse_avant
        self.poids += gain

        lait = self._calculer_lait(panse_avant)
        self._stocker_lait(lait)

        self.panse = 0.0
        self._post_rumination()

        return lait

    # -------------------------
    # HOOKS
    # -------------------------
    def _calculer_lait(self, panse_avant):
        return 0.0

    def _stocker_lait(self, lait):
        pass

    def _post_rumination(self):
        pass

    # -------------------------
    # VIEILLIR
    # -------------------------
    def vieillir(self):
        if self.age >= self.AGE_MAX:
            raise InvalidVacheException("Âge maximum atteint")

        self.age += 1
