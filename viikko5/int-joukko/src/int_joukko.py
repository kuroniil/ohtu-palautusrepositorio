KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.ljono:
            return True
        return False
        
        
    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                nykyinen_joukko = self.ljono
                self.kopioi_lista(self.ljono, nykyinen_joukko)
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(nykyinen_joukko, self.ljono)

            return True

        return False

    def poista(self, n):
        indeksi = -1

        if n in self.ljono:
            indeksi = self.ljono.index(n)
            self.ljono[indeksi] = 0

        if indeksi != -1:
            for i in range(indeksi, self.alkioiden_lkm - 1):
                self.ljono[i] = self.ljono[i + 1]

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        joukko = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(joukko)):
            joukko[i] = self.ljono[i]

        return joukko

    @staticmethod
    def yhdiste(a, b):
        yhdistejoukko = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for i in range(0, len(a_joukko)):
            yhdistejoukko.lisaa(a_joukko[i])

        for i in range(0, len(b_joukko)):
            yhdistejoukko.lisaa(b_joukko[i])

        return yhdistejoukko

    @staticmethod
    def leikkaus(a, b):
        leikkausjoukko = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for i in range(len(a_joukko)):
            if a_joukko[i] in b_joukko:
                leikkausjoukko.lisaa(a_joukko[i])

        return leikkausjoukko

    @staticmethod
    def erotus(a, b):
        erotusjoukko = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for i in range(0, len(a_joukko)):
            erotusjoukko.lisaa(a_joukko[i])

        for i in range(0, len(b_joukko)):
            erotusjoukko.poista(b_joukko[i])

        return erotusjoukko

    def __str__(self):
        lista_mjono = "{"
        for i in range(0, self.alkioiden_lkm - 1):
            lista_mjono += str(self.ljono[i]) + ", "
        
        if self.alkioiden_lkm != 0:
            lista_mjono += str(self.ljono[self.alkioiden_lkm - 1])

        return lista_mjono + "}"
