from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from src.utils.database import Base


class Transaction(Base):

    __tablename__ = 'transactions'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    payment_id: Mapped[int] = mapped_column(
        ForeignKey("payments.id"),
        nullable=False,
    )

    action: Mapped[str] = mapped_column(
        nullable=False,
    )  # created, charged, refunded, failed, etc.

    status: Mapped[str] = mapped_column(
        nullable=False,
    )  # success / failed / pending

    message: Mapped[str] = mapped_column(
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False,
    )