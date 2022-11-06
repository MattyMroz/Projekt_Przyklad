DROP DATABASE IF EXISTS `szkola`;

CREATE DATABASE `szkola`;

USE `szkola`;

CREATE TABLE `uczniowie` (
    `id_ucz` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nazwisko` char(7) NOT NULL,
    `imie` char(7) NOT NULL,
    `pesel` char(11) NOT NULL,
    `adres_ul` char(8) NOT NULL,
    `adres_nr` char(3) NOT NULL,
    `miasto` char(7) NOT NULL
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8;

INSERT INTO
    `uczniowie`
VALUES
    (
        1,
        'Abacki',
        'Jan',
        95091202012,
        'Nocna',
        '21a',
        'Gnieno'
    ),
    (
        2,
        'Babacki',
        'Tomasz',
        96100102013,
        'Gwiezdna',
        '2',
        'Gniezno'
    ),
    (
        3,
        'Cabacki',
        'Jerzy',
        95110902056,
        'Mierna',
        '13b',
        'Kutno'
    ),
    (
        4,
        'Dabacki',
        'Tobiasz',
        94010398345,
        'Bierna',
        '3',
        'Miastko'
    ),
    (
        5,
        'Ebacki',
        'Adrian',
        95010198934,
        'Marna',
        '456',
        'Mielno'
    );