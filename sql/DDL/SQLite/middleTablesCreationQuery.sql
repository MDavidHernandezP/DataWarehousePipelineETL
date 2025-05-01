-- SECTION products
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    provider_id INTEGER,
    category_id INTEGER,
    bar_code INTEGER,
    original_price REAL,
    discount INTEGER,
    sale_price REAL,
    measure_unit VARCHAR(255),
    FOREIGN KEY (provider_id) REFERENCES providers(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- SECTION services
CREATE TABLE services (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    branch_id INTEGER,
    costs REAL,
    date DATE,
    FOREIGN KEY (branch_id) REFERENCES branches(id)
);

-- SECTION employees
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    position_id INTEGER,
    branch_id INTEGER,
    income_date DATE,
    schedule VARCHAR(255),
    salary INTEGER,
    gender VARCHAR(255),
    age INTEGER,
    birth_date DATE,
    curp VARCHAR(255),
    rfc VARCHAR(255),
    nss INTEGER,
    FOREIGN KEY (position_id) REFERENCES positions(id),
    FOREIGN KEY (branch_id) REFERENCES branches(id)
);