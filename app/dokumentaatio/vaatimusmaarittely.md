# **VAATIMUSMÄÄRITTELY**

## Sovelluksen idea  
Sovellukseni "I want it, I got it... but when" on rahan säästämiseen kannustava sovellus. 

## Käyttäjät
Tulevaisuudessa käyttäjiä monia. Tällä hetkellä vain yhdet toimivat tunnukset.

## Sovelluksen tarjoamat toiminnot ja toiminta pähkinänkuoressa

  - Yksi ainoa käyttäjä kirjautuu sisään.  
  - Käyttäjä lisää yhden tai useamman kohteen johon haluaa säästää rahaa sekä kuinka paljon tämä esine/asia kustantaa ( Esim. Lumilauta 500e)  
  - Käyttäjä määrittelee X-summan, jonka on valmis pistämään sivuun joka kuukausi kyseistä asiaa varten. Summaa voi halutessaan muokata
  - Sovellus laskee kuinka monta kuukautta käyttäjällä kuluu, jotta saa ostettua haluamansa asian (yläkanttiin)

## Sovelluksen eri näkymät
  ##### Kirjautumis-näkymä 
  - Kysytään käyttäjänimi + salasana, jotka kerrottu käyttöohjeessa
  ##### Valikko-näkymä
  - Kirjautumisen jälken avautuu sivu, jossa on kolme nappia
      - *Create*
          - Nappia painamalla avautuu ikkuna johon syötetään säästökohde, sen hinta sekä summa jonka on valmis säästämään joka kuukausi
      - *View*
          - Täällä voi tarkastella säästökohteita. Tällä sivulla myös lukee monta kuukautta/vuotta, jotta kyseinen asia saadaan ostettua. Myös siihen säästetty summa näkyy. Jos painaa tätä eikä yhtäkään säästökohdetta ole vielä lisätty niin sivulla näkyy nappi, josta pääsee myös luomaan semmoisen. Kun säästökohteen saamiseen on 0kk niin se häviää VIEW näkymästä
      - *Delete All*
          - Tätä painamalla poistuu kaikki säästökohteet tiedostosta
       

## Jatkokehitysideoita
----- Sovelluksen luomisen jälkeen
  - En ehtinyt tehdä SQL tietokantaa, jotta käyttäjiä voisi olla monia ja niitä voisi luoda, joten se siirtyy tänne kehitysideoihin
  - Yksittäisiä säästökohteita voisi poistaa


----- Alla olevat kehitysideat luotu ennen aloittamista (vieläkin hyviä)
  - Käyttäjä pystyisi laittamaan myös deadlineja. Esim "Italian reissu kesäkuussa" ja määritellä kuinka paljon siihen mennessä pitää olla säästettynä. Sovellus laskee sitten summan, joka on laitettava sivuun joka kuukausi, jotta päästään tavoitteeseen
  - Perhejako/Ystäväjako eli voidaan laittaa yhteisiä tavotteita sekä määritellä kuinka paljon kukakin on valmis laittamaan sivuun tai jakaa koko summan osallistujien kesken
  - Sovellukseen voisi merkata omat kuukausitulot sekä kuukaisttaiset pakolliset menot jolloin omien menojen seuranta sekä sivuun laitettavan summan määritteleminen helpottuu
  - Mahdollisuus siihen, että kuukausittainen summa menisi sovelluksen kautta automaattisesti säästötilille eikä käyttäjä joutuisi sitä itse tekemään


