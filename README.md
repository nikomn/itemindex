# itemindex

Aineopintojen harjoitustyö: Tietokantasovellus

Alustava kuvaus sovelluksen toiminnallisuudesta:

Tehtävänä on luoda tietokantasovellus, jonka avulla käyttäjä voi hallinnoida hallussaan olevia esineitä. Tarkoituksena on, että käyttäjä pystyy sovelluksen avulla määrittämään jokaiselle esineelle jonkin oletetun käyttöajan, jonka jälkeen esine vanhenee, eli johon mennessä se on tullut käyttöikänsä päähän ja pitää uusia. Käyttötarkoitus on sovellettavissa monenlaisiin tarkoituksiin jääkaapin sisällön hallinnoimisesta koko omaisuuden listaamiseen asti. Idean taustalla on joskus aikoinaan minimalistien keskuudessa suosittu 100-esinettä haaste, jossa listattiin kaikki esineet, jotka omistaa ja kilpailtiin siitä, kuka pääsee lähimmäs sataa (huvinsa kullakin!).

Eli sovelluksessa on siis tarkoitus pystyä lisäämään/poistamaan ja listaamaan esineitä. Esineille määritellään kategoria (esim. core, essential, work, hobby, luxyry...) ja käyttöikä.

Sovelluksessa on kahdenlaisia käyttäjiä: admin-käyttäjät ja peruskäyttäjät.

Peruskäyttäjät voivat lisätä ja poistaa omia esineitä ja kategorioita. Esineeseen liittyy aina yksi tai useampi kategoria. Peruskäyttäjä voi myös poistaa oman käyttäjätilinsä.

Admin käyttäjillä on kaikki oikeudet, jotka peruskäyttäjälläkin, mutta he voivat myös poistaa kenen tahansa käyttäjän luomia esineitä ja kategorioita ja myös käyttäjätunnuksia.

Käyttäjätunnuksen poistaminen poistaa samalla kaikki käyttäjään liittyvät esineet ja kategoriat. Kategorian poistaminen poistaa kategorian kaikista esineistä, missä niitä on käytetty.

Tietokannasta pitää olla mahdollista hakea erilaisia listauksia esineistä, esim. kaikki esineet, tietyn kategorian esineet vanhentueet esineet yms.
