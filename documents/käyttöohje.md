# Käyttöohje

Lataa projekti.

## Ohjelman käynnistäminen

Ennen kuin käynnistät ohjelman pitää asentaa riippuvuudet komennolla:

```bash
poetry install
```

Nyt ohjelman voi käynnistää komennolla

**
poetry run invoke start
**
joka käynnistää python moduulin connectfour.py hakemistosta src.

mikäli koneesi asetuksista riippuen sinulla ei toimi pelkästään komento python vaan python3, vois käynnistä pelin komennolla
**
poetry run invoke start3
**


## Pelaaminen

Peliä pelataan graafisesti hiirellä ohjaamalla pelimerkki sen pystykolumnin kohdalle, johon pelimerkki halutaan tiputtaa.
