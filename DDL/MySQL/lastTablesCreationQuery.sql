-- SECTION purchases
CREATE TABLE purchases (
    id INT PRIMARY KEY,
    purchase_number INT,
    product_id INT,
    provider_id INT,
    branch_id INT,
    product_quantity INT,
    total_cost FLOAT(10,2),
    date DATE,
    time TIME,
    caducity_date DATE,
    caducity_time TIME,
    FOREIGN KEY (product_id) 
		REFERENCES products(id),
    FOREIGN KEY (provider_id) 
		REFERENCES providers(id),
    FOREIGN KEY (branch_id) 
		REFERENCES branches(id)
);

-- SECTION checkout
CREATE TABLE checkout (
    id INT PRIMARY KEY,
    number INT,
    branch_id INT,
    employee_id INT,
    FOREIGN KEY (branch_id) 
		REFERENCES branches(id),
    FOREIGN KEY (employee_id) 
		REFERENCES employees(id)
);

-- SECTION sales
CREATE TABLE sales (
    id INT PRIMARY KEY,
    sale_number INT,
    branch_id INT,
    checkout_id INT,
    total_sale FLOAT(10,2),
    total_products INT,
    payment_type VARCHAR(255),
    client_name VARCHAR(255),
    date DATE,
    time TIME,
    FOREIGN KEY (branch_id) 
		REFERENCES branches(id),
    FOREIGN KEY (checkout_id) 
		REFERENCES checkout(id)
);