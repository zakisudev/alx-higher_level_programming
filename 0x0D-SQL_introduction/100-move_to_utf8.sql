-- Change database to UTF-8
USE htbn_0c_0;
-- Change name to UTF-8
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
