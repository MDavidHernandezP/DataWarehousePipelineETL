-- SECTION categories
INSERT INTO categories (id, name) VALUES (?, ?);

-- SECTION providers
INSERT INTO providers (id, brand_name, contact_name, products_provided, contact_phone,
                        contact_email, location, address, rfc)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);

-- SECTION branches
INSERT INTO branches (id, name, location, manager, state) VALUES (?, ?, ?, ?, ?);

-- SECTION positions
INSERT INTO positions (id, name, salary) VALUES (?, ?, ?);