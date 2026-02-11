from domain.vaches.vache import Vache

class VacheALait(Vache):
    RENDEMENT_LAIT = 0.5

    def produire_lait(self):
        panse_avant = self.ruminer()
        lait = self._calculer_lait(panse_avant)
        self._post_rumination()
        return lait

    def _calculer_lait(self, panse_avant):
        raise NotImplementedError("A implementer dans la classe fille")
    def _post_rumination(self):
        pass
