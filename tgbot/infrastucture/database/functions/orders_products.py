from sqlalchemy import bindparam
from sqlalchemy import insert, select

from tgbot.infrastucture.database.models.orders import Order, OrderProduct
from tgbot.infrastucture.database.models.products import Product
from tgbot.infrastucture.database.models.users import User


def create_new_order_for_user(session, user_id):
    new_order = insert(
        Order
    ).values(
        user_id=user_id,
    ).returning(Order.order_id)
    result = session.execute(new_order)
    return result.scalar()


def show_users_orders(session):
    user_orders = select(
        Order.order_id, User.full_name
    ).join(
        User  # We can skip on clause here, let SQLAlchemy figure it out
    )
    result = session.execute(user_orders)
    return result.all()


def create_new_products(session, products_info):
    new_products = insert(
        Product
    ).values(
        products_info
    ).returning(
        Product.product_id
    )
    result = session.execute(new_products)
    return result.scalars()


def add_products_to_order(session, order_id, product_data):
    stmt = insert(
        OrderProduct
    ).values(
        order_id=order_id,
        product_id=bindparam('product_id'),
        quantity=bindparam('quantity'),
    )
    session.execute(stmt, product_data)


def show_all_users_products(session):
    stmt = select(
        Order.order_id, Product.title, User.full_name
    ).select_from(
        OrderProduct
    ).join(
        Product, Product.product_id == OrderProduct.product_id
    ).join(
        Order, Order.order_id == OrderProduct.order_id,
    ).join(
        User, User.telegram_id == Order.user_id
    )
    result = session.execute(stmt)
    return result.all()
