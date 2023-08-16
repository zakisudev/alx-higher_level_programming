-- Query to create new user if not exist

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- Grant privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
