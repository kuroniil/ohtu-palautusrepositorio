import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()
        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote

    def varasto_saldo(self, tuote_id):
        if tuote_id == 1 or tuote_id == 2:
            return 10
        if tuote_id == 3:
            return 0


    def varasto_hae_tuote(self, tuote_id):
        if tuote_id == 1:
            return Tuote(1, "maito", 5)
        if tuote_id == 2:
            return Tuote(2, "piimä", 3)
        if tuote_id == 3:
            return Tuote(3, "päärynä", 9)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_tiedoilla(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_pankin_tilisiirto_metodia_kutsutaan_oikeilla_tiedoilla_kun_ostetaan_kaksi_eri_tuotetta(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("jari", "123")
        self.pankki_mock.tilisiirto.assert_called_with("jari", ANY, "123", ANY, 8)

    def test_pankin_tilisiirto_metodia_kutsutaan_oikeilla_tiedoilla_kun_ostetaan_kaksi_samaa_tuotetta(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("jarin serkku", "123876")
        self.pankki_mock.tilisiirto.assert_called_with("jarin serkku", ANY, "123876", ANY, 10)

    def test_pankin_tilisiirto_metodia_kutsutaan_oikeilla_tiedoilla_kun_ostetaan_kaksi_tuotetta_joista_toinen_on_loppu(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("jari", "123")
        self.pankki_mock.tilisiirto.assert_called_with("jari", ANY, "123", ANY, 5)

    def test_aloita_asiointi_metodi_nollaa_edellisen_ostoksen_tiedot(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("jari", "123456")

        self.pankki_mock.tilisiirto.assert_called_with("jari", ANY, "123456", ANY, 3)

    def test_kauppa_pyytää_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("jari", "123456")

        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 1)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("jarmo", "456")

        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 2)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Timo", "987456")

        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 3)

    def test_tuotteen_poistaminen_korista_onnistuu_poista_korista_metodilla(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.poista_korista(1)
        kauppa.tilimaksu("jari", "123456")
        
        self.pankki_mock.tilisiirto.assert_called_with("jari", ANY, "123456", ANY, 3)
