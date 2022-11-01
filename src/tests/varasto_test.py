import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-1)
        self.varasto3 = Varasto(-1, -1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_luo_negatiivisen_varaston(self):
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_negatiivisella_varastolla_negatiivinen_saldo(self):
        self.assertAlmostEqual(self.varasto2.saldo, -1)

    def test_negatiivinen_saldo_vaihtuu_nollaksi(self):
        self.assertAlmostEqual(self.varasto3.saldo, 0)

    def test_negatiivisen_maaran_lsays_estetty(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ei_voi_lisata_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_varastosta_negatiivinen_maara(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_ota_varastosta_kaikki_mita_voidaan(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(11), 0)

    def test_varasto_str(self):
        self.assertEqual(str(self.varasto), 'saldo = 0, vielä tilaa 10')