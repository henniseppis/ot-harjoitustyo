import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_lataa_rahaa(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        kortti = Maksukortti(200)
        kortti.ota_rahaa(250)

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
    
    def test_saldo_vahenee_oikein_kun_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(250)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.50 euroa")


    
