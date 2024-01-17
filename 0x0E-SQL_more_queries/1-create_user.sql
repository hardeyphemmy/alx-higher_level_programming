-- user should have all priviledges password 
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- all privileges to server
GRANT ALL PRIVILEDGES ON *.* TO user_0d_1@localhost;
