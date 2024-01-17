-- A script that converts 'hbtn_0c_0' to UTF8
USE hbtn_0c_0;

-- convert table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4_unicode_ci;

-- convert field to UTF8
ALTER TABLE first_table MODIFY COLUMN name TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;:x

