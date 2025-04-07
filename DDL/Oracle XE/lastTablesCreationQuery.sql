CREATE TABLE purchases (
    id NUMBER(10) CONSTRAINT pk_purchases_id PRIMARY KEY,
    purchase_number NUMBER(20),
    product_id NUMBER(10),
    provider_id NUMBER(10),
    branch_id NUMBER(10),
    product_quantity NUMBER(10),
    total_cost NUMBER(10, 2),
    purchase_date DATE,
    purchase_time TIMESTAMP,
    caducity_date DATE,
    caducity_time TIMESTAMP,
    CONSTRAINT fk_purchases_products_id
        FOREIGN KEY (product_id)
        REFERENCES products(id),
    CONSTRAINT fk_purchases_providers_id
        FOREIGN KEY (provider_id)
        REFERENCES providers(id),
    CONSTRAINT fk_purchases_branches_id
        FOREIGN KEY (branch_id)
        REFERENCES branches(id)
);

CREATE TABLE checkout (
    id NUMBER(10) CONSTRAINT pk_checkout_id PRIMARY KEY,
    checkout_number NUMBER(10),
    branch_id NUMBER(10),
    employee_id NUMBER(10),
    CONSTRAINT fk_checkout_branches_id
        FOREIGN KEY (branch_id)
        REFERENCES branches(id),
    CONSTRAINT fk_checkout_employees_id
        FOREIGN KEY (employee_id)
        REFERENCES employees(id)
);

CREATE TABLE sales (
    id NUMBER(10) CONSTRAINT pk_sales_id PRIMARY KEY,
    sale_number NUMBER(20),
    branch_id NUMBER(10),
    checkout_id NUMBER(10),
    total_sale NUMBER(10, 2),
    total_products NUMBER(10),
    payment_type VARCHAR2(255),
    client_name VARCHAR2(255),
    sale_date DATE,
    sale_time TIMESTAMP,
    CONSTRAINT fk_sales_branches_id
        FOREIGN KEY (branch_id)
        REFERENCES branches(id),
    CONSTRAINT fk_sales_checkout_id
        FOREIGN KEY (checkout_id)
        REFERENCES checkout(id)
);