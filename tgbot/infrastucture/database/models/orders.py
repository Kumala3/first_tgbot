from sqlalchemy import Column, Integer, BIGINT, VARCHAR, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func

from tgbot.infrastucture.database.models.base import Base


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BIGINT, ForeignKey('users.telegram_id', ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())


class OrderProduct(Base):
    __tablename__ = 'order_products'

    order_id = Column(Integer, ForeignKey('orders.order_id', ondelete='CASCADE'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id', ondelete='RESTRICT'), primary_key=True)
    quantity = Column(Integer, nullable=False)