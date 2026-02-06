from domain.vaches.exceptions import InvalidVacheException
class Vache:
    AGE_MAX=25
    POID_MAX=1200.0
    PANSE_MAX=200.0
    RENDEMENT_RUMINATION=0.25

    def __init__(self, petitNom, age, poids):
        if not petitNom or petitNom.strip()=="":
            raise InvalidVacheException("Nom invalide")
        if not (0<= age <= self.AGE_MAX):
            raise InvalidVacheException("Âge invalide")
        if poids<0 or poids>self.POID_MAX:
            raise InvalidVacheException("Poids invalide")

        self.petitNom= petitNom
        self.age= age
        self.poids= poids
        self.panse= 0.0

    def brouter(self, quantite):
        if quantite <=0:
            raise InvalidVacheException("Quantite invalide")
        if self.panse + quantite > self.PANSE_MAX:
            raise InvalidVacheException("Panse invalide")
        self.panse += quantite

    def ruminer(self):


