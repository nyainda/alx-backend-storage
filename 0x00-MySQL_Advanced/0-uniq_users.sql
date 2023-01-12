-- creates a table  users following these requirements:

-- With these attributes: id, email, name

CREATE TABLE
    IF NOT EXISTS users (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        name VARCHAR(255),
        email VARCHAR(255) UNIQUE NOT NULL
    );