CREATE USER 'lafrise'@'localhost' IDENTIFIED BY 'lafrise';
CREATE DATABASE lafrise;
GRANT ALL PRIVILEGES ON lafrise.* TO 'lafrise'@'localhost';
USE lafrise;
CREATE TABLE events(id int NOT NULL AUTO_INCREMENT, name VARCHAR(500), description VARCHAR(4000) NOT NULL, url VARCHAR(500), source VARCHAR(200) NOT NULL, date DATE NOT NULL, PRIMARY KEY(id));
