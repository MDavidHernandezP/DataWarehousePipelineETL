CREATE TABLE products (
    id NUMBER(10) CONSTRAINT pk_products_id PRIMARY KEY,
    name VARCHAR2(255),
    provider_id NUMBER(10),
    category_id NUMBER(10),
    bar_code NUMBER(20),
    original_price NUMBER(10, 2),
    discount NUMBER(3),
    sale_price NUMBER(10, 2),
    measure_unit VARCHAR2(255),
    CONSTRAINT fk_products_providers_id
        FOREIGN KEY (provider_id)
        REFERENCES providers(id),
    CONSTRAINT fk_products_categories_id
        FOREIGN KEY (category_id)
        REFERENCES categories(id)
);

CREATE TABLE services (
    id NUMBER(10) CONSTRAINT pk_services_id PRIMARY KEY,
    name VARCHAR2(255),
    branch_id NUMBER(10),
    costs NUMBER(10, 2),
    issue_date DATE,
    CONSTRAINT fk_services_branches_id
        FOREIGN KEY (branch_id)
        REFERENCES branches(id)
);

CREATE TABLE employees (
    id NUMBER(10) CONSTRAINT pk_employees_id PRIMARY KEY,
    name VARCHAR2(255),
    position_id NUMBER(10),
    branch_id NUMBER(10),
    income_date DATE,
    schedule VARCHAR2(255),
    salary NUMBER(10),
    gender VARCHAR2(255),
    age NUMBER(3),
    birth_date DATE,
    curp VARCHAR2(255),
    rfc VARCHAR2(255),
    nss NUMBER(20),
    CONSTRAINT fk_employees_positions_id
        FOREIGN KEY (position_id)
        REFERENCES positions(id),
    CONSTRAINT fk_employees_branches_id
        FOREIGN KEY (branch_id)
        REFERENCES branches(id)
);