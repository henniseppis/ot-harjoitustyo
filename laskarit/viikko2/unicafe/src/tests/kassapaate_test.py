import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
    
    def test_kassassa_rahaa_aluksi(self):
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
    
    def test_edullisia_lounaita_myyty_aluksi(self):
        self.assertEqual(str(self.kassa.edulliset), "0")
    
    def test_maukkaita_lounaita_myyty_aluksi(self):
        self.assertEqual(str(self.kassa.maukkaat), "0")
    
    def test_osta_edullinen_lounas_kateisella_tasaraha(self):
        maksu = self.kassa.syo_edullisesti_kateisella(240)

        self.assertEqual(str(self.kassa.kassassa_rahaa), "100240")
        self.assertEqual(str(self.kassa.edulliset), "1")
    
    def test_osta_edullinen_lounas_kateisella_vaihtoraha(self):
        maksu = self.kassa.syo_edullisesti_kateisella(500)

        self.assertEqual(str(self.kassa.kassassa_rahaa), "100240")
        self.assertEqual(str(self.kassa.edulliset), "1")

    
    def test_osta_edullinen_lounas_kateisella_rahat_ei_riita(self):
        maksu = self.kassa.syo_edullisesti_kateisella(200)

        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassa.edulliset), "0")
    

    def test_osta_maukas_lounas_kateisella_tasaraha(self):
        maksu = self.kassa.syo_maukkaasti_kateisella(400)

        self.assertEqual(str(self.kassa.kassassa_rahaa), "100400")
        self.assertEqual(str(self.kassa.maukkaat), "1")
    
    def test_osta_maukas_lounas_kateisella_vaihtoraha(self):
        maksu = self.kassa.syo_maukkaasti_kateisella(600)

        self.assertEqual(str(self.kassa.kassassa_rahaa), "100400")
        self.assertEqual(str(self.kassa.maukkaat), "1")
    
    def test_osta_maukas_lounas_kateisella_rahat_ei_riita(self):
        maksu = self.kassa.syo_maukkaasti_kateisella(200)

        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassa.edulliset), "0")

    
    def test_osta_edullinen_lounas_kortilla(self):
        kortti = Maksukortti(500)
        maksu = self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(str(self.kassa.edulliset), "1")
        self.assertEqual(str(kortti.saldo), "260")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
    
    def test_osta_edullinen_lounas_kortilla_rahat_ei_riita(self):
        kortti = Maksukortti(200)
        maksu = self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(str(self.kassa.edulliset), "0")
        self.assertEqual(str(kortti.saldo), "200")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
    
    def test_osta_edullinen_lounas_kortilla(self):
        kortti = Maksukortti(500)
        maksu = self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(str(self.kassa.edulliset), "1")
        self.assertEqual(str(kortti.saldo), "260")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
    
    def test_osta_edullinen_lounas_kortilla_rahat_ei_riita(self):
        kortti = Maksukortti(200)
        maksu = self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(str(self.kassa.edulliset), "0")
        self.assertEqual(str(kortti.saldo), "200")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
    
    def test_osta_maukas_lounas_kortilla(self):
        kortti = Maksukortti(500)
        maksu = self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(str(self.kassa.maukkaat), "1")
        self.assertEqual(str(kortti.saldo), "100")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")

    
    def test_osta_maukas_lounas_kortilla_rahat_ei_riita(self):
        kortti = Maksukortti(200)
        maksu = self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(str(self.kassa.maukkaat), "0")
        self.assertEqual(str(kortti.saldo), "200")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
    
    def test_lataa_rahaa_kortille(self):
        kortti = Maksukortti(500)
        maksu = self.kassa.lataa_rahaa_kortille(kortti,1000)

        self.assertEqual(str(self.kassa.kassassa_rahaa), "101000")
        self.assertEqual(str(kortti.saldo), "1500")
    
    def test_negatiivinen_summa_ei_muuta_arvoa(self):
        kortti = Maksukortti(500)
        maksu = self.kassa.lataa_rahaa_kortille(kortti,-1000)

        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(kortti.saldo), "500")









    
