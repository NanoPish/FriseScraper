CREATE USER 'lafrise'@'localhost' IDENTIFIED BY 'lafrise';
CREATE DATABASE lafrise;
GRANT ALL PRIVILEGES ON lafrise.* TO 'lafrise'@'localhost';
USE lafrise;
CREATE TABLE events(id int NOT NULL AUTO_INCREMENT, name VARCHAR(255), description VARCHAR(510) NOT NULL, url VARCHAR(255), source VARCHAR(100) NOT NULL, date DATE NOT NULL, PRIMARY KEY(id)); 
