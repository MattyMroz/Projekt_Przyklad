DROP DATABASE IF EXISTS `app`;

CREATE DATABASE `app`;

USE `app`;

CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `fristname` varchar(32) NOT NULL,
    `lastname` varchar(32) NOT NULL,
    `login` varchar(32) NOT NULL,
    `email` varchar(64) NOT NULL,
    `password` varchar(64) NOT NULL,
    `phone` varchar(32),
    `address` varchar(64),
    `city` varchar(32),
    `zip` varchar(32),
    `region` varchar(64),
    `country` varchar(32),
    `access` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8;

-- przykładowy rekord
INSERT INTO
    `users` (
        `fristname`,
        `lastname`,
        `login`,
        `email`,
        `password`,
        `phone`,
        `address`,
        `city`,
        `zip`,
        `region`,
        `country`,
        `access`
    )
VALUES
    (
        'Andrzej',
        'Nowak',
        'Andrzeju',
        'andrzejnowak@gmail.com',
        '$2y$10$06USw3UXbijCRu.M9B6fO.RHeThufZ87ZY7urEvqYeMz6LViW/Heu',
        --Andrzeju123456
        '123456789',
        'ul. Lolowa 1',
        'Lolowo',
        '12-345',
        'Mazowieckie',
        'Polska',
        '0'
    );