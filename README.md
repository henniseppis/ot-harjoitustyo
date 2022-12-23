# I WANT IT I GOT IT...BUT WHEN

## Sovellukseni "I want it, I got it... but when" on rahan säästämiseen kannustava sovellus.

## Linkit

[Käyttöohje](https://github.com/henniseppis/ot-harjoitustyo/blob/master/app/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/henniseppis/ot-harjoitustyo/blob/master/app/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/henniseppis/ot-harjoitustyo/blob/master/app/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/henniseppis/ot-harjoitustyo/blob/master/app/dokumentaatio/changelog.md)

[Testidokumentti](https://github.com/henniseppis/I-want-it-I-got-it...But-when/blob/master/app/dokumentaatio/testaus.md)

[Arkkitehtuurikuvaus](https://github.com/henniseppis/I-want-it-I-got-it...But-when/blob/master/app/dokumentaatio/arkkitehtuurim%C3%A4%C3%A4ritelm%C3%A4.md)

## Ohjelman käynnistys

Lataa ensiksi sovellus täältä:

[Release](https://github.com/henniseppis/I-want-it-I-got-it...But-when/releases/tag/FinalReleaese)

---

- **!TÄRKEÄ!** kun olet ladannut sovelluksen koneelle avaa kansio terminaalissa ja mene kansioon "app" komennolla:

    - cd app
    
     TAI vaihtoehtoisesti:  
     manuaalisesti ladatun tiedoston kansiossa app kansioon ja vasta sen jälkeen avaa se terminaaliin 
    
Kuitenkin tarkista ennen etenemistä, että seuraavat asiat tapahtuvat app- kansiossa 


- Asennetaan riippuvuudet:  
    - poetry install
 
- **!TÄRKEÄ!** Luodaan targets.csv - tiedosto app- kansioon komennolla:
 
    - touch targets.csv
 
- Jonka jälkeen käynnistys komennolla:  
    - poetry run invoke start
    
### Käyttäjätunnukset
- Katso käyttöohje

### Käskyt

Käynnistys 
 - Poetry run invoke start
 
 Testaus 
 - Poetry run invoke test

Coverage report
 - Poetry run invoke coverage-report
