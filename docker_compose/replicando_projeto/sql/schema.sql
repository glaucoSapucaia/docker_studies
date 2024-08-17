CREATE DATABASE flask_docker;

USE flask_docker;

CREATE TABLE `flask_docker`.`users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255)
);