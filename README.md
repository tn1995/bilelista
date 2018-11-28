# bilelista
Sovellukseen voi lisätä omia bileitä, joihin muut kirjautuneet käyttäjät voivat osallistua. Sovellukseen pitää kirjautua, ennen kuin voi ilmoittautua tai luoda uusia bileitä. Vain bileet luonut käyttäjä voi poistaa omat bileensä. Etusivu on kirjautumissivu, jossa on myös linkki rekisteröitymiseen. Kirjautumisen jälkeen tulee lista bileistä ja niihin osallistuvien ihmisten määrä, sekä nappi, josta pääsee luomaan uudet bileet. Valitsemiaan bileitä klikkaamalla näkee listan osallistujista ja bileiden sijainnin, sekä pystyy laittamaan osallistuvansa niihin. Oman osallistumisensa voi poistaa. Samat bileet voivat olla eri vuosina eri sijainnissa.
  Tarvitaan ainakin viisi tietokantataulua. User, PartyUser, Party, PartyLocation ja Location.
  
[linkki sovellukseen](https://bilelista.herokuapp.com/)

[linkki kayttotapauksiin](https://github.com/tn1995/bilelista/blob/master/documentation/kayttotapaukset.md)

[linkki tietokantakaavioon](https://github.com/tn1995/bilelista/blob/master/documentation/tietokantakaavio.pdf)

Testitunnusten käyttäjänimi on Tuomas 
ja salasana on yolo

Tämänhetkiset toiminnallisuudet:
- Kirjautuminen ja rekisteröityminen
- Bileiden lisääminen ja poistaminen onnistuu. Poistaminen onnistuu vain henkilöltä, joka on luonut bileet listaan.
- Osallistu- nappia painamalla vain done arvo muuttuu trueksi

Tulevat toiminnallisuudet:
- Osallistumisnappia painamalla nappia painanut henkilö lisätään osallistujalistaan
- Bileitä klikkaamalla pääsee uudelle HTML- sivulle, jolta löytyy kaikki osallistujat ja bileiden tiedot, sekä sijainti
