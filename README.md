# itemindex

# Aineopintojen harjoitustyö: Tietokantasovellus

## Huomioita sovelluksen toiminnasta
Sovellus toimii tällä hetkellä omalle koneelle asennettuna, mutta ei herokussa. Ongelma liittyy jotenkin tällä hetkellä käyttämättömään "item_category"-liitostauluun.

Asiaa selvitellään...


## TODO 10.10. mennessä...

Tavoitteena olisi saada sovellukseen *ainakin* seuraavat toiminnallisuudet 10.10. mennessä:

- Oletuskategoria jokaiselle uudelle käyttäjälle **VALMIS**
    - Nykyisessä toteutuksessa täytyy itse luoda vähintään yksi kategoria, ennen kuin esineitä voi lisätä, mikä on hieman hankalaa.
- Kaikkien syötteiden validoinnit ja virheilmoitukset **VALMIS(?)**
- Kateorian poistaminen estetään, jos kategoriaa on käytetty jossain esineessä. **VALMIS**
- SQL kyselyitä **Valmis, mutta ei toimi ihan oikein**:
    - Listaa esineet kategorian mukaan   
    esim.

        ```
    SELECT Item.name FROM item
    LEFT JOIN Account ON Item.account_id=Account.id
    LEFT JOIN Category ON Category.account_id=Account.id
    WHERE Category.id = 3;
        ```
    - Listaa vanhentuneet esineet  
    esim.
    ```
SELECT Item.name FROM item
LEFT JOIN Account ON Item.account_id=Account.id
LEFT JOIN Category ON Category.account_id=Account.id
WHERE Item.expired = True;
    ```    
    - Listaa ei-vanhentuneet esineet
    ```
SELECT Item.name FROM item
LEFT JOIN Account ON Item.account_id=Account.id
LEFT JOIN Category ON Category.account_id=Account.id
WHERE Item.expired = False;
    ```


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

## Asennusohje

1. Lataa projekti koneellesi komennolla:
```
git clone https://github.com/nikomn/itemindex.git
```
2. Siirry projektin kansioon  
```
cd itemindex  
```
2. Luo ja aktivoi virtuaaliympäristö  
```
virtualenv venv  
source venv/bin/activate
```
3. Päivitä pip ja asenna riippuvuudet  
```
pip install --upgrade pip  
pip install -r requirements.txt
```
4. Käynnistä sovellus  
```
python3 start.py
```

Sovellus näkyy tämän jälkeen esim. Firefoxilla osoitteessa http://127.0.0.1:5000/


## Käyttöohje

### Tunnusten luominen

Käyttäjällä pitää olla tunnukset järjestelmään, ennen kuin sovellusta voi käyttää.

Käyttäjätunnusten luomiseen pääsee aloitussivulta "Luo uusi käyttäjätunnus" linkin kautta.

Käyttäjätunnusta varten tulee määrittää nimi, käyttäjätunnus ja salasana. **HUOM: Sovelluksen nykyisessä demoversiossa salasanat tallennetaan tietokantaan selkokielisinä, tämä on tiedossa ja tullaan myöhemmin muuttamaan turvallisemmaksi toteutukseksi.**

### Kirjautuminen

Sovelluksen käyttö edellyttää kirjautumista, joten käytännössä jos yrität käyttää mitä tahansa muuta kuin tunnuksen luomistoimintoa kirjautumatta, päädyt kirjautumissivulle.

Järjestelmää kirjaudutaan aikaisemmin luodulla Käyttäjätunnuksella ja salasanalla.

### Esineiden lisääminen

Esineitä voi lisätä klikkaamalla "Lisää esine"-painiketta

Esineille määritellään nimi, kategoria ja tieto siitä, onko esine vanhentunut vai ei ja lisätään se tietokantaan klikkaamalla "Lisää uusi esine" painiketta. Tämän jälkeen sovellus listaa käyttäjän kaikki esineet. **Huom: Käyttäjä näkee vain omat esineensä.**

Jos et haluakkaan lisätä esinettä, klikkaa esim. "Näytä esineet" linkkiä

### Kategorian lisääminen
Kategorioita voi lisätä klikkaamalla 'Lisää kategoria'-painiketta.

Kategorialle määritellää nimi, ja se lisätään tietokantaan klikkaamalla "Lisää kategoria" painiketta. Tämän jälkeen sovellus listaa käyttäjän kaikki kategoriat. **Huom: Käyttäjä näkee vain omat esineensä. (poislukien oletuskategorian "Ei kategoriaa")**

### Esineiden listaaminen

Voit listata esineet 'Näytä esineet' linkin kautta

Esineen voimassa-olon näkee listaus näkymästä, True tarkoittaa sitä, että esineen käyttöikä ei ole vielä päättynyt, ja False tarkoittaa sitä, että pitäsi hankkia uusi vastaava esine.

### Esineen poistaminen

Voit poistaa esineen klikkaamalla "Poista esine"-painiketta.

### Esineen tietojen muokkaaminen

Pääset muokkaamaan esineen tietoja klikkaamalla "Muokkaa"-painiketta.

### Kategorioiden listaaminen

Voit listata esineet 'Näytä kategoriat' linkin kautta

### Kategorian poistaminen
Voit poistaa kategorian klikkaamalla "Poista kategoria"-painiketta. **Huom! Jos kategoria on käytössä, sitä ei poisteta, vaan näytetään virheilmoitus. Jos haluat poistaa kategorian vaihda se pois kaikista esineistä, missä sitä on käytetty**

### Kategorian tietojen muokkaaminen

Pääset muokkaamaan kategorian tietoja klikkaamalla "Muokkaa"-painiketta.

Kategorian nimen muuttaminen näkyy kaikissa esine listauksissa, eli jos kategoriaa on käytetty esineessä, sen kohdalla näkyy jatkossa uusi kategorian nimi.

## Keskeisimmät käyttötapaukset

[Linkki keskeisimpien käyttötapausten kuvauksiin](./documentation/use_cases.md)

## Demosovellus herokussa

[https://itemindex-demo.herokuapp.com/](https://itemindex-demo.herokuapp.com/)

## Työn eteneminen...

[Loki työn etenemisestä ja aikatauluista](./documentation/progress_log.md)

## Tietokantakaavio

![Kuva tietokantataulusta](./documentation/tietokantakaavio.jpg)
