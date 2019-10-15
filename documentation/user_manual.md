# Käyttöohjeita:

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
python3 -m venv venv  
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
