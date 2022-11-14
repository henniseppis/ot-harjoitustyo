# **VAATIMUSMÄÄRITTELY OHTE-HARJOITUSTYÖ**

## Sovelluksen idea  
Sovellukseni "I want it, I got it... but when" on rahan säästämiseen kannustava sovellus. 

## Käyttäjät
Käyttäjä laatua on vain yksi eli peruskäyttäjä

## Sovelluksen tarjoamat toiminnot ja toiminta pähkinänkuoressa

  - Uusi käyttäjä luo tunnuksen, ja kirjautuu sisään.  
  - Käyttäjä lisää yhden tai useamman kohteen johon haluaa säästää rahaa sekä kuinka paljon tämä esine/asia kustantaa ( Esim. Lumilauta 500e)  
  - Käyttäjä määrittelee X-summan, jonka on valmis pistämään sivuun joka kuukausi kyseistä asiaa varten. Summaa voi halutessaan muokata
  - Sovellus laskee kuinka monta kuukautta käyttäjällä kuluu, jotta saa ostettua haluamansa asian  
  - Jos säästökohteita on monia lasketaan yksilölliset summat per asia. Esim. "Lumilauta 500e säästöön 25e/kk " , "Sohva 1000e säästöön 150e/kk"

## Sovelluksen eri näkymät
  ##### Kirjautumis-näkymä 
  - Kysytään käyttäjänimi + salasana sekä tässä kohtaa on mahdollisuus tilin luomiseen
   - Jos pitää luoda uusi käyttäjätili niin luodaan yksilöllinen käyttäjänimi sekä salasana.
  ##### Säästötavoitteet- näkymä (Main page)
  - Kirjautumisen jälken avautuu sivu, jossa näkyy kaikki jo määritellyt säästötavoitteet (toki jos on juuri luonut käyttäjän niitä on luonnollisesti vielä tässä vaiheessa 0) sekä voi luoda uuden säästökohteen
  - Ajatuksena, että tällä sivulla näkyisi riveittäin " Kohteen nimi, summa, kuukausisäästötavoite, kuukausien määrä targettiin puolikkaiden kuukausien tarkkuudella"
  -Esim. "Lumilauta     500e     50e     10kk"
  ##### Luo säästökohde- näkymä
  - Uuden säästökohteen luonnissa kysytään (ainakin) seuraavia asioita
      - Säästökohteen nimi
      - Säästökohteen hinta
      - Kuukasittainen säästöön pistettävä summa kyseiselle asialle

## Jatkokehitysideoita

  - Käyttäjä pystyisi laittamaan myös deadlineja. Esim "Italian reissu kesäkuussa" ja määritellä kuinka paljon siihen mennessä pitää olla säästettynä. Sovellus laskee sitten summan, joka on laitettava sivuun joka kuukausi, jotta päästään tavoitteeseen
  - Perhejako/Ystäväjako eli voidaan laittaa yhteisiä tavotteita sekä määritellä kuinka paljon kukakin on valmis laittamaan sivuun tai jakaa koko summan osallistujien kesken
  - Sovellukseen voisi merkata omat kuukausitulot sekä kuukaisttaiset pakolliset menot jolloin omien menojen seuranta sekä sivuun laitettavan summan määritteleminen helpottuu
  - Mahdollisuus siihen, että kuukausittainen summa menisi sovelluksen kautta automaattisesti säästötilille eikä käyttäjä joutuisi sitä itse tekemään


