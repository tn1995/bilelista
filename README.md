# bilelista
Sovellukseen voi lisätä omia bileitä, joihin muut kirjautuneet käyttäjät voivat osallistua. Sovellukseen pitää kirjautua, ennen kuin voi ilmoittautua tai luoda uusia bileitä. Vain bileet luonut käyttäjä voi poistaa omat bileensä. Etusivu on kirjautumissivu, jossa on myös linkki rekisteröitymiseen. Kirjautumisen jälkeen tulee lista bileistä sekä nappi, josta pääsee luomaan uudet bileet. Valitsemiaan bileitä klikkaamalla näkee listan osallistujista, sekä pystyy laittamaan osallistuvansa niihin. Oman osallistumisensa voi poistaa.
  Tarvitaan todennäköisesti 4 tietokantataulua. Account, User_task, Task ja Location.
  
[linkki sovellukseen](https://bilelista.herokuapp.com/)

[linkki kayttotapauksiin](https://github.com/tn1995/bilelista/blob/master/documentation/kayttotapaukset.md)

[linkki alkuperäiseen tietokantakaavioon](https://github.com/tn1995/bilelista/blob/master/documentation/tietokantakaavio.pdf)

[linkki tämänhetkiseen tietokantakaavioon](https://github.com/tn1995/bilelista/blob/master/documentation/TietokantakaavioUPDATE.pdf)

[linkki asennusohjeisiin](https://github.com/tn1995/bilelista/blob/master/documentation/asennusohjeet.md)

Testitunnusten käyttäjänimi on Tuomas 
ja salasana on Tuomas

Tämänhetkiset toiminnallisuudet:
- Kirjautuminen ja rekisteröityminen
- Bileiden lisääminen ja poistaminen onnistuu. Poistaminen onnistuu vain henkilöltä, joka on luonut bileet listaan.
- Bileisiin voi osallistua ja osallistumisen voi poistaa
- Osallistu- nappia painamalla vain done arvo muuttuu trueksi
- Sovellus listaa henkilöt, joilla ei ole bileitä
- Bileitä klikkaamalla pääsee uudelle HTML- sivulle, jolta löytyy kaikki osallistujat

Puuttuvat toiminnallisuudet ja ongelmat:
- Osallistumisen poisto poistaa kaikkien samoihin bileisiin osallistuneiden osallistumisen
- Bileiden sijainti ja päivämäärä pitää vielä saada näkyviin

# Omat kokemukset
Materiaalit ovat hyvät ja sovelluksen tekeminen on ollut hauskaa. On hyvä, että tekemisen tueksi on järjestetty paja, sillä siitä on ollut reilusti apua.
