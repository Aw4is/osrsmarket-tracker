from typing import List 
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String 
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

# individual 
class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    members: Mapped[bool] = mapped_column()
    high_alch: Mapped[int] = mapped_column()
    low_alch: Mapped[int] = mapped_column()
    buy_limit: Mapped[int | None] = mapped_column()
                