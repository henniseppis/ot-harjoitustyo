# Arkkitehtuuri määritelmä

### Pakkausrakenne


![](./kuvat/pakkaus.png)


UI sisältää käyttöliittymän. 4 eri tiedostoa, jotka kuvaavat eri ikkunoita sovelluksessa. Suurin osa toiminnallisuudesta myös täällä. Services sisältää muutaman toiminnallisuuden.

### Käyttöliittymä

  - Kirjautuminen
      - Sisältää mahdollisuuden sisään kirjautumiseen
  - Valikko (create,view,delete all)
      - Sisältää mahdollisuuden säästökohteiden luomiseen, tarkasteluun sekä niiden poistamiseen
  - Säästökohteiden luominen
      - Käyttäjältä kysytään 3 kysymystä, joiden perusteella luodaan säästökohde sekä lasketaan sen saavuttamiseen kuluva aika
  - Säästökohteiden tarkastelu
      - Täällä pystyy tarkastella omia säästökohteita

Kaikki ovat omissa tiedostoissaan ja näin ollen myös omissa luokissa. Jokaisen näkymän tiedosto sisältää myös suurimman osan sen tominnasta. Tarkoitus oli täysin erottaa sovelluslogiikka sekä käyttöliittymä, mutta en siinä onnistunut. Mielestäni kuitenkin sain ihan selkeän kokonaisuuden rakennettua näinkin.

Valikko ja säästökohteiden luominen tai valikko ja sääsötkohteiden tarkastelu voivat olla yhtä aikaa auki. Näin ollen on helpompi palata valikkoon säästökohteiden luonnin/tarkastelun jälkeen. 



