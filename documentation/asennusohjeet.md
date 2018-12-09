Asennusohjeet bilelistaan:

- Käytössäsi tulee olla vähintään Pythonin versio 3.5, Pythonin pip sekä venv-kirjasto. 
- Käytössäsi tulee olla myös git työvälineet, sekä työvälineet Herokun käyttöön.
- Suosittelen myös käyttämään jotain muuta, kuin Windows-käyttöjärjestelmää.

Sovelluksen asennusvaiheet:

1. Lataa projekti Githubista projekti omalle koneellesi zip-muodossa ja pura se johonkin kansioon.
2. Virtuaaliympäristö otetaan käyttöön terminaalissa komennolla "python3 -m venv venv" ja se aktivoidaan komennolla source "venv/bin/activate".
3. Asenna projektin riippuvuudet komennolla "pip install -r requirements.txt"
3. Sovellus käynnistetään lokaalisti komennolla "python run.py".

Herokuun lataaminen:

1. Kun olet tehnyt edellä olevat vaiheet ja sinulla on herokun käyttäjätunnus voit asentaa projektin Herokuun komennolla: "heroku create sovelluksen-nimi", päättämällä sovellukselle haluamasi nimen.
2. Kun muokkaat projektia ja olet commitannut muutoksesi, voit päivittää herokua komennolla "git push heroku master".


