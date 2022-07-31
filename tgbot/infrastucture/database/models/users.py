from sqlalchemy import Column, BIGINT, VARCHAR, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func

from tgbot.infrastucture.database.models.base import Base


class User(Base):
    __tablename__ = 'users'

    telegram_id = Column(BIGINT, primary_key=True)
    full_name = Column(VARCHAR(255), nullable=False)
    username = Column(VARCHAR(255))
    language_code = Column(VARCHAR(10), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    referrer_id = Column(BIGINT, ForeignKey('users.telegram_id', ondelete='SET NULL'))
