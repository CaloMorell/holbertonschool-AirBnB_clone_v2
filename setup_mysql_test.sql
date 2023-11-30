<<<<<<< HEAD
-- Write a script that prepares a MySQL server for the project
=======
"""Write a script that prepares a MySQL server for the project"""
>>>>>>> 7277493441002411fef3e625cb1f0175110f3ad7

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
