import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
     def setUp(self):
        self.kortti = Maksukortti(1000)

     def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")

     def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150.00 euroa")

     def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti= Maksukortti(200)
        kortti.syo_maukkaasti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

     def test_negatiivinen_summa_ei_muuta_arvoa(self):
        self.kortti.lataa_rahaa(-10)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

     def test_osta_edullinen_lounas_tasa_rahalla(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")
 
     def test_osta_maukas_lounas_tasa_rahalla(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

