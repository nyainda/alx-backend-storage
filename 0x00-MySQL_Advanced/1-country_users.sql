-- creates a table users following these requirements:

-- creates a table users following these requirements: id,email, name, country

CREATE TABLE
    IF NOT EXISTS users (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        name VARCHAR(255),
        email VARCHAR(255) UNIQUE NOT NULL,
        country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
    )