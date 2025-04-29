-- SECTION purchases
INSERT INTO purchases (id, purchase_number, product_id, provider_id, branch_id,
                       product_quantity, total_cost, date, time, caducity_date, caducity_time)
VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11);

-- SECTION checkout
INSERT INTO checkout (id, number, branch_id, employee_id) VALUES (:1, :2, :3, :4);

-- SECTION sales
INSERT INTO sales (id, sale_number, branch_id, checkout_id, total_sale,
                   total_products, payment_type, client_name, date, time)
VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10);