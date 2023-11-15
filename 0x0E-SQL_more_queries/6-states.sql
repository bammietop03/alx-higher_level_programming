-- creates the database hbtn_0d_usa and the table states (in hbtn_0d_usa)
CREATE DATABASE hbtn_0d_usa IF NOT EXISTS;
USE hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
