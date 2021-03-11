SELECT * FROM shows WHERE title = "friends";
SELECT * FROM genres WHERE name LIKE "action";
SELECT * FROM genres WHERE name LIKE "Adventure";
SELECT name FROM genres WHERE name = "comedy";
SELECT title FROM shows WHERE id IN (SELECT id FROM genres WHERE name = "comedy");
SELECT DISTINCT(name) FROM genres WHERE id IN (SELECT id FROM shows WHERE title = "friends") ORDER BY name;
SELECT DISTINCT(name) FROM genres WHERE id IN (SELECT id FROM shows WHERE title = "brooklyn99") ORDER BY name;

SELECT id FROM shows WHERE title = "friends";

SELECT * FROM genres;
SELECT id as number, title FROM shows;

SELECT DISTINCT(title) FROM shows;
SELECT id, name FROM genres LIMIT 3;
SELECT * FROM shows WHERE id = "1" or id = "2";
SELECT * FROM shows WHERE title LIKE "%n%" and title LIKE "%e%";
SELECT * FROM shows WHERE id BETWEEN 2 AND 4;
SELECT * FROM genres WHERE name IN ("crime", "adventure", "romance");
SELECT id, name FROM genres WHERE name LIKE "%om%";
SELECT id, title FROM shows WHERE title NOT IN ("friends", "brooklyn99");

SELECT id, name FROM genres ORDER BY name;
SELECT id, name FROM genres ORDER BY id DESC LIMIT 3;

ALTER TABLE shows ADD COLUMN year INTEGER;
SELECT * FROM shows;
ALTER TABLE shows RENAME year TO YYYY;
SELECT * FROM shows;
ALTER TABLE shows RENAME TO shows_new;
SELECT * FROM shows_new;
ALTER TABLE shows_new RENAME TO shows;
SELECT * FROM shows;

INSERT INTO shows(title) VALUES ("My favorite show");
SELECT * FROM shows;

-- No recommend.
INSERT INTO shows VALUES ("My brand new show");
SELECT * FROM shows;

-- CRUD
UPDATE shows SET title = "qwerty" WHERE id BETWEEN 2 AND 4;
SELECT * FROM shows;

UPDATE shows SET title = "rty123" WHERE id = 1;
SELECT * FROM shows;

DELETE FROM shows WHERE title LIKE "QWERTY";
SELECT * FROM shows;

SELECT title FROM shows GROUP BY title ORDER BY title;

-- aggregated functions AVG, COUNT, MAX, MIN, SUM
SELECT title, SUM(id) FROM shows GROUP BY title;
