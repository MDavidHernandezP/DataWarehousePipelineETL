import mysql.connector
from dataGenerator import generate_all_data

def connect_to_mysql(host, user, password, database):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return conn
    except Exception as e:
        print("Error connecting to MySQL:", e)
        return None

def insert_data_to_mysql(conn, data, N):
    cursor = conn.cursor()
    print("Inserting data into MySQL...")

    for i in range(N):
        if i < len(data['categories']):
            cat = data['categories'][i]
            cursor.execute("INSERT INTO categories (id, name) VALUES (%s, %s)", (cat["id"], cat["name"]))

        if i < len(data['providers']):
            prov = data['providers'][i]
            cursor.execute("""
                INSERT INTO providers (id, brand_name, contact_name, products_provided, contact_phone,
                                       contact_email, location, address, rfc)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (prov["id"], prov["brand_name"], prov["contact_name"], prov["products_provided"],
                  prov["contact_phone"], prov["contact_email"], prov["location"], prov["address"], prov["rfc"]))

        if i < len(data['branches']):
            branch = data['branches'][i]
            cursor.execute("INSERT INTO branches (id, name, location, manager, state) VALUES (%s, %s, %s, %s, %s)",
                           (branch["id"], branch["name"], branch["location"], branch["manager"], branch["state"]))

        if i < len(data['positions']):
            pos = data['positions'][i]
            cursor.execute("INSERT INTO positions (id, name, salary) VALUES (%s, %s, %s)",
                           (pos["id"], pos["name"], pos["salary"]))

        if i < len(data['products']):
            prod = data['products'][i]
            cursor.execute("""
                INSERT INTO products (id, name, provider_id, category_id, bar_code,
                                      original_price, discount, sale_price, measure_unit)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (prod["id"], prod["name"], prod["provider_id"], prod["category_id"], prod["bar_code"],
                  prod["original_price"], prod["discount"], prod["sale_price"], prod["measure_unit"]))

        if i < len(data['services']):
            serv = data['services'][i]
            cursor.execute("""
                INSERT INTO services (id, name, branch_id, costs, date)
                VALUES (%s, %s, %s, %s, %s)
            """, (serv["id"], serv["name"], serv["branch_id"], serv["costs"], serv["date"]))

        if i < len(data['employees']):
            emp = data['employees'][i]
            cursor.execute("""
                INSERT INTO employees (id, name, position_id, branch_id, income_date, schedule, salary,
                                       gender, age, birth_date, curp, rfc, nss)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (emp["id"], emp["name"], emp["position_id"], emp["branch_id"], emp["income_date"],
                  emp["schedule"], emp["salary"], emp["gender"], emp["age"], emp["birth_date"],
                  emp["curp"], emp["rfc"], emp["nss"]))

        if i < len(data['purchases']):
            pur = data['purchases'][i]
            cursor.execute("""
                INSERT INTO purchases (id, purchase_number, product_id, provider_id, branch_id,
                                       product_quantity, total_cost, date, time,
                                       caducity_date, caducity_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (pur["id"], pur["purchase_number"], pur["product_id"], pur["provider_id"],
                  pur["branch_id"], pur["product_quantity"], pur["total_cost"], pur["date"],
                  pur["time"], pur["caducity_date"], pur["caducity_time"]))

        if i < len(data['checkout']):
            co = data['checkout'][i]
            cursor.execute("INSERT INTO checkout (id, number, branch_id, employee_id) VALUES (%s, %s, %s, %s)",
                           (co["id"], co["number"], co["branch_id"], co["employee_id"]))

        if i < len(data['sales']):
            sale = data['sales'][i]
            cursor.execute("""
                INSERT INTO sales (id, sale_number, branch_id, checkout_id, total_sale,
                                   total_products, payment_type, client_name, date, time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (sale["id"], sale["sale_number"], sale["branch_id"], sale["checkout_id"],
                  sale["total_sale"], sale["total_products"], sale["payment_type"],
                  sale["client_name"], sale["date"], sale["time"]))

    conn.commit()
    print("Data inserted successfully into MySQL.")

def main():
    # Change these values according to your MySQL setup.
    host = "localhost"
    database = "supermercado"
    user = "sa"
    password = "your_secure_password"

    conn = connect_to_mysql(host, database, user, password)
    if conn:
        N = 10
        data = generate_all_data(N)
        insert_data_to_mysql(conn, data, N)
        conn.close()

if __name__ == "__main__":
    main()