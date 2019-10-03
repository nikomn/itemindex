# itemindex

# Aineopintojen harjoitustyö: Tietokantasovellus

## 3.10. Päivitys
3.10. päivityksen jälkeen esineiden ja kategorioiden lisääminen toimii vihdoin (ainakin joten kuten). Pyrin kirimään viikonlopun aikana kiinni menetettyä aikaa, joka tämän ongelman ratkomisessa on valitettavasti mennyt.


## Kuvaus sovelluksen toiminnallisuudesta:

Tehtävänä on luoda tietokantasovellus, jonka avulla käyttäjä voi hallinnoida hallussaan olevia esineitä.

Tarkoituksena on, että valmis sovellus sisältää seuraavat ominaisuudet:
- Käyttäjätunnusten luominen
- Esineiden lisääminen, muokkaaminen, poistaminen
- Kategorioiden lisääminen, muokkaaminen, poistaminen
- Kategorian liittäminen esineeseen
- Esineen merkkaaminen poistettavaksi, uusittavaksi tai hankittavaksi
- Esineiden listaaminen esim. seuraavilla tavoilla:
  - Kaikki omistamani esineet
  - Tiettyyn itse määrittämääni kategoriaan tai kategorioihin kuuluvat esineet
  - Kaikki vanhentuneet esineet
  - Kaikki poistettavaksi merkatut esineet
  - Kaikki vanhentuneet esineet
  - Kaikki hankittavat esineet

Lisää kuvauksia toiminnallisuuksista löytyy myös [käyttötapauskuvauksista](./documentation/use_cases.md)

## Käyttöohje

### Tunnusten luominen

Käyttäjällä pitää olla tunnukset järjestelmään, ennen kuin sovellusta voi käyttää.

Käyttäjätunnusten luomiseen pääsee aloitussivulta "Luo uusi käyttäjätunnus" linkin kautta.

Käyttäjätunnusta varten tulee määrittää nimi, käyttäjätunnus ja salasana. **HUOM: Sovelluksen nykyisessä demoversiossa salasanat tallennetaan tietokantaan selkokielisinä, tämä on tiedossa ja tullaan myöhemmin muuttamaan turvallisemmaksi toteutukseksi.**

### Kirjautuminen

Sovelluksen käyttö edellyttää kirjautumista, joten käytännössä jos yrität käyttää mitä tahansa muuta kuin tunnuksen luomistoimintoa kirjautumatta, päädyt kirjautumissivulle.

Järjestelmää kirjaudutaan aikaisemmin luodulla Käyttäjätunnuksella ja salasanalla.

### Esineiden lisääminen

Esineitä voi lisätä klikkaamalla "Add an item"-painiketta

Esineille määritellään nimi ja lisätään se tietokantaan "Lisää uusi esine" painiketta. Tämän jälkeen sovellus listaa käyttäjän kaikki esineet. **Huom: Käyttäjä näkee vain omat esineensä.** (Tähän liittyä bugi korjattu 22.9.)

Jos et haluakkaan lisätä esinettä, klikkaa "List items" linkkiä

### Esineiden listaaminen

Voit listata esineet list items linkin kautta

Esineen voimassa-olon näkee listaus näkymästä, True tarkoittaa sitä, että esineen käyttöikä ei ole vielä päättynyt, ja False tarkoittaa sitä, että pitäsi hankkia uusi vastaava esine.

### Esineen poistaminen

Voit poistaa esineen klikkaamalla "Poista esine"-painiketta.

### Esineen tietojen muokkaaminen

Pääset muokkaamaan esineen tietoja klikkaamalla "Muokkaa"-painiketta.

## Keskeisimmät käyttötapaukset

[Linkki keskeisimpien käyttötapausten kuvauksiin](./documentation/use_cases.md)

## Demosovellus herokussa

[https://itemindex-demo.herokuapp.com/](https://itemindex-demo.herokuapp.com/)

## Työn eteneminen...

[Loki työn etenemisestä ja aikatauluista](./documentation/progress_log.md)

## Tietokantakaavio

![Kuva tietokantataulusta](./documentation/tietokantakaavio.jpg)
