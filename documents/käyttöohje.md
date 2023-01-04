# Käyttöohje

Lataa ja asenna projekti githubista, sen jälkeen voit käynnistää pelin omalta koneeltasi.

## Ohjelman käynnistäminen

Ennen kuin käynnistät ohjelman pitää asentaa riippuvuudet komennolla:

```bash
poetry install
```

Nyt ohjelman voi käynnistää komennolla

```bash
poetry run invoke start
```
joka käynnistää python moduulin connectfour.py hakemistosta src.

mikäli koneesi asetuksista riippuen sinulla ei toimi pelkästään komento python vaan python3, vois käynnistä pelin komennolla

```bash
poetry run invoke start3
```

Voit myös käynnistää pelin ajamalla 
```bash
main.py
```
ohjelman hakemistosta src.

## Pelaaminen

Peliä pelataan graafisesti hiirellä ohjaamalla pelimerkki sen pystykolumnin kohdalle, johon pelimerkki halutaan tiputtaa.
