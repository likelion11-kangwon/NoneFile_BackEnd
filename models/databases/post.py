import datetime
from pydantic import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.databases.base import Base
from models.databases.comment import Comment


class Post(BaseModel, Base):
    __tablename__ = "post_model"

    post_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    category_id: Mapped[int] = mapped_column()
    post_time: Mapped[datetime.datetime]
    post_name: Mapped[str] = mapped_column(String(500))
    post_info: Mapped[str] = mapped_column(String(15000))
    like: Mapped[int] = mapped_column()
    comment_id: Mapped[list["Comment"]] = relationship(
        back_populates="comment_id"
    )
