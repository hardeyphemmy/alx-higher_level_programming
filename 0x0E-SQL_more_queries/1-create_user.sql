-- user should have all privileges password 
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- all privileges to servers
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
