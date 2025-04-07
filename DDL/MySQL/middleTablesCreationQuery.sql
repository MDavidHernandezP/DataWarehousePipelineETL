CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    provider_id INT,
    category_id INT,
    bar_code INT,
    original_price FLOAT(10,2),
    discount INT,
    sale_price FLOAT(10,2),
    measure_unit VARCHAR(255),
    FOREIGN KEY (provider_id) 
		REFERENCES providers(id),
    FOREIGN KEY (category_id) 
		REFERENCES categories(id)
);

CREATE TABLE services (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    branch_id INT,
    costs FLOAT(10,2),
    date DATE,
    FOREIGN KEY (branch_id) 
		REFERENCES branches(id)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    position_id INT,
    branch_id INT,
    income_date DATE,
    schedule VARCHAR(255),
    salary INT,
    gender VARCHAR(255),
    age INT,
    birth_date DATE,
    curp VARCHAR(255),
    rfc VARCHAR(255),
    nss INT,
    FOREIGN KEY (position_id) 
		REFERENCES positions(id),
    FOREIGN KEY (branch_id) 
		REFERENCES branches(id)
);