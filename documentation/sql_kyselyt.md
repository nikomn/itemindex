# Tietokannan luomiseen käytetyt lauseet SQlite-tietokannassa

Käyttäjät:

```SQL
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
);
```

Kategoriat:


```SQL
CREATE TABLE category (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
);
```

Esineet:

```SQL
CREATE TABLE item (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        expired BOOLEAN NOT NULL,
        account_id INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        CHECK (expired IN (0, 1)),
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(category_id) REFERENCES category (id)
);
```

## Aloitussivulla näytetyt tilastot

### Esineiden määrät

```SQL
SELECT Account.username AS nimi, COUNT(Item.name) as lkm
        FROM Account, Item WHERE Account.id = Item.account_id
        GROUP BY nimi
        ORDER BY lkm DESC
);
```

### Kategorioiden määrät

```SQL
SELECT Account.username AS nimi, COUNT(Category.name) as lkm
        FROM Account, Item WHERE Account.id = Category.account_id
        GROUP BY nimi
        ORDER BY lkm DESC
);
```

## Koodissa olevat muut kyselyt, joita ei käytetä tällä hetkellä

### Tiettyyn kategoriaan kuuluvat esineet (esim. kategoria id 1)

```SQL
SELECT Item.name FROM item
        LEFT JOIN Account ON Item.account_id=Account.id
        LEFT JOIN Category ON Category.account_id=Account.id
        WHERE Category.id = 1
);
```

### Vanhentuneet/voimassa olevat esineet (Item.expired = True/False tilanteesta riippuen)

```SQL
SELECT Item.name FROM item
        LEFT JOIN Account ON Item.account_id=Account.id
        LEFT JOIN Category ON Category.account_id=Account.id
        WHERE Item.expired = True
);
```
