CREATE TABLE categories (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE providers (
    id INT PRIMARY KEY,
    brand_name VARCHAR(255),
    contact_name VARCHAR(255),
    products_provided INT,
    contact_phone VARCHAR(255),
    contact_email VARCHAR(255),
    location VARCHAR(255),
    address VARCHAR(255),
    rfc VARCHAR(255)
);

CREATE TABLE branches (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    manager VARCHAR(255),
    state VARCHAR(255)
);

CREATE TABLE positions (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    salary INT
);