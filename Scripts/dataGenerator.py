# Dummy Data Generator.

import random
import json
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

def generate_categories(N):
    return [{"id": i + 1, "name": fake.word()} for i in range(N)]

def generate_providers(N):
    return [{
        "id": i + 1,
        "brand_name": fake.company(),
        "contact_name": fake.name(),
        "products_provided": random.randint(5, 100),
        "contact_phone": fake.phone_number(),
        "contact_email": fake.email(),
        "location": fake.city(),
        "address": fake.address(),
        "rfc": fake.lexify(text='????######XXX')
    } for i in range(N)]

def generate_branches(N):
    return [{
        "id": i + 1,
        "name": f"Sucursal {fake.city()}",
        "location": fake.city(),
        "manager": fake.name(),
        "state": fake.state()
    } for i in range(N)]

def generate_positions(N):
    positions = ['Cajero', 'Gerente', 'Reponedor', 'Limpieza', 'Supervisor']
    return [{
        "id": i + 1,
        "name": positions[i % len(positions)],
        "salary": random.randint(6000, 25000)
    } for i in range(N)]

def generate_products(N, providers, categories):
    return [{
        "id": i + 1,
        "name": fake.word(),
        "provider_id": random.choice(providers)["id"],
        "category_id": random.choice(categories)["id"],
        "bar_code": random.randint(1000000000000, 9999999999999),
        "original_price": round(random.uniform(10, 100), 2),
        "discount": random.randint(0, 30),
        "sale_price": round(random.uniform(10, 100), 2),
        "measure_unit": random.choice(["kg", "unit", "liters", "box"])
    } for i in range(N)]

def generate_services(N, branches):
    return [{
        "id": i + 1,
        "name": fake.bs(),
        "branch_id": random.choice(branches)["id"],
        "costs": round(random.uniform(100, 1000), 2),
        "date": fake.date()
    } for i in range(N)]

def generate_employees(N, positions, branches):
    return [{
        "id": i + 1,
        "name": fake.name(),
        "position_id": random.choice(positions)["id"],
        "branch_id": random.choice(branches)["id"],
        "income_date": fake.date_between(start_date='-3y', end_date='today'),
        "schedule": random.choice(["Matutino", "Vespertino", "Nocturno"]),
        "salary": random.randint(6000, 25000),
        "gender": random.choice(["M", "F"]),
        "age": random.randint(18, 65),
        "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=65),
        "curp": fake.lexify(text='????######??????XX'),
        "rfc": fake.lexify(text='????######XXX'),
        "nss": random.randint(10000000000, 99999999999)
    } for i in range(N)]

def generate_purchases(N, products, providers, branches):
    return [{
        "id": i + 1,
        "purchase_number": random.randint(1000, 9999),
        "product_id": random.choice(products)["id"],
        "provider_id": random.choice(providers)["id"],
        "branch_id": random.choice(branches)["id"],
        "product_quantity": random.randint(1, 100),
        "total_cost": round(random.uniform(100, 1000), 2),
        "date": fake.date(),
        "time": fake.time(),
        "caducity_date": fake.future_date(end_date="+2y"),
        "caducity_time": fake.time()
    } for i in range(N)]

def generate_checkout(N, branches, employees):
    return [{
        "id": i + 1,
        "number": random.randint(1, 10),
        "branch_id": random.choice(branches)["id"],
        "employee_id": random.choice(employees)["id"]
    } for i in range(N)]

def generate_sales(N, branches, checkouts):
    return [{
        "id": i + 1,
        "sale_number": random.randint(10000, 99999),
        "branch_id": random.choice(branches)["id"],
        "checkout_id": random.choice(checkouts)["id"],
        "total_sale": round(random.uniform(100, 1000), 2),
        "total_products": random.randint(1, 20),
        "payment_type": random.choice(["Efectivo", "Tarjeta", "Transferencia"]),
        "client_name": fake.name(),
        "date": fake.date(),
        "time": fake.time()
    } for i in range(N)]

def generate_all_data(N):
    categories = generate_categories(N)
    providers = generate_providers(N)
    branches = generate_branches(N)
    positions = generate_positions(N)
    products = generate_products(N, providers, categories)
    services = generate_services(N, branches)
    employees = generate_employees(N, positions, branches)
    purchases = generate_purchases(N, products, providers, branches)
    checkout = generate_checkout(N, branches, employees)
    sales = generate_sales(N, branches, checkout)

    data = {
        "categories": categories,
        "providers": providers,
        "branches": branches,
        "positions": positions,
        "products": products,
        "services": services,
        "employees": employees,
        "purchases": purchases,
        "checkout": checkout,
        "sales": sales
    }

    return data

if __name__ == "__main__":
    N = 10
    data = generate_all_data(N)

    with open("dummy_data.json", "w") as f:
        json.dump(data, f, indent=4, default=str)

    print(f"Datos dummy generados exitosamente con {N} registros por tabla.")
