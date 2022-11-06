-- UŻYTKOWNICY
-- pierwszy może tylko wyświetlać dane;
-- drugi może wyświetlać oraz edytować, dodawać, usuwać dane
CREATE USER 'user1' @'localhost' IDENTIFIED BY 'user1';

GRANT
SELECT
    ON szkola.uczniowie TO 'user1' @'localhost';

CREATE USER 'user2' @'localhost' IDENTIFIED BY 'user2';

GRANT
SELECT
,
INSERT
,
UPDATE
,
    DELETE ON szkola.uczniowie TO 'user2' @'localhost';

-- -- USUŃ UŻYTKOWNIKÓW
-- DROP USER 'user1' @'localhost';
-- DROP USER 'user2' @'localhost';
-- -- WYŚWIETL WSZYTSTKICH UŻYTKOWNIKÓW Z BAZY DANYCH
-- SELECT user, host FROM mysql.user;

-- wyąświetl uprawnienia dla user2
-- SHOW GRANTS FOR 'user2' @'localhost';