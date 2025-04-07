CREATE TABLE purchases (
	id INT CONSTRAINT pk_purchases_id PRIMARY KEY,
	purchase_number INT,
	product_id INT,
	provider_id INT,
	branch_id INT,
	product_quantity INT,
	total_cost FLOAT,
	date DATE,
	time TIME,
	caducity_date DATE,
	caducity_time TIME,
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
	id INT CONSTRAINT pk_checkout_id PRIMARY KEY,
	number INT,
	branch_id INT,
	employee_id INT,
	CONSTRAINT fk_checkout_branches_id
		FOREIGN KEY (branch_id)
		REFERENCES branches(id),
	CONSTRAINT fk_checkout_employees_id
		FOREIGN KEY (employee_id)
		REFERENCES employees(id)
);

CREATE TABLE sales (
	id INT CONSTRAINT pk_sales_id PRIMARY KEY,
	sale_number INT,
	branch_id INT,
	checkout_id INT,
	total_sale FLOAT,
	total_products INT,
	payment_type VARCHAR(255),
	client_name VARCHAR(255),
	date DATE,
	time TIME,
	CONSTRAINT fk_sales_branches_id
		FOREIGN KEY (branch_id)
		REFERENCES branches(id),
	CONSTRAINT fk_sales_checkout_id
		FOREIGN KEY (checkout_id)
		REFERENCES checkout(id)
);