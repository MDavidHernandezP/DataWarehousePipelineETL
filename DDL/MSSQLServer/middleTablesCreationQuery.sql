-- SECTION products
CREATE TABLE products (
	id INT CONSTRAINT pk_products_id PRIMARY KEY,
	name VARCHAR(255),
	provider_id INT,
	category_id INT,
	bar_code INT,
	original_price FLOAT,
	discount INT,
	sale_price FLOAT,
	measure_unit VARCHAR(255),
	CONSTRAINT fk_products_providers_id
		FOREIGN KEY (provider_id)
		REFERENCES providers(id),
	CONSTRAINT fk_products_categories_id
		FOREIGN KEY (category_id)
		REFERENCES categories(id)
);

-- SECTION services
CREATE TABLE services (
	id INT CONSTRAINT pk_services_id PRIMARY KEY,
	name VARCHAR(255),
	branch_id INT,
	costs FLOAT,
	date DATE,
	CONSTRAINT fk_services_branches_id
		FOREIGN KEY (branch_id)
		REFERENCES branches(id)
);

-- SECTION employees
CREATE TABLE employees (
	id INT CONSTRAINT pk_employees_id PRIMARY KEY,
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
	CONSTRAINT fk_employees_positions_id
		FOREIGN KEY (position_id)
		REFERENCES positions(id),
	CONSTRAINT fk_employees_branches_id
		FOREIGN KEY (branch_id)
		REFERENCES branches(id)
);