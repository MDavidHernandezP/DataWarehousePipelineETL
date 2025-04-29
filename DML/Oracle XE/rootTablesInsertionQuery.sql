-- SECTION categories
INSERT INTO categories (id, name) VALUES (:1, :2);

-- SECTION providers
INSERT INTO providers (id, brand_name, contact_name, products_provided, contact_phone,
                        contact_email, location, address, rfc)
VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9);

-- SECTION branches
INSERT INTO branches (id, name, location, manager, state) VALUES (:1, :2, :3, :4, :5);

-- SECTION positions
INSERT INTO positions (id, name, salary) VALUES (:1, :2, :3);