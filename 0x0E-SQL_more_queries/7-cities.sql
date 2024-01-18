-- create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use database
USE hbtn_0d_usa;

-- create table cities
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE NOT NULL AUTO_INCREMENT, state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id), 
FOREIGN KEY(state_id) REFERENCE states(id));
