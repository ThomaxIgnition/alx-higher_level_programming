#!/usr/bin/env bash
-- a script that creates the first_table table in the
-- current database in MySQL server
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
