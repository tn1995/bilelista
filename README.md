# bilelista
Sovellukseen voi lisätä omia bileitä, joihin muut kirjautuneet käyttäjät voivat osallistua. Sovellukseen pitää kirjautua, ennen kuin voi ilmoittautua tai luoda uusia bileitä. Vain bileet luonut käyttäjä voi poistaa omat bileensä. Etusivu on kirjautumissivu, jossa on myös linkki rekisteröitymiseen. Kirjautumisen jälkeen tulee lista bileistä sekä nappi, josta pääsee luomaan uudet bileet. Valitsemiaan bileitä klikkaamalla näkee listan osallistujista, sekä pystyy laittamaan osallistuvansa niihin. Oman osallistumisensa voi poistaa.
  Käytössä on 3 tietokantataulua: Account, User_task ja Task.
  
[linkki sovellukseen](https://bilelista.herokuapp.com/)

[linkki kayttotapauksiin](https://github.com/tn1995/bilelista/blob/master/documentation/kayttotapaukset.md)

[linkki tietokantakaavioon](https://github.com/tn1995/bilelista/blob/master/documentation/tietokantakaavio.pdf)

[linkki asennusohjeisiin](https://github.com/tn1995/bilelista/blob/master/documentation/asennusohjeet.md)

Testitunnusten käyttäjänimi on Tuomas 
ja salasana on Tuomas

Toiminnallisuudet:
- Kirjautuminen ja rekisteröityminen
- Bileiden lisääminen ja poistaminen onnistuu. Poistaminen onnistuu vain henkilöltä, joka on luonut bileet listaan.
- Bileisiin voi osallistua ja osallistumisen voi poistaa
- Bileet voi merkitä alkaneeksi vain niiden luoja
- Sovellus listaa henkilöt, joilla ei ole bileitä
- Bileitä klikkaamalla pääsee uudelle HTML- sivulle, jolta löytyy kaikki osallistujat
- Jokaisella henkilöllä on myös omat sivut

# CREATE TABLE- komennot

CREATE TABLE user_task (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	account_id INTEGER NOT NULL, 
	task_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(task_id) REFERENCES task (id))
	
CREATE TABLE user_task (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	account_id INTEGER NOT NULL, 
	task_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(task_id) REFERENCES task (id))
	
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)

# SQL-kyselyt
Listataan kaikki bileet:

SELECT Account.name AS account_name, Task.id, Task.done, Task.name, Task.date, Task.klo, Task.location FROM Account LEFT JOIN Task ON Task.account_id = Account.id WHERE Task.account_id = Account.id GROUP BY Task.id, account.name

Listataan valitun käyttäjän bileet:

SELECT Task.id, Task.name, Task.date FROM Account JOIN Task ON Account.id = Task.account_id WHERE (Account.username = :username) GROUP BY Account.id, task.name, task.id

Listataan kaikki valittuun bileisiin osallistujat:

SELECT Account.name FROM Account LEFT JOIN User_task ON User_task.account_id = Account.id WHERE User_task.account_id = Account.id AND User_task.task_id = :task_id GROUP BY Account.id

Poistetaan valittu osallistuja bileistä:

DELETE FROM user_task WHERE User_task.account_id = :account_id AND User_task.task_id = :task_id

Näytetään osallistujat, jotka eivät ole luoneet bileitä:

SELECT Account.id, Account.name FROM Account LEFT JOIN Task ON Task.account_id = Account.id WHERE Task.done IS null OR Task.done = :done GROUP BY Account.id HAVING COUNT(Task.id) = 0

Poistetaan tiettyihin bileisiin osallistujat user_task liitostaulusta:

DELETE FROM user_task WHERE User_task.task_id = task_id

Haetaan käyttäjän tiedot käyttäjätunnuksen perusteella:

SELECT Account.id, Account.name, Account.username FROM Account WHERE Account.username = username

# Omat kokemukset
Materiaalit ovat hyvät ja sovelluksen tekeminen on ollut hauskaa. On hyvä, että tekemisen tueksi on järjestetty paja, sillä siitä on ollut reilusti apua.
