from tekoaly import Tekoaly
from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self):
        self.tekoaly = Tekoaly()
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto