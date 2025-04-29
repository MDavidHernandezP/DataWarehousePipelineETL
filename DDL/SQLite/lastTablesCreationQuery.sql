-- SECTION purchases
CREATE TABLE purchases (
    id INTEGER PRIMARY KEY,
    purchase_number INTEGER,
    product_id INTEGER,
    provider_id INTEGER,
    branch_id INTEGER,
    product_quantity INTEGER,
    total_cost REAL,
    date DATE,
    time TEXT,
    caducity_date DATE,
    caducity_time TEXT,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (provider_id) REFERENCES providers(id),
    FOREIGN KEY (branch_id) REFERENCES branches(id)
);

-- SECTION checkout
CREATE TABLE checkout (
    id INTEGER PRIMARY KEY,
    number INTEGER,
    branch_id INTEGER,
    employee_id INTEGER,
    FOREIGN KEY (branch_id) REFERENCES branches(id),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- SECTION sales
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    sale_number INTEGER,
    branch_id INTEGER,
    checkout_id INTEGER,
    total_sale REAL,
    total_products INTEGER,
    payment_type VARCHAR(255),
    client_name VARCHAR(255),
    date DATE,
    time TEXT,
    FOREIGN KEY (branch_id) REFERENCES branches(id),
    FOREIGN KEY (checkout_id) REFERENCES checkout(id)
);