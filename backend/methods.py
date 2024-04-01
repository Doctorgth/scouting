from tables import clients, clients_products, products, products_parsing_info, parsing_info, managers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import database

tables = [clients, clients_products, products, products_parsing_info, parsing_info, managers]
table_names = ["clients", "clients_products", "products", "products_parsing_info", "parsing_info", "managers"]

session = 0


def catch_session(data):
    global session
    session = data


def get_table_class(table_name):

    try:
        pos = table_names.index(table_name)
        return tables[pos]
    except:
        return None


def add_record(table_name, data):
    table_class = get_table_class(table_name)
    if type(table_class) != type(None):
        new_record = table_class(**data)
        session.add(new_record)
        session.commit()
        return 0
    else:
        print(f"Table {table_name} not found")
        return -1


def get_record(table_name, column_name, value):
    table_class = get_table_class(table_name)
    if type(table_class) != type(None):
        records = session.query(table_class).filter(getattr(table_class, column_name) == value).all()
        return records
    else:
        print(f"Table {table_name} not found")
        return -1


def delete_record(table_name, column, value):
    table_class = get_table_class(table_name)
    if type(table_class) != type(None):
        session.query(table_class).filter(getattr(table_class, column) == value).delete()
        session.commit()
        return 0
    else:
        print(f"Table {table_name} not found")
        return -1


def update_record(table_name, field_name, new_value, condition_field, condition_value):
    table_class = get_table_class(table_name)
    if type(table_class) != type(None):
        session.query(table_class).filter(getattr(table_class, condition_field) == condition_value).update(
            {field_name: new_value}, synchronize_session=False)
        session.commit()
        return 0
    else:
        print(f"Table {table_name} not found")
        return -1
