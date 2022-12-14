import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(),0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(),1)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        mehu = Tuote("Mehu", 4)
        self.kori.lisaa_tuote(mehu)

        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(),2)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(),3)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteiden_hinnat_yhteensa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        mehu = Tuote("Mehu", 4)
        self.kori.lisaa_tuote(mehu)

        self.assertEqual(self.kori.hinta(),7)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteiden_hinnat_yhteensa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(),6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset),1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
    
        self.assertEqual((ostos.tuotteen_nimi(),ostos.lukumaara()),("Maito",1))
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        suklaa = Tuote("Suklaa", 2)
        self.kori.lisaa_tuote(suklaa)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset),2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset),1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
    
        self.assertEqual((ostos.tuotteen_nimi(),ostos.lukumaara()),("Maito",2))

    def test_kaksi_samaa_tuotetta_ja_toinen_poistetaan(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostos = self.kori.ostokset()[0]
        
        self.assertEqual((ostos.tuotteen_nimi(),ostos.lukumaara()),("Maito",1))
    
    def test_kori_tyhja_jos_tuote_poistetaan(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostos = self.kori.ostokset()[0]
    
        self.assertEqual(ostos.lukumaara(),0)
    
    def test_metodi_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.tyhjenna()

        kori = self.kori.ostokset()
        self.assertEqual(len(kori),0)