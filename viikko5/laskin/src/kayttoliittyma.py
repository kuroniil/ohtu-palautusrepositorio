from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote

    def suorita(self):
        self._arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.plus(int(self._syote()))

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._arvo)
        

class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote

    def suorita(self):
        self._arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.miinus(int(self._syote()))
    
    def kumoa(self):    
        self._sovelluslogiikka.aseta_arvo(self._arvo)
    

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self._sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, summa_olio, erotus_olio):
        self._sovelluslogiikka = sovelluslogiikka
        self.summa_olio = summa_olio
        self.erotus_olio = erotus_olio

    def suorita(self):
        if self._sovelluslogiikka.edellinen_toiminto == "plus":
            self.summa_olio.kumoa()
        elif self._sovelluslogiikka.edellinen_toiminto == "miinus":
            self.erotus_olio.kumoa()

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka),
        }
        self._kumoa = Kumoa(sovelluslogiikka, self._komennot[Komento.SUMMA], self._komennot[Komento.EROTUS])


    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)
   
    def _lue_syote(self):
        luku = self._syote_kentta.get()
        if luku == "":
            luku = 0
        return luku

    def _suorita_komento(self, komento):
        if komento == Komento.KUMOA:
            self._kumoa.suorita()
        else:
            komento_olio = self._komennot[komento]
            komento_olio.suorita()

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())
