-- SECTION products
INSERT INTO products (id, name, provider_id, category_id, bar_code,
                      original_price, discount, sale_price, measure_unit)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);

-- SECTION services
INSERT INTO services (id, name, branch_id, costs, date)
VALUES (%s, %s, %s, %s, %s);

-- SECTION employees
INSERT INTO employees (id, name, position_id, branch_id, income_date, schedule, salary,
                       gender, age, birth_date, curp, rfc, nss)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);