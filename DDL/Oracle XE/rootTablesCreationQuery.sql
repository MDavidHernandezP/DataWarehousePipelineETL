-- SECTION categories
CREATE TABLE categories (
    id NUMBER(10) CONSTRAINT pk_categories_id PRIMARY KEY,
    name VARCHAR2(255)
);

-- SECTION providers
CREATE TABLE providers (
    id NUMBER(10) CONSTRAINT pk_providers_id PRIMARY KEY,
    brand_name VARCHAR2(255),
    contact_name VARCHAR2(255),
    products_provided NUMBER(10),
    contact_phone VARCHAR2(255),
    contact_email VARCHAR2(255),
    location VARCHAR2(255),
    address VARCHAR2(255),
    rfc VARCHAR2(255)
);

-- SECTION branches
CREATE TABLE branches (
    id NUMBER(10) CONSTRAINT pk_branches_id PRIMARY KEY,
    name VARCHAR2(255),
    location VARCHAR2(255),
    manager VARCHAR2(255),
    state VARCHAR2(255)
);

-- SECTION positions
CREATE TABLE positions (
    id NUMBER(10) CONSTRAINT pk_positions_id PRIMARY KEY,
    name VARCHAR2(255),
    salary NUMBER(10)
);