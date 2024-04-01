from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Создаем базовый класс, который будет использоваться для создания моделей
Base = declarative_base()


# Определяем модель (таблицу) как класс
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)


class managers(Base):
    __tablename__ = 'managers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String)
    password = Column(String)


class clients(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    manager_id = Column(Integer, ForeignKey("managers.id"))
    fio = Column(String)
    managers = relationship("managers")


class products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    header = Column(String)
    description = Column(String)
    stage = Column(Integer)


class parsing_info(Base):
    __tablename__ = 'parsing_info'
    id = Column(Integer, primary_key=True)
    content = Column(String)


class products_parsing_info(Base):
    __tablename__ = 'products-parsing_info'
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    parsing_id = Column(Integer, ForeignKey("parsing_info.id"), primary_key=True)
    products = relationship("products")
    parsing_info = relationship("parsing_info")


class clients_products(Base):
    __tablename__ = 'clients-products'
    client_id_id = Column(Integer, ForeignKey("clients.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    products = relationship("products")
    clients = relationship("clients")
