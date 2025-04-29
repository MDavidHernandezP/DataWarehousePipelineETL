-- SECTION products
INSERT INTO products (id, name, provider_id, category_id, bar_code,
                      original_price, discount, sale_price, measure_unit)
VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9);

-- SECTION services
INSERT INTO services (id, name, branch_id, costs, date)
VALUES (:1, :2, :3, :4, :5);

-- SECTION employees
INSERT INTO employees (id, name, position_id, branch_id, income_date, schedule, salary,
                       gender, age, birth_date, curp, rfc, nss)
VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13);